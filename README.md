# 🚀 Bank Transaction ETL Pipeline using PySpark

## 📌 Project Overview

This project demonstrates an End-to-End ETL Pipeline built using Apache Spark (PySpark) on a real-world banking transaction dataset.

The pipeline reads millions of bank transactions from a CSV dataset, performs data cleaning, feature engineering, fraud analysis, Spark SQL queries, joins, window functions, partitioning, and writes the processed data in Parquet format (Hadoop-compatible environments).

The project follows real-world Data Engineering practices and showcases distributed data processing using Apache Spark.

---

# 🏗️ Project Architecture

```
Bank Transaction Dataset (CSV)
            │
            ▼
      PySpark DataFrame
            │
            ▼
      Data Cleaning
            │
            ▼
   Feature Engineering
            │
            ▼
 Fraud Detection & Analysis
            │
            ▼
 Aggregations & Spark SQL
            │
            ▼
 Joins & Window Functions
            │
            ▼
Partition Optimization
            │
            ▼
 Parquet Output (Hadoop Compatible)
```

---

# 📂 Project Folder Structure

```
Bank_Transaction_ETL_Pipeline/
│
├── data/
│   └── transactions_data.csv
│
├── output/
│
├── screenshots/
│   ├── 01_read_transactions.png
│   ├── 02_fraud_analysis.png
│   ├── 03_transaction_analysis.png
│   ├── 04_customer_analysis.png
│   ├── 05_window_functions.png
│   ├── 06_joins.png
│   ├── 07_spark_sql.png
│   └── 08_aggregations.png
│
├── scripts/
│   ├── 01_read_transactions.py
│   ├── 02_data_cleaning.py
│   ├── 03_feature_engineering.py
│   ├── 04_fraud_analysis.py
│   ├── 05_partitioning.py
│   ├── 06_transaction_analysis.py
│   ├── 07_customer_analysis.py
│   ├── 08_window_functions.py
│   ├── 09_joins.py
│   ├── 10_spark_sql.py
│   └── 11_aggregations.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Programming |
| Apache Spark (PySpark) | Distributed Data Processing |
| Spark SQL | SQL Analytics |
| DataFrame API | Data Transformation |
| Window Functions | Ranking & Analytics |
| CSV | Input Dataset |
| Parquet | Optimized Storage |
| Git | Version Control |
| GitHub | Project Repository |

---

# ✨ Features

- Read Large CSV Dataset
- Data Cleaning
- Missing Value Handling
- Feature Engineering
- Fraud Transaction Analysis
- Customer-wise Analysis
- Transaction Analysis
- Spark SQL Queries
- Aggregations
- Joins
- Window Functions
- Partition Optimization
- Parquet Export
- Modular ETL Scripts

---

# 📊 Implemented Modules

## ✅ Read Transactions

- Load CSV into Spark DataFrame
- Infer Schema
- Display Dataset

---

## ✅ Data Cleaning

- Remove Null Values
- Remove Duplicates
- Data Validation

---

## ✅ Feature Engineering

- Create Derived Columns
- Generate Business Metrics

---

## ✅ Fraud Analysis

- Detect Fraud Transactions
- Fraud Statistics

---

## ✅ Transaction Analysis

- Transaction Type Analysis
- Amount Distribution

---

## ✅ Customer Analysis

- Customer Transaction Summary
- High-value Customers

---

## ✅ Partitioning

- Repartition
- Coalesce

---

## ✅ Window Functions

- ROW_NUMBER()
- RANK()
- DENSE_RANK()

---

## ✅ Joins

- Inner Join
- Join Analysis

---

## ✅ Spark SQL

- SQL Queries on Spark DataFrames
- Group By
- Aggregations

---

## ✅ Aggregations

- COUNT
- SUM
- AVG
- MAX
- MIN

---

# 🚀 Setup Instructions

## 1 Clone Repository

```bash
git clone https://github.com/Poojitha363/Bank_Transaction_ETL_Pipeline.git
```

---

## 2 Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

---

## 3 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4 Install Java

Java 17 or above should be installed.

Verify

```bash
java -version
```

---

## 5 Install PySpark

```bash
pip install pyspark
```

---

## 6 Run Scripts

Example

```bash
python scripts/01_read_transactions.py
```

Similarly run all scripts sequentially.

---

# 📸 Project Screenshots

## Read Transactions

![Read Transactions](c:\Users\venka\OneDrive\Documents\Pictures\Screenshots\read and schema.png)

---

## Fraud Analysis

![Fraud Analysis](c:\Users\venka\OneDrive\Documents\Pictures\Screenshots\fraud transactions.png)

---

## Transaction Analysis

![Transaction Analysis](c:\Users\venka\OneDrive\Documents\Pictures\Screenshots\transaction analysis.png)

---

## Customer Analysis

![Customer Analysis](c:\Users\venka\OneDrive\Documents\Pictures\Screenshots\customer analysis.png)

---

## Window Functions

![Window Functions](c:\Users\venka\OneDrive\Documents\Pictures\Screenshots\window funtions.png)

---

## Joins

![Joins](c:\Users\venka\OneDrive\Documents\Pictures\Screenshots\jon operations.png)

---

## Spark SQL

![Spark SQL](c:\Users\venka\OneDrive\Documents\Pictures\Screenshots\spark analysis.png)

---

## Aggregations

![Aggregations](c:\Users\venka\OneDrive\Documents\Pictures\Screenshots\aggregations.png)

---

# 📈 Future Improvements

- Apache Hadoop Integration
- Hive Support
- Apache Airflow Orchestration
- Kafka Streaming
- Delta Lake
- AWS EMR Deployment
- Azure Databricks
- Docker Support

---

# 🎯 Learning Outcomes

This project demonstrates practical experience in:

- PySpark
- ETL Pipeline Development
- Distributed Data Processing
- Spark SQL
- Data Cleaning
- Feature Engineering
- Window Functions
- Joins
- Aggregations
- Partition Optimization
- Big Data Concepts

---

# 👩‍💻 Author

**Pooja**

B.Tech CSE | Aspiring Data Engineer

---

# ⭐ If you like this project

Please consider giving it a ⭐ on GitHub.

