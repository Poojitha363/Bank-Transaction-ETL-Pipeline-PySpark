import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import count, sum, col

os.environ["PYSPARK_PYTHON"] = "python"
os.environ["PYSPARK_DRIVER_PYTHON"] = "python"

spark = SparkSession.builder \
    .appName("Customer Analysis") \
    .getOrCreate()

# Read Dataset
df = spark.read.csv(
    "data/transactions.csv",
    header=True,
    inferSchema=True
)

print("\n========== TOP 10 SENDERS ==========\n")

df.groupBy("nameOrig") \
  .agg(count("*").alias("Total Transactions")) \
  .orderBy(col("Total Transactions").desc()) \
  .show(10, truncate=False)

print("\n========== TOP 10 RECEIVERS ==========\n")

df.groupBy("nameDest") \
  .agg(count("*").alias("Total Transactions")) \
  .orderBy(col("Total Transactions").desc()) \
  .show(10, truncate=False)

print("\n========== TOP 10 CUSTOMERS BY AMOUNT SENT ==========\n")

df.groupBy("nameOrig") \
  .agg(sum("amount").alias("Total Amount")) \
  .orderBy(col("Total Amount").desc()) \
  .show(10, truncate=False)

spark.stop()