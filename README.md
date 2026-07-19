# Python ETL Pipeline

A Python-based ETL (Extract, Transform, Load) pipeline that reads raw customer data, performs data cleaning and transformation using Pandas, logs every step of the process, and produces clean, analysis-ready data.

---

## Project Overview

This project demonstrates a real-world ETL workflow commonly used by Data Engineers.

The pipeline:

- Extracts customer data from a CSV file
- Cleans inconsistent and missing data
- Standardizes formats
- Creates new business columns
- Logs each execution step
- Produces a clean dataset for analytics

---

## Tech Stack

- Python
- Pandas
- NumPy
- Logging
- CSV Files

---

## Project Structure

```
Python-ETL-Project/
│
├── etl.py
├── customer_data_raw.csv
├── customer_data_clean.csv
├── etl.log
├── README.md
└── requirements.txt
```

---

## ETL Workflow

### Extract

- Read customer data from CSV

### Transform

The pipeline performs the following transformations:

- Remove duplicate records
- Trim leading and trailing spaces
- Convert email addresses to lowercase
- Clean phone numbers
- Standardize gender values
- Convert date columns to datetime format
- Convert salary to numeric
- Handle missing values
- Create Full Name column
- Create Join Month column
- Create Salary Band
- Calculate customer Age

### Load

- Save cleaned data to a new CSV file

---

## Features

- Modular ETL functions
- Reusable code
- Detailed logging
- Easy to extend
- Beginner-friendly project structure
- Suitable for Data Engineering practice

---

## Logging

The project records every major ETL step.

Example:

```
INFO - ETL Pipeline Started
INFO - CSV file loaded successfully
INFO - Removed duplicate records
INFO - Standardized email addresses
INFO - Created Full Name column
INFO - ETL Pipeline Completed Successfully
```

---

## Sample Dataset

The input dataset contains customer information such as:

- First Name
- Last Name
- Email
- Phone Number
- Gender
- Date of Birth
- Join Date
- Salary
- Department
- City
- State

---

## How to Run

Clone the repository

```bash
git clone https://github.com/Saisant/Python-ETL-Project.git
```

Move into the project folder

```bash
cd Python-ETL-Project
```

Install dependencies

```bash
pip install pandas numpy
```

Run the ETL pipeline

```bash
python etl.py
```

---

## Learning Objectives

This project helped me practice:

- Python programming
- Pandas data cleaning
- Modular function design
- Logging
- Data transformation
- ETL pipeline development
- Git & GitHub

---

## Future Improvements

- Read data from SQL databases
- Write output to Parquet
- Add configuration using YAML
- Build an Airflow DAG
- Containerize using Docker
- Deploy on AWS

---

## Author

**Sunny**

Aspiring Data Engineer | Python | SQL | Pandas | ETL | GitHub
