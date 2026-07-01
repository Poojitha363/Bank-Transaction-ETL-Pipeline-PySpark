import os
from pyspark.sql import SparkSession

os.environ["PYSPARK_PYTHON"] = "python"
os.environ["PYSPARK_DRIVER_PYTHON"] = "python"

spark = SparkSession.builder \
    .appName("Partitioning") \
    .getOrCreate()

# Read Dataset
df = spark.read.csv(
    "data/transactions.csv",
    header=True,
    inferSchema=True
)

print("\n========== ORIGINAL PARTITIONS ==========\n")

print(df.rdd.getNumPartitions())

# ----------------------------
# Repartition
# ----------------------------

df_repartition = df.repartition(4)

print("\n========== AFTER REPARTITION ==========\n")

print(df_repartition.rdd.getNumPartitions())

# ----------------------------
# Coalesce
# ----------------------------

df_coalesce = df_repartition.coalesce(2)

print("\n========== AFTER COALESCE ==========\n")

print(df_coalesce.rdd.getNumPartitions())

spark.stop()