import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, avg, max, min, count, col

os.environ["PYSPARK_PYTHON"] = "python"
os.environ["PYSPARK_DRIVER_PYTHON"] = "python"

spark = SparkSession.builder \
    .appName("Transaction Analysis") \
    .getOrCreate()

# Read Dataset
df = spark.read.csv(
    "data/transactions.csv",
    header=True,
    inferSchema=True
)

print("\n========== TOTAL TRANSACTION AMOUNT ==========\n")

df.select(
    sum("amount").alias("Total Amount")
).show()

print("\n========== AVERAGE TRANSACTION AMOUNT ==========\n")

df.select(
    avg("amount").alias("Average Amount")
).show()

print("\n========== MAXIMUM TRANSACTION ==========\n")

df.select(
    max("amount").alias("Maximum Amount")
).show()

print("\n========== MINIMUM TRANSACTION ==========\n")

df.select(
    min("amount").alias("Minimum Amount")
).show()

print("\n========== TRANSACTION COUNT BY TYPE ==========\n")

df.groupBy("type") \
  .agg(count("*").alias("Total Transactions")) \
  .orderBy(col("Total Transactions").desc()) \
  .show()

spark.stop()