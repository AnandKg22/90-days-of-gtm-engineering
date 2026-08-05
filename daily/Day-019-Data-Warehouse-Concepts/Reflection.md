# Reflection - Day 019: Data Warehouse Concepts

A personal log reflecting on the learning outcomes and concepts mastered on Day 19.

---

## 💡 Key Takeaways & Lessons Learned

1.  **Dimensional Modeling speeds up Analytics**: By separating transaction counts (`fact_deals`) from descriptive variables (`dim_companies`, `dim_dates`), we construct a clean Star Schema. This structure cuts query execution times by avoiding long, recursive SQL queries.
2.  **Staging Tables isolate raw API bugs**: Loading raw webhook payloads directly into staging tables (`stg_`) before run transformations protects our core production fact and dimension tables from corrupted API inputs.
3.  **Partitioning cuts BigQuery costs**: Cloud data warehouses charge based on the volume of data scanned. Partitioning fact tables by transaction date ensures queries only scan matching date partitions, preventing expensive bills on large datasets.

---

## 💻 Script Verification

I ran the `Code/warehouse_db.py` script to test the ETL pipeline and Star Schema queries.
*   **Result**: 
    *   *Staging Ingest*: Successfully loads raw companies and deals.
    *   *ETL execution*: Transforms employee counts to tiers and parses date keys correctly, populating the dimensions and fact tables.
    *   *Sales Digest Report*: Successfully joins the three tables, grouping closed revenue and seats by quarter and size tier (e.g. Mid-Market Q1 closed $10,000.00 and sold 500 licenses).
*   **Insight**: This verifies that our dimensional design compiles accurate, consolidated business intelligence reports.

---

## 🎯 Plan for Tomorrow
Tomorrow is Day 20: **Data Warehousing (BigQuery)**. I will focus on deploying analytics tables inside Google BigQuery, configuring BigQuery schemas, loading external datasets, and executing SQL aggregates.
