from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date

movies_input_path = './tmdb_comedy_movies.json'
series_input_path = './tmdb_comedy_series.json'
movies_target_path = './output/JSON/movies-parquet'
series_target_path = './output/JSON/series-parquet'

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
    "episode_run_time": "array<int>",
    "genre_ids": "array<int>",
    "first_air_date": "date",
    "id": "int",
    "name": "string",
    "number_of_episodes": "int",
    "number_of_seasons": "int",
    "origin_country": "array<string>",
    "original_language": "string",
    "original_name": "string",
    "popularity": "float",
    "vote_average": "float",
    "vote_count": "int"
}

def process_json_to_parquet(input_path, target_path, tipo_arquivo):
    print(f"Processando {tipo_arquivo}...")

    df = spark.read.option("multiline", "true").json(input_path)

    if tipo_arquivo == "filmes":
        df = df.drop("adult", "video", "backdrop_path", "belongs_to_collection", "homepage", "overview", "tagline", "production_companies", "production_countries", "poster_path", "spoken_languages", "genres")
        for column, data_type in movies_cast.items():
            if data_type == "date":
                df = df.withColumn(column, to_date(col(column)))
            else:
                df = df.withColumn(column, col(column).cast(data_type))
    else:
        df = df.drop("adult", "type", "status", "spoken_languages", "seasons", "production_countries", "production_companies", "taglines", "poster_path", "overview", "next_episode_to_air", "networks", "last_episode_to_air", "last_air_date", "in_production", "homepage", "genres", "created_by", "backdrop_path")
        for column, data_type in series_cast.items():
            if data_type == "date":
                df = df.withColumn(column, to_date(col(column)))
            else:
                df = df.withColumn(column, col(column).cast(data_type))

    df.show()
    df.printSchema()

    df.repartition(1).write.mode('overwrite').parquet(target_path)

    print(f"{tipo_arquivo} salvo em {target_path}")

spark = SparkSession.builder.master("local").appName("parquet_json").getOrCreate()

process_json_to_parquet(movies_input_path, movies_target_path, "filmes")
process_json_to_parquet(series_input_path, series_target_path, "series")

spark.stop()
