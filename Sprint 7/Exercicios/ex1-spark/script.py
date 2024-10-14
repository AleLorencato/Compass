text_file = spark.read.text("README.md")

words = text_file.selectExpr("split(value, ' ') as words")

word_counts = words.selectExpr("explode(words) as word").groupBy("word").count()

word_counts.show()
