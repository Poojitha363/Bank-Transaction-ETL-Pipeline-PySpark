from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, avg, max, min, count

spark = SparkSession.builder \
    .appName("Aggregations") \
    .getOrCreate()

df = spark.read.csv(
    "data/transactions.csv",
    header=True,
    inferSchema=True
)

result = df.groupBy("type").agg(
    count("*").alias("total_transactions"),
    sum("amount").alias("total_amount"),
    avg("amount").alias("average_amount"),
    max("amount").alias("highest_amount"),
    min("amount").alias("lowest_amount")
)

print("\n========== AGGREGATIONS ==========\n")

result.show()

spark.stop()