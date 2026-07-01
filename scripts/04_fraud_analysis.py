import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, sum

os.environ["PYSPARK_PYTHON"] = "python"
os.environ["PYSPARK_DRIVER_PYTHON"] = "python"

spark = SparkSession.builder \
    .appName("Fraud Analysis") \
    .getOrCreate()

# Read Dataset
df = spark.read.csv(
    "data/transactions.csv",
    header=True,
    inferSchema=True
)

print("\n========== TOTAL TRANSACTIONS ==========\n")
print(df.count())

# ----------------------------
# Fraud vs Normal
# ----------------------------

print("\n========== FRAUD VS NORMAL ==========\n")

df.groupBy("isFraud").count().show()

# ----------------------------
# Fraud by Transaction Type
# ----------------------------

print("\n========== FRAUD BY TRANSACTION TYPE ==========\n")

df.filter(col("isFraud") == 1) \
  .groupBy("type") \
  .count() \
  .show()

# ----------------------------
# Total Fraud Amount
# ----------------------------

print("\n========== TOTAL FRAUD AMOUNT ==========\n")

df.filter(col("isFraud") == 1) \
  .agg(sum("amount").alias("Total Fraud Amount")) \
  .show()

# ----------------------------
# Top 10 Biggest Fraud Transactions
# ----------------------------

print("\n========== TOP 10 FRAUD TRANSACTIONS ==========\n")

df.filter(col("isFraud") == 1) \
  .select("type", "amount", "nameOrig", "nameDest") \
  .orderBy(col("amount").desc()) \
  .show(10, truncate=False)

spark.stop()