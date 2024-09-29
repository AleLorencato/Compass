import datetime
import boto3
import os
from dotenv import load_dotenv
from botocore.exceptions import ClientError

load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_SESSION_TOKEN = os.getenv("AWS_SESSION_TOKEN")

Bucketname = "compass-desafio-final"

client = boto3.client('s3', 
                      aws_access_key_id=AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                      aws_session_token=AWS_SESSION_TOKEN)

def put_object_to_s3(local_file, s3_file):
    try:
        with open(local_file, 'rb') as data:
            client.put_object(Bucket=Bucketname, Key=s3_file, Body=data)
            print(f"Upload com put_object realizado para {s3_file}")
    except ClientError as e:
        print(f"Erro no upload: {e}")
        return False
    return True


# Pegar a data atual
date = datetime.datetime.now().strftime("%Y/%m/%d")
print(f"Data atual: {date}")
# Caminho local e S3
local_file_movies = './movies.csv'
s3_file_movies = (f'Raw/Local/CSV/Movies/{date}/movies.csv')

local_file_series = './series.csv'
s3_file_series = (f'Raw/Local/CSV/Series/{date}/series.csv')

# Enviar arquivo

put_object_to_s3(local_file_movies, s3_file_movies)
put_object_to_s3(local_file_series, s3_file_series)