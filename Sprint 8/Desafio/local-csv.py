from pyspark.sql import SparkSession
from pyspark.sql.functions import when, col, split

movies_input_path = './movies.csv'
series_input_path = './series.csv'
movies_target_path = './output/CSV/movies-parquet'
series_target_path = './output/CSV/series-parquet'

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

def process_csv_to_parquet(input_path, target_path, tipo_arquivo):
    print(f"Processando {tipo_arquivo}...")

    df = spark.read.option("delimiter", "|").option("header", "true").csv(input_path)

    df = df.withColumn("is_comedy", when(df.genero == "Comedy", 1).otherwise(0))

    df_comedy = df.filter(df.is_comedy == 1).drop("is_comedy")

    if tipo_arquivo == "filmes":
        df_comedy = df_comedy.drop("nomeArtista", "anoNascimento", "anoFalecimento", "personagem")
        for column, data_type in movies_cast.items():
            if column in df_comedy.columns:
                if data_type == "string":
                    df_comedy = df_comedy.withColumn(column, when(col(column) == '\n', 'null').otherwise(col(column)))
                elif data_type == "int" or data_type == "float":
                    df_comedy = df_comedy.withColumn(column, when(col(column) == '\n', 0).otherwise(col(column)))
                elif data_type == "array<string>":
                    df_comedy = df_comedy.withColumn(column, when(col(column).contains('\n'), 'null').otherwise(col(column)))

        for column, data_type in movies_cast.items():
            if column in df_comedy.columns:
                if data_type == "array<string>":
                    df_comedy = df_comedy.withColumn(column, split(col(column), ','))
                else:
                    df_comedy = df_comedy.withColumn(column, col(column).cast(data_type))
    else:
        df_comedy = df_comedy.drop("anoTermino", "nomeArtista", "anoNascimento", "anoFalecimento", "personagem")
        for column, data_type in series_cast.items():
            if column in df_comedy.columns:
                if data_type == "string":
                    df_comedy = df_comedy.withColumn(column, when(col(column) == '\n', 'null').otherwise(col(column)))
                elif data_type == "int" or data_type == "float":
                    df_comedy = df_comedy.withColumn(column, when(col(column) == '\n', 0).otherwise(col(column)))
                elif data_type == "array<string>":
                    df_comedy = df_comedy.withColumn(column, when(col(column).contains('\n'), 'null').otherwise(col(column)))

        for column, data_type in series_cast.items():
            if column in df_comedy.columns:
                if data_type == "array<string>":
                    df_comedy = df_comedy.withColumn(column, split(col(column), ','))
                else:
                    df_comedy = df_comedy.withColumn(column, col(column).cast(data_type))

    df_comedy.show()
    df_comedy.printSchema()

    df_comedy.repartition(2).write.mode('overwrite').parquet(target_path)

    print(f"{tipo_arquivo} salvo em {target_path}")

spark = SparkSession.builder.master("local").appName("parquet_csv").getOrCreate()

process_csv_to_parquet(movies_input_path, movies_target_path, "filmes")
process_csv_to_parquet(series_input_path, series_target_path, "series")


spark.stop()
