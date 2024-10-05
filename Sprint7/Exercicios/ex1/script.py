from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ex1").getOrCreate()

wget blob:https://github.com/b64dc929-b866-4871-9935-d8e91e3e135a

text_file = spark.read.text("copia-readme.md")

words = text_file.selectExpr("split(value, ' ') as words")

word_counts = words.selectExpr("explode(words) as word").groupBy("word").count()

word_counts.show()
