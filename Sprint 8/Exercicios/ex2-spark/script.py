from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext

spark = SparkSession.builder.master("local[*]").appName("Ex3").getOrCreate()

df_nomes = spark.read.csv("../ex1-python/nomes_aleatorios.txt")

df_nomes.show(5)

spark.stop()
