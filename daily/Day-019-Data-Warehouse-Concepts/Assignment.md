# Project Assignment - Day 019: GTM Data Warehouse ETL Pipeline

This project requires developing a Python/SQLite simulation of an enterprise Data Warehouse ETL Pipeline. It loads raw records into staging tables, runs SQL extraction pipelines to populate Fact and Dimension tables, and executes star-schema aggregate queries.

---

## 🎯 Requirements

Your Python/SQLite application must:
1.  Define a database representing the Cloud Data Warehouse.
2.  Run DDL SQL commands to construct:
    *   **Staging Tables**: `stg_companies` and `stg_deals` (raw, denormalized ingest tables).
    *   **Dimension Tables**: `dim_companies` and `dim_dates`.
    *   **Fact Table**: `fact_deals` (containing numeric metrics and dimension foreign keys).
3.  Seed raw, unstructured records in the staging tables representing different maritime client accounts.
4.  Execute an **ETL pipeline** (using SQL `INSERT INTO ... SELECT` statements) to clean and route data from staging tables into the normalized Star Schema tables.
5.  Execute JOIN queries joining the fact and dimension tables to output a Sales Performance Digest showing revenue and seats sold grouped by company tier and calendar year/quarter.

---

## 💻 Deliverable Code

A complete, working ETL pipeline script has been created and placed in [Code/warehouse_db.py](Code/warehouse_db.py). It builds the staging environment, runs the ETL transformations, and outputs the performance reports to the console.
