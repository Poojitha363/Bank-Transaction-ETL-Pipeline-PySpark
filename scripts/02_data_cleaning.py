import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

os.environ["PYSPARK_PYTHON"] = "python"
os.environ["PYSPARK_DRIVER_PYTHON"] = "python"

spark = SparkSession.builder \
    .appName("Data Cleaning") \
    .getOrCreate()

# Read CSV
df = spark.read.csv(
    "data/transactions.csv",   # rename cheyyakapothe transactions_data.csv pettu
    header=True,
    inferSchema=True
)

print("\n========== TOTAL RECORDS ==========\n")
print(df.count())

print("\n========== MISSING VALUES ==========\n")

for column in df.columns:
    print(column, ":", df.filter(col(column).isNull()).count())

print("\n========== REMOVE DUPLICATES ==========\n")

before = df.count()

df = df.dropDuplicates()

after = df.count()

print("Before :", before)
print("After  :", after)

print("\n========== DATA TYPES ==========\n")

df.printSchema()

print("\n========== CLEANED DATA ==========\n")

df.show(10)

spark.stop()