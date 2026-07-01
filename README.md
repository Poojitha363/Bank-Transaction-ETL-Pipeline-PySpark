#  Bank Transaction ETL Pipeline using PySpark

##  Project Overview

This project demonstrates an End-to-End ETL Pipeline built using Apache Spark (PySpark) on a real-world banking transaction dataset.

The pipeline reads millions of bank transactions from a CSV dataset, performs data cleaning, feature engineering, fraud analysis, Spark SQL queries, joins, window functions, partitioning, and writes the processed data in Parquet format (Hadoop-compatible environments).

The project follows real-world Data Engineering practices and showcases distributed data processing using Apache Spark.

---

#  Project Architecture

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

#  Project Folder Structure

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

#  Technologies Used

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

#  Features

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

#  Implemented Modules

##  Read Transactions

- Load CSV into Spark DataFrame
- Infer Schema
- Display Dataset

---

##  Data Cleaning

- Remove Null Values
- Remove Duplicates
- Data Validation

---

##  Feature Engineering

- Create Derived Columns
- Generate Business Metrics

---

##  Fraud Analysis

- Detect Fraud Transactions
- Fraud Statistics

---

##  Transaction Analysis

- Transaction Type Analysis
- Amount Distribution

---

##  Customer Analysis

- Customer Transaction Summary
- High-value Customers

---

##  Partitioning

- Repartition
- Coalesce

---

##  Window Functions

- ROW_NUMBER()
- RANK()
- DENSE_RANK()

---

##  Joins

- Inner Join
- Join Analysis

---

##  Spark SQL

- SQL Queries on Spark DataFrames
- Group By
- Aggregations

---

##  Aggregations

- COUNT
- SUM
- AVG
- MAX
- MIN

---

#  Setup Instructions

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

![Read Transactions](<img width="1253" height="826" alt="read and schema" src="https://github.com/user-attachments/assets/885d7fdc-7e29-4114-ae67-9dcd52622dee" />
)

---

## Fraud Analysis

![Fraud Analysis](<img width="687" height="917" alt="fraud transactions" src="https://github.com/user-attachments/assets/78dd5bee-f944-437a-bd12-3779216ca430" />
)

---

## Transaction Analysis

![Transaction Analysis](<img width="482" height="275" alt="transaction analysis" src="https://github.com/user-attachments/assets/018cbf41-0f6a-42c3-8482-9f999cd7459d" />
)

---

## Customer Analysis

![Customer Analysis](<img width="1376" height="817" alt="customer analysis" src="https://github.com/user-attachments/assets/00d76f14-e86a-402e-b3bc-51d4ceccbe95" />
)

---

## Window Functions

![Window Functions](<img width="1347" height="540" alt="window funtions" src="https://github.com/user-attachments/assets/1090954c-80f5-4eea-80f8-6f32120510ad" />
)

---

## Joins

![Joins](<img width="1361" height="921" alt="jon operations" src="https://github.com/user-attachments/assets/b7c6ca93-df3e-4d06-9385-4659935bb044" />
)

---

## Spark SQL

![Spark SQL](<img width="742" height="282" alt="spark analysis" src="https://github.com/user-attachments/assets/132804aa-d76e-46f6-a2be-4bcd5ef039d5" />
)

---

## Aggregations

![Aggregations](<img width="940" height="265" alt="aggregations" src="https://github.com/user-attachments/assets/fe832084-686f-4766-b5ea-0efa9e77ef82" />
)

---

#  Future Improvements

- Apache Hadoop Integration
- Hive Support
- Apache Airflow Orchestration
- Kafka Streaming
- Delta Lake
- AWS EMR Deployment
- Azure Databricks
- Docker Support

---

#  Learning Outcomes

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

#  Author

**Poojitha Indirala**

B.Tech CSE | Aspiring Data Engineer

---

# ⭐ If you like this project

Please consider giving it a ⭐ on GitHub.

