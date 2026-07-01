import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import rank, dense_rank, row_number, col
from pyspark.sql.window import Window

os.environ["PYSPARK_PYTHON"] = "python"
os.environ["PYSPARK_DRIVER_PYTHON"] = "python"

spark = SparkSession.builder \
    .appName("Window Functions") \
    .getOrCreate()

# Read Dataset
df = spark.read.csv(
    "data/transactions.csv",
    header=True,
    inferSchema=True
)

# Window Specification
window_spec = Window.orderBy(col("amount").desc())

# Row Number
df = df.withColumn(
    "row_number",
    row_number().over(window_spec)
)

# Rank
df = df.withColumn(
    "rank",
    rank().over(window_spec)
)

# Dense Rank
df = df.withColumn(
    "dense_rank",
    dense_rank().over(window_spec)
)

print("\n========== WINDOW FUNCTIONS ==========\n")

df.select(
    "type",
    "amount",
    "row_number",
    "rank",
    "dense_rank"
).show(20, truncate=False)

spark.stop()