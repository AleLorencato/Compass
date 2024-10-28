import sys
import re
from pyspark.sql import SparkSession
from pyspark.sql.functions import when, col, split
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME, S3_MOVIES_INPUT_PATH, S3_SERIES_INPUT_PATH, S3_MOVIES_TARGET_PATH, S3_SERIES_TARGET_PATH]

args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_MOVIES_INPUT_PATH', 'S3_SERIES_INPUT_PATH', 'S3_MOVIES_TARGET_PATH', 'S3_SERIES_TARGET_PATH'])

spark = SparkSession.builder.appName("parquet_csv").getOrCreate()
glueContext = GlueContext(spark.sparkContext)
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

movies_input_path = args['S3_MOVIES_INPUT_PATH']
series_input_path = args['S3_SERIES_INPUT_PATH']
movies_target_path = args['S3_MOVIES_TARGET_PATH']
series_target_path = args['S3_SERIES_TARGET_PATH']

movies_cast = {
    "id": "string",
    "tituloPrincipal": "string",
    "tituloOriginal": "string",
    "anoLancamento": "int",
    "tempoMinutos": "int",
    "genero": "string",
    "notaMedia": "float",
    "numeroVotos": "int",
    "generoArtista": "string",
    "profissao": "array<string>",
    "titulosMaisConhecidos": "array<string>"
}
series_cast = {
    "id": "string",
    "tituloPrincipal": "string",
    "tituloOriginal": "string",
    "anoLancamento": "int",
    "tempoMinutos": "int",
    "genero": "string",
    "notaMedia": "float",
    "numeroVotos": "int",
    "generoArtista": "string",
    "profissao": "array<string>",
    "titulosMaisConhecidos": "array<string>"
}

def extract_date_from_path(input_path):
    match = re.search(r'(\d{4})/(\d{2})/(\d{2})', input_path)
    if match:
        year, month, day = match.groups()
        return year, month, day
    else:
        raise ValueError("Caminho de entrada não contém uma data válida no formato YYYY/MM/DD")

def process_csv_to_parquet(input_path, target_path, tipo_arquivo):
    print(f"Processando {tipo_arquivo}...")

    df = spark.read.option("delimiter", "|").option("header", "true").csv(input_path)

    df = df.withColumn("is_comedy", when(df.genero == "Comedy", 1).otherwise(0))

    df_comedy = df.filter(df.is_comedy == 1)

    df_comedy = df_comedy.drop("is_comedy")

    if tipo_arquivo == "filmes":
        df = df.drop("nomeArtista","anoNascimento", "anoFalecimento", "personagem")
        for column, data_type in movies_cast.items():
            if column in df.columns:
                if data_type == "string":
                    df = df.withColumn(column, when(col(column) == '\n', 'null').otherwise(col(column)))
                elif data_type == "int" or data_type == "float":
                    df = df.withColumn(column, when(col(column) == '\n', 0).otherwise(col(column)))
                elif data_type == "array<string>":
                    df = df.withColumn(column, when(col(column).contains('\n'), 'null').otherwise(col(column)))

        for column, data_type in movies_cast.items():
            if column in df.columns:
                if data_type == "array<string>":
                    df = df.withColumn(column, split(col(column), ','))
            else:
                df = df.withColumn(column, col(column).cast(data_type))
    else:
        df = df.drop("anoTermino","nomeArtista","anoNascimento", "anoFalecimento", "personagem")
        for column, data_type in series_cast.items():
            if column in df.columns:
                if data_type == "string":
                    df = df.withColumn(column, when(col(column) == '\n', 'null').otherwise(col(column)))
                elif data_type == "int" or data_type == "float":
                    df = df.withColumn(column, when(col(column) == '\n', 0).otherwise(col(column)))
                elif data_type == "array<string>":
                    df = df.withColumn(column, when(col(column).contains('\n'), 'null').otherwise(col(column)))

        for column, data_type in series_cast.items():
            if column in df.columns:
                if data_type == "array<string>":
                    df = df.withColumn(column, split(col(column), ','))
                else:
                    df = df.withColumn(column, col(column).cast(data_type))

    year, month, day = extract_date_from_path(input_path)

    dynamic_target_path = f"{target_path}/{year}/{month}/{day}/"

    df_comedy.repartition(2).write.mode('overwrite').parquet(dynamic_target_path)

    print(f"{tipo_arquivo} salvo em {dynamic_target_path}")

process_csv_to_parquet(movies_input_path, movies_target_path, "filmes")

process_csv_to_parquet(series_input_path, series_target_path, "series")

job.commit()
