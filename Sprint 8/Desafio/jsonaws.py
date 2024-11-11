import sys
import re
import boto3
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME, S3_MOVIES_INPUT_PATH, S3_SERIES_INPUT_PATH, S3_MOVIES_TARGET_PATH, S3_SERIES_TARGET_PATH]

args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_MOVIES_INPUT_PATH', 'S3_SERIES_INPUT_PATH', 'S3_MOVIES_TARGET_PATH', 'S3_SERIES_TARGET_PATH'])

spark = SparkSession.builder.appName("parquet_json").getOrCreate()
glueContext = GlueContext(spark.sparkContext)
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

movies_input_path = args['S3_MOVIES_INPUT_PATH']
series_input_path = args['S3_SERIES_INPUT_PATH']
movies_target_path = args['S3_MOVIES_TARGET_PATH']
series_target_path = args['S3_SERIES_TARGET_PATH']

movies_cast = {
    "id": "int",
    "budget": "int",
    "revenue": "int",
    "runtime": "int",
    "vote_average": "float",
    "vote_count": "int",
    "popularity": "float",
    "release_date": "date",
    "status": "string",
    "genre_ids": "array<int>"
}

series_cast = {
    "episode_run_time":"array<int>",
    "genre_ids":"array<int>",
    "first_air_date":"date",
    "id":"int",
    "name":"string",
    "number_of_episodes":"int",
    "origin_country":"array<string>",
    "original_language":"string",
    "original_name":"string",
    "popularity":"float",
    "vote_average":"float",
    "vote_count":"int"
}

s3 = boto3.client('s3')

def list_s3_files(bucket_name, prefix):
    file_list = []
    result = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
    for obj in result.get('Contents', []):
        file_list.append(obj['Key'])

    return file_list

def extract_date_from_path(input_path):
    match = re.search(r'(\d{4})/(\d{2})/(\d{2})', input_path)
    if match:
        year, month, day = match.groups()
        return year, month, day
    else:
        raise ValueError("Caminho de entrada não contém uma data válida no formato YYYY/MM/DD")

def process_json_to_parquet(input_path, target_path, tipo_arquivo):
    print(f"Processando {tipo_arquivo}...")

    bucket_name = input_path.split('/')[2]
    prefix = '/'.join(input_path.split('/')[3:])

    file_list = list_s3_files(bucket_name, prefix)

    for file_path in file_list:
        print(f"Processando arquivo: {file_path}")

        year, month, day = extract_date_from_path(file_path)

        dynamic_target_path = f"{target_path}/{year}/{month}/{day}/"

        df = spark.read.option("multiline", "true").json(f"s3://{bucket_name}/{file_path}")
        if(tipo_arquivo == "filmes"):
            df = df.drop("adult", "video","backdrop_path","belongs_to_collection","homepage","overview","tagline","production_companies","production_countries","poster_path","spoken_languages","genres","id","status")
            for column, data_type in movies_cast.items():
                if data_type == "date":
                    df = df.withColumn(column, to_date(col(column)))
                else:
                    df = df.withColumn(column, col(column).cast(data_type))
        else:
            df = df.drop("adult","type","status","spoken_languages","seasons","production_countries","production_companies","tagline","poster_path","overview","next_episode_to_air","networks","last_episode_to_air","last_air_date","in_production","homepage","genres","created_by","backdrop_path","number_of_seasons","languages")

            for column, data_type in series_cast.items():
                if data_type == "date":
                    df = df.withColumn(column, to_date(col(column)))
                else:
                    df = df.withColumn(column, col(column).cast(data_type))


        df.repartition(1).write.mode('overwrite').parquet(dynamic_target_path)

        print(f"{tipo_arquivo} salvo em {dynamic_target_path}")

process_json_to_parquet(movies_input_path, movies_target_path, "filmes")

process_json_to_parquet(series_input_path, series_target_path, "series")

job.commit()
