import requests
import json
import boto3
import os
import datetime
from botocore.exceptions import ClientError

Bucketname = "compass-desafio-final"

client = boto3.client('s3')

BASE_URL = os.environ['BASE_URL']
API_KEY = os.environ['API_KEY']
READ_TOKEN = os.environ['READ_TOKEN']

def fetch_movies_by_genre(genre_id, genre_name, max_movies=100):
    url = f'{BASE_URL}/discover/movie'
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {READ_TOKEN}"
    }
    params = {
        'api_key': API_KEY,
        'language': 'en-US',
        'with_genres': genre_id,
        'primary_release_date.gte': '1894-01-01',
        'primary_release_date.lte': '2022-12-31',
        'page': 1
    }

    all_movies = []
    while len(all_movies) < max_movies:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            all_movies.extend(data['results'])
            if len(data['results']) == 0 or len(all_movies) >= max_movies:
                break
            params['page'] += 1
        else:
            print(f"Erro na requisição: {response.status_code}")
            break

    all_movies = all_movies[:max_movies]
    for movie in all_movies:
        movie_details = fetch_movie_details(movie['id'])
        if movie_details:
            movie.update(movie_details)

    date = datetime.datetime.now().strftime("%Y/%m/%d")
    put_object_to_s3(all_movies, genre_name, date, 'Movies')

def fetch_movie_details(movie_id):
    url = f'{BASE_URL}/movie/{movie_id}'
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {READ_TOKEN}"
    }
    params = {
        'api_key': API_KEY,
        'language': 'en-US',
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao buscar detalhes do filme {movie_id}: {response.status_code}")
        return {}

def fetch_series_by_genre(genre_id, genre_name, max_series=100):
    url = f'{BASE_URL}/discover/tv'
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {READ_TOKEN}"
    }
    params = {
        'api_key': API_KEY,
        'language': 'en-US',
        'with_genres': genre_id,
        'first_air_date.gte': '1894-01-01',
        'first_air_date.lte': '2022-12-31',
        'page': 1
    }

    all_series = []
    while len(all_series) < max_series:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            all_series.extend(data['results'])
            if len(data['results']) == 0 or len(all_series) >= max_series:
                break
            params['page'] += 1
        else:
            print(f"Erro na requisição: {response.status_code}")
            break

    all_series = all_series[:max_series]
    for serie in all_series:
        serie_details = fetch_serie_details(serie['id'])
        if serie_details:
            serie.update(serie_details)

    date = datetime.datetime.now().strftime("%Y/%m/%d")
    put_object_to_s3(all_series, genre_name, date, 'Series')

def fetch_serie_details(serie_id):
    url = f'{BASE_URL}/tv/{serie_id}'
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {READ_TOKEN}"
    }
    params = {
        'api_key': API_KEY,
        'language': 'en-US',
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao buscar detalhes da série {serie_id}: {response.status_code}")
        return {}

def put_object_to_s3(data, genre_name, date, content_type):
    s3_file = f'Raw/Local/TMDB/JSON/{content_type}/{date}/tmdb_{genre_name}_{content_type.lower()}.json'
    try:
        file_content = json.dumps(data, ensure_ascii=False, indent=4)
        client.put_object(Bucket=Bucketname, Key=s3_file, Body=file_content)
        print(f"Upload realizado para {s3_file}")
    except ClientError as e:
        print(f"Erro no upload para o S3: {e}")
        return False
    return True

def lambda_handler(event, context):
    fetch_movies_by_genre('35', 'comedy')
    fetch_series_by_genre('35', 'comedy')
    return {
        'statusCode': 200,
        'body': 'Terminei com sucesso'
    }
