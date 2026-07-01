from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Spark SQL Analysis") \
    .getOrCreate()

df = spark.read.csv(
    "data/transactions.csv",
    header=True,
    inferSchema=True
)

df.createOrReplaceTempView("transactions")

result = spark.sql("""
SELECT
type,
COUNT(*) AS total_transactions,
ROUND(AVG(amount),2) AS avg_amount,
ROUND(MAX(amount),2) AS max_amount,
ROUND(MIN(amount),2) AS min_amount
FROM transactions
GROUP BY type
ORDER BY total_transactions DESC
""")

print("\n========== SPARK SQL ANALYSIS ==========\n")

result.show()

spark.stop()