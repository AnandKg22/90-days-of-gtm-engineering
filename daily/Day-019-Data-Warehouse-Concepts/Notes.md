# Study Notes - Day 019: Data Warehouse Concepts

Today's studies focused on cloud data warehousing (BigQuery/Snowflake), Star vs. Snowflake dimensional schemas, staging tables, Fact vs. Dimension tables, and query optimizations.

---

## 1. Cloud Data Warehousing in GTM

A data warehouse (like Google BigQuery or Snowflake) is an analytical database optimized for running queries across millions or billions of rows of historical data. Unlike transactional databases (which write single records quickly), data warehouses use columnar storage to aggregate numbers (like summing revenue) in seconds.

---

## 2. Deep-Dive: Data Warehouse Subtopics

To model enterprise analytics databases, a GTM Engineer must master these three warehousing subtopics:

### 1. Database Design (Dimensional Star Schema)
*   **Definition**: Organizing tables into a central **Fact table** surrounded by multiple **Dimension tables**:
    *   **Fact Tables**: Store quantitative measurements or business transactions (e.g. `fact_sales` containing transaction amounts, quantities, and dates). Rows are typically narrow and contain foreign key links to dimensions.
    *   **Dimension Tables**: Store qualitative, descriptive context about the business entities (e.g. `dim_companies` storing name, size, and location; `dim_dates` storing year, quarter, and month).
    *   **Staging Tables**: Temporary tables (`stg_`) where raw API JSON payloads are loaded before cleaning and inserting into fact/dimension tables.
*   **GTM Application**: Star schemas simplify writing SQL queries and speed up execution by avoiding complex, recursive joins.

### 2. SQL Syntax (Analytical Aggregations)
*   **Definition**: Writing multi-table JOIN queries that aggregate facts along specific dimension constraints.
*   **GTM Application**: You write queries to calculate business metrics:
    *   *Example*: Calculate total MRR (`fact_sales`) grouped by company size tier (`dim_companies`) and transaction calendar quarter (`dim_dates`).

### 3. Query Optimization (Partitioning & Clustering)
*   **Definition**: Optimizing cloud data warehouse costs and query performance:
    *   **Partitioning**: Dividing a large table into smaller segments based on a date column (e.g., partitioning `fact_sales` by day). When a query filters by a date range, BigQuery only reads the matching partitions, cutting processed data costs by 99%.
    *   **Clustering**: Sorting table rows based on columns frequently filtered or joined (e.g., clustering by `company_id`). This groups matching data together on disk, speeding up searches.
