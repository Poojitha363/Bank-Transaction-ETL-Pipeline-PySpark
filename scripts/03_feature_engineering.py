import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

os.environ["PYSPARK_PYTHON"] = "python"
os.environ["PYSPARK_DRIVER_PYTHON"] = "python"

spark = SparkSession.builder \
    .appName("Feature Engineering") \
    .getOrCreate()

# Read Dataset
df = spark.read.csv(
    "data/transactions.csv",
    header=True,
    inferSchema=True
)

print("\n========== ORIGINAL DATA ==========\n")
df.show(10)

# ----------------------------
# Feature 1: High Value Transaction
# ----------------------------

df = df.withColumn(
    "high_value_transaction",
    when(col("amount") > 200000, "YES").otherwise("NO")
)

# ----------------------------
# Feature 2: Balance Difference
# ----------------------------

df = df.withColumn(
    "balance_difference",
    col("oldbalanceOrg") - col("newbalanceOrig")
)

# ----------------------------
# Feature 3: Fraud Label
# ----------------------------

df = df.withColumn(
    "fraud_label",
    when(col("isFraud") == 1, "Fraud").otherwise("Normal")
)

print("\n========== FEATURE ENGINEERING ==========\n")
df.select(
    "type",
    "amount",
    "high_value_transaction",
    "balance_difference",
    "fraud_label"
).show(20)

spark.stop()