import os
from pyspark.sql import SparkSession

os.environ["PYSPARK_PYTHON"] = "python"
os.environ["PYSPARK_DRIVER_PYTHON"] = "python"

spark = SparkSession.builder \
    .appName("Bank Transaction ETL") \
    .getOrCreate()

df = spark.read.csv(
    "data/transactions_data.csv",
    header=True,
    inferSchema=True
)

print("\n========== FIRST 10 ROWS ==========\n")
df.show(10)

print("\n========== SCHEMA ==========\n")
df.printSchema()

print("\n========== TOTAL RECORDS ==========\n")
print(df.count())

spark.stop()