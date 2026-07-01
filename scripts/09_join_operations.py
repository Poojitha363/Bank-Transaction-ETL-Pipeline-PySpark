import os
from pyspark.sql import SparkSession

os.environ["PYSPARK_PYTHON"] = "python"
os.environ["PYSPARK_DRIVER_PYTHON"] = "python"

spark = SparkSession.builder \
    .appName("Join Operations") \
    .getOrCreate()

# Read Transactions Dataset
transactions_df = spark.read.csv(
    "data/transactions.csv",
    header=True,
    inferSchema=True
)

# Create Customer Dataset
customer_data = [
    ("C1231006815", "Gold"),
    ("C1666544295", "Silver"),
    ("C1305486145", "Platinum"),
    ("C840083671", "Gold"),
    ("C2048537720", "Silver")
]

customer_df = spark.createDataFrame(
    customer_data,
    ["nameOrig", "customer_type"]
)

print("\n========== CUSTOMER DATA ==========\n")
customer_df.show()

# -----------------------------
# INNER JOIN
# -----------------------------

print("\n========== INNER JOIN ==========\n")

inner_join = transactions_df.join(
    customer_df,
    on="nameOrig",
    how="inner"
)

inner_join.select(
    "nameOrig",
    "customer_type",
    "amount",
    "type"
).show(truncate=False)

# -----------------------------
# LEFT JOIN
# -----------------------------

print("\n========== LEFT JOIN ==========\n")

left_join = transactions_df.join(
    customer_df,
    on="nameOrig",
    how="left"
)

left_join.select(
    "nameOrig",
    "customer_type",
    "amount",
    "type"
).show(20, truncate=False)

spark.stop()