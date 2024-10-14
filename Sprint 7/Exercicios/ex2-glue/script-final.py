import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as F

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']
df = glueContext.create_dynamic_frame.from_options(
    "s3",
    {"paths": [source_file]},
    "csv",
    {"withHeader": True, "separator": ","}
).toDF()

df_uppercase = df.withColumn("nome", F.upper(F.col("nome")))

print(f"Contagem de linhas: {df_uppercase.count()}")

df_grouped = df_uppercase.groupBy("ano", "sexo").count()
df_grouped.show()

df_sorted = df_uppercase.orderBy(F.col("ano").desc())
df_sorted.show()

fem_max = df_uppercase.filter(F.col("sexo") == "F").groupBy("nome", "ano").count().orderBy(F.col("count").desc()).first()
print(f"Nome feminino mais comum: {fem_max['nome']}, Ano: {fem_max['ano']}")

masc_max = df_uppercase.filter(F.col("sexo") == "M").groupBy("nome", "ano").count().orderBy(F.col("count").desc()).first()
print(f"Nome masculino mais comum: {masc_max['nome']}, Ano: {masc_max['ano']}")

df_total_per_year = df_uppercase.groupBy("ano", "sexo").count().orderBy("ano").show()

df_top_10 = df_uppercase.orderBy(F.col("ano").asc()).limit(10)
df_top_10.show()

target_path = args['S3_TARGET_PATH']
df_uppercase.write.partitionBy("sexo", "ano").format("json").save(f"{target_path}/frequencia_registro_nomes_eua")

job.commit()
