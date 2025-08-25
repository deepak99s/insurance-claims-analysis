# Claims Analysis Project

## Overview
This project demonstrates an end-to-end data pipeline for analyzing insurance claims.  
It covers:
1. Extracting, transforming, and loading (ETL) raw customer and policy data into a structured database.
2. Writing SQL queries to answer business questions.
3. Building a Power BI dashboard to visualize insights.

---

## Project Deliverables
The submission contains:
- **claims_etl.py** → Python script to perform ETL from CSV files into MySQL.
- **claims_queries.sql** → SQL queries answering the given business questions.
- **claims_analysis.sql** → MySQL dump of the populated database.
- **Dashboard.pbix** → Power BI dashboard with visualizations.
- **README.md** → Documentation (this file).

---

## Setup Instructions

### 1. Database Setup
- Install **MySQL Server** and **MySQL Workbench**.
- Create a new database (e.g., 'claims_db').
- Run the ETL script to populate tables.

### 2. Running the ETL Script
- Place the CSV files ('customers.csv', 'policies.csv') in the same folder as 'claims_etl.py'.
- Open a terminal/command prompt and run:
  '''bash
  python claims_etl.py

Update the database connection details inside the script:
user="YOUR_USERNAME"
password="YOUR_PASSWORD"
host="localhost"
database="claims_db"

### 3. Using the SQL Queries

Open MySQL Workbench.

Load claims_queries.sql.

Execute the queries to generate the required analysis outputs.


### 4. Restoring the Database from Dump

Import claims_analysis.sql using MySQL Workbench or the MySQL command line:

mysql -u root -p claims_db < claims_analysis.sql


### 5. Power BI Dashboard

Open Dashboard.pbix in Power BI Desktop.

If required, update the data source (MySQL or exported CSVs).

The dashboard includes:

Geographical Performance: Claim payouts by state.

Core Efficiency Metric: Average assessment time.

Claim Funnel: Count of claims by status.

High-Value Customers: Top customers by payouts.

Correlation: Relationship between assessment time and payout discrepancy.

### Assumptions

Missing or invalid numerical values were set to 0 during ETL.

Dates were assumed to be in standard YYYY-MM-DD format.

Customer names and states are assumed to be clean and consistent.

Payout discrepancy is calculated as estimated_payout_amount - final_payout_amount.

### Design Choices

Used MySQL as the relational database for robustness and compatibility with Power BI.

Kept ETL modular (separating data cleaning, transformation, and loading).

Exported a MySQL dump (claims_analysis.sql) for easy reproducibility.

Power BI chosen for visualization due to strong support for interactive dashboards.

