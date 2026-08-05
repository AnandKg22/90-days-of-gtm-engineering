# Day 020: Data Warehousing (BigQuery)

## Objective
Understand Google BigQuery serverless cloud data warehousing, configure table partitioning and clustering, design JSON schemas with nested and repeated fields (RECORD/STRUCT), and write optimized SQL queries utilizing the `UNNEST` operator.

## Topics Covered
- Google BigQuery datasets & tables
- JSON schemas with nested records
- SQL array queries (UNNEST operator)
- Slot and query cost optimization

## Subtopics (Developed in Notes)
- Database Design (Partitioning & Clustering)
- SQL Syntax (Nested & Repeated Fields)
- Query Optimization & Slot Management

---

## 🛠️ Practical Exercise: BigQuery Schema Configurations

In this exercise, we designed an optimized BigQuery table schema containing nested fields:
*   **JSON Schema Definition**: Declares root fields (`email`, `company_name`) and a repeated RECORD field (`touchpoints`) storing arrays of clickstream structs (source, medium, url, timestamp).
*   **Nested SQL Query**: Wrote SQL commands using the `UNNEST` operator to flatten repeated fields, aggregating page views and filtering campaign acquisitions.

*View complete schema JSON templates and SQL statements in [Exercises.md](Exercises.md).*

---

## 🏫 Daily Project / Assignment: BigQuery Query & Cost Optimizer

We built an executable Python BigQuery query simulator in [Code/bigquery_simulator.py](Code/bigquery_simulator.py):
*   Models nested and repeated customer record datasets.
*   Simulates SQL `UNNEST` array flattening, filtering on nested variables.
*   Implements an **Auditing Cost Optimizer** that logs performance warnings (Full Table Scan penalties) when queries fail to filter by the table's date partition key, and logs confirmation messages when partition pruning is active.

*View project requirements in [Assignment.md](Assignment.md) and the pipeline diagram in [Architecture.md](Architecture.md).*

---

## 📂 Expected Deliverables
*   📝 [Day 20 Study Notes](Notes.md) — BigQuery slots, array structures, and partitions.
*   📝 [BigQuery Schema Spec](Exercises.md) — JSON schema files and UNNEST queries.
*   📝 [Optimizer Spec](Assignment.md) — Project requirements.
*   📊 [Ingestion Pipeline Diagram](Architecture.md) — Telemetry-to-BigQuery GCP design.
*   💻 [BigQuery Simulator Script](Code/bigquery_simulator.py) — Executable SQL unnesting and cost check program.

---

## 📝 Notes & Reflection
*   **Key Insight**: Enforcing date partition filters on cloud data warehouse queries limits data scanning, protecting companies from massive query billing overruns.
*   **Study Log**: Read notes in [Notes.md](Notes.md).
*   **Daily Log**: Read reflections in [Reflection.md](Reflection.md).
