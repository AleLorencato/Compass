from pyspark.sql import SparkSession
from pyspark.sql.functions import year

spark = SparkSession.builder.appName("Exemplo").getOrCreate()

arqschema = "id INT, nome STRING, status STRING, cidade STRING, vendas INT, data STRING"

despachantes = spark.read.csv("./despachantes.csv", header=False, schema=arqschema)

calculo = despachantes.select("data").groupBy(year("data").alias("year")).count()

calculo.show()

calculo.write.format("csv").save("./output")

spark.stop()
