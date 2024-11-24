import sys
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, array_contains, row_number
from pyspark.sql.window import Window
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, [
    'JOB_NAME',
    'S3_CSV_MOVIES_INPUT_PATH',
    'S3_JSON_MOVIES_INPUT_PATH',
    'S3_CSV_SERIES_INPUT_PATH',
    'S3_JSON_SERIES_INPUT_PATH',
    'S3_TARGET_PATH'
])

# Initialize Spark and Glue contexts
spark = SparkSession.builder.appName("RefinedDataProcessing").getOrCreate()
glueContext = GlueContext(spark.sparkContext)
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Paths for input and outputs
csv_movies_input_path = args['S3_CSV_MOVIES_INPUT_PATH']
json_movies_input_path = args['S3_JSON_MOVIES_INPUT_PATH']

csv_series_input_path = args['S3_CSV_SERIES_INPUT_PATH']
json_series_input_path = args['S3_JSON_SERIES_INPUT_PATH']

output_path = args['S3_TARGET_PATH']

def carregar_dataframe(caminho):
    return spark.read.option("mergeSchema", "true").parquet(f'{caminho}/*/*/*')

def salvar_parquet(df, caminho):
    df.coalesce(1).write.mode('overwrite').parquet(caminho)

def processar_filmes(csv_path, json_path, output_path):
    csv_movies_df = carregar_dataframe(csv_path)
    json_movies_df = carregar_dataframe(json_path)

    csv_movies_df = csv_movies_df.drop_duplicates()
    json_movies_df = json_movies_df.drop_duplicates()

    df_movies = csv_movies_df.join(json_movies_df, csv_movies_df.id == json_movies_df.imdb_id, how='inner')

    fact_movies = df_movies.select('id', 'tituloPrincipal', 'original_title', 'imdb_id', 'popularity', 'budget', 'revenue').distinct()
    dim_country = df_movies.select('original_title', 'origin_country', 'original_language', 'id').distinct()
    dim_grades = df_movies.select('imdb_id', 'vote_average', 'vote_count', 'notaMedia', 'numeroVotos', 'id').distinct()

    salvar_parquet(fact_movies, os.path.join(output_path, 'movies/fact_movies'))
    salvar_parquet(dim_country, os.path.join(output_path, 'movies/dim_country'))
    salvar_parquet(dim_grades, os.path.join(output_path, 'movies/dim_grades'))

def processar_series(csv_path, json_path, output_path):
    csv_series_df = carregar_dataframe(csv_path)
    json_series_df = carregar_dataframe(json_path)

    csv_series_df = csv_series_df.drop_duplicates()
    json_series_df = json_series_df.drop_duplicates().drop('genre_ids').withColumnRenamed('id', 'id_json')
    csv_series_df = csv_series_df.drop('genero')

    df_series = csv_series_df.join(json_series_df, csv_series_df.tituloOriginal == json_series_df.original_name, how='inner')
    df_series = df_series.withColumn('has_director', when(array_contains(col('profissao'), 'director'), 1).otherwise(0))
    window_spec_series = Window.partitionBy('id').orderBy(col('has_director').desc())
    df_series = df_series.withColumn('row_num', row_number().over(window_spec_series))
    df_dedup_series = df_series.filter(col('row_num') == 1).drop('has_director', 'row_num')

    fact_series = df_dedup_series.select('id', 'tituloPrincipal', 'original_name', 'id_json', 'popularity').distinct()
    dim_production = df_dedup_series.select('tituloPrincipal', 'generoArtista', 'profissao', 'id').distinct()
    dim_country = df_dedup_series.select('original_name', 'origin_country', 'original_language', 'id').distinct()
    dim_grades = df_dedup_series.select('id_json', 'vote_average', 'vote_count', 'notaMedia', 'numeroVotos', 'id').distinct()

    salvar_parquet(fact_series, os.path.join(output_path, 'series/fact_series'))
    salvar_parquet(dim_production, os.path.join(output_path, 'series/dim_production'))
    salvar_parquet(dim_country, os.path.join(output_path, 'series/dim_country'))
    salvar_parquet(dim_grades, os.path.join(output_path, 'series/dim_grades'))

processar_filmes(csv_movies_input_path, json_movies_input_path, output_path)
processar_series(csv_series_input_path, json_series_input_path, output_path)

job.commit()
spark.stop()
