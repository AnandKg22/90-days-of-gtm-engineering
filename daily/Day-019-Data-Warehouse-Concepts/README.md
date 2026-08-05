# Day 019: Data Warehouse Concepts

## Objective
Understand Cloud Data Warehouse architectures (BigQuery/Snowflake), design normalized dimensional Star Schemas (separating Fact and Dimension tables), and build ETL pipelines that transform raw staging records into consolidated sales performance databases.

## Topics Covered
- Cloud Data Warehouses
- Star vs. Snowflake Schemas
- Staging, Fact, and Dimension tables
- Columnar database architectures

## Subtopics (Developed in Notes)
- Database Design (Dimensional Star Schema)
- SQL Syntax (Analytical Aggregations)
- Query Optimization (Partitioning & Clustering)

---

## 🛠️ Practical Exercise: Star Schema Design

In this exercise, we designed a GTM Star Schema optimized for high-volume analytics queries:
*   **Fact Table (`fact_deals`)**: Stores numeric deal amounts and seat license counts, linked via foreign keys to dimension tables.
*   **Company Dimension (`dim_companies`)**: Stores firmographic context and segment size tiers (SME, Mid-Market, Enterprise).
*   **Date Dimension (`dim_dates`)**: Stores calendar date details (year, quarter, month names) and date key indexes.

*View complete DDL statements and analytical queries in [Exercises.md](Exercises.md).*

---

## 🏫 Daily Project / Assignment: GTM Data Warehouse ETL

We built an executable Python/SQLite ETL pipeline script in [Code/warehouse_db.py](Code/warehouse_db.py):
*   Exposes raw staging tables (`stg_companies`, `stg_deals`) to capture uncleaned billing events.
*   Executes SQL `INSERT INTO ... SELECT` ETL pipelines to transform raw strings and load them into normalized Fact and Dimension tables.
*   Executes joint analytical queries producing Sales Performance reports directly to the console.

*View project requirements in [Assignment.md](Assignment.md) and the entity relationship diagram in [Architecture.md](Architecture.md).*

---

## 📂 Expected Deliverables
*   📝 [Day 19 Study Notes](Notes.md) — Dimensional modeling, facts, and partitioning.
*   📝 [Star Schema Spec](Exercises.md) — Table DDLs and quarter-over-quarter queries.
*   📝 [ETL Pipeline Spec](Assignment.md) — Project requirements.
*   📊 [Star Schema Diagram](Architecture.md) — Entity relationship diagram.
*   💻 [Warehouse ETL Script](Code/warehouse_db.py) — Executable staging-to-fact ETL engine.

---

## 📝 Notes & Reflection
*   **Key Insight**: Utilizing date partitioning on fact tables ensures queries only scan matching date partitions, preventing expensive query fees in cloud warehouses.
*   **Study Log**: Read notes in [Notes.md](Notes.md).
*   **Daily Log**: Read reflections in [Reflection.md](Reflection.md).
