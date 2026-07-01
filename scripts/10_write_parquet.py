import os
from pyspark.sql import SparkSession

os.environ["PYSPARK_PYTHON"] = "python"
os.environ["PYSPARK_DRIVER_PYTHON"] = "python"

spark = SparkSession.builder \
    .appName("Write Parquet") \
    .getOrCreate()

# Read Dataset
df = spark.read.csv(
    "data/transactions.csv",
    header=True,
    inferSchema=True
)

print("\n========== WRITING PARQUET ==========\n")

df.write \
    .mode("overwrite") \
    .parquet("output/parquet_data")

print("✅ Parquet file written successfully.")

print("\n========== READING PARQUET ==========\n")

parquet_df = spark.read.parquet(
    "output/parquet_data"
)

parquet_df.show(10)

spark.stop()