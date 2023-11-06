## Pyspark [![CI](https://github.com/nogibjj/miniproject_10/actions/workflows/ci.yml/badge.svg)](https://github.com/nogibjj/miniproject_10/actions/workflows/ci.yml)

#### What is Pyspark

PySpark is the Python API for Apache Spark, an open source, distributed computing framework and set of libraries for real-time, large-scale data processing. If you’re already familiar with Python and libraries such as Pandas, then PySpark is a good language to learn to create more scalable analyses and pipelines.

Apache Spark is basically a computational engine that works with huge sets of data by processing them in parallel and batch systems. Spark is written in Scala, and PySpark was released to support the collaboration of Spark and Python. In addition to providing an API for Spark, PySpark helps you interface with Resilient Distributed Datasets (RDDs) by leveraging the Py4j library.

#### Spark Sql

PySpark provides an easy-to-use interface to Spark SQL, allowing users to perform complex data processing tasks with few lines of code. With PySpark, users can create Spark DataFrames, which is similar to Pandas DataFrames and can be queried using Spark SQL.

Spark SQL is a module in Apache Spark that provides a programming interface and SQL query engine for data stored in Spark’s supported data sources. It allows users to query data stored in Spark’s Resilient Distributed Datasets (RDDs), Apache Hive, Parquet, JSON, and JDBC data sources.

PySpark dataframe needs to be registered before they can be queried with Spark SQL.

#### Dataset

This is a dataset on diabetes with these columns; 

- Pregnancies
- Glucose
- Blood Pressure
- SkinThickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age
- Outcome

#### SQL Query

This subsets the data where the `Outcome` = `0`
<img width="1080" alt="Screenshot 2023-11-06 at 2 25 01 PM" src="https://github.com/nogibjj/miniproject_10/assets/125210401/d24f8241-3b0f-4723-aef6-2723ad30fb14">

#### Summary Statistics 

This is a sumary statistics of the data which can also be found in the `Pyspark_output.md`

<img width="1049" alt="Screenshot 2023-11-06 at 2 27 23 PM" src="https://github.com/nogibjj/miniproject_10/assets/125210401/320497bd-62eb-44b9-b0c3-f1e38c21b86e">

