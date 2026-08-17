# Day 026: Looker Studio (Setup & Connections)

## Objective
Initiate **Phase 3: Analytics & Reporting** by understanding Google Looker Studio architectures, configuring native data connectors (GCP BigQuery, PostgreSQL JDBC, and Google Sheets), and optimizing query performance using cache freshness rules and Google BI Engine reservations.

## Topics Covered
- Looker Studio BI platform setup
- BigQuery & PostgreSQL native connectors
- JDBC SSL database authentication
- Cache freshness & Google BI Engine
- Custom SQL query wrapping

## Subtopics (Developed in Notes)
- Dashboard Design (Visual Layouts & Filters)
- SQL Syntax (Custom Connector SQL)
- Query Optimization (Caching & BI Engine)

---

## 🛠️ Practical Exercise: Data Source Connections

In this exercise, we mapped out data source configurations inside the Looker Studio UI:
*   **GCP BigQuery**: Setup credentials using OAuth2, configured Custom SQL targets, and allocated BI Engine caching.
*   **PostgreSQL JDBC**: Configured IP ports, database schemas, and uploaded Server CA and Client certificates to enforce mandatory SSL encryption.
*   **Google Sheets**: Bound sheet ranges, ensuring first-row headers were active.

*View complete connection parameters and custom SQL scripts in [Exercises.md](Exercises.md).*

---

## 🏫 Daily Project / Assignment: Looker Connection Auditor

We built an executable Python Looker Connector Auditor in [Code/looker_connector_auditor.py](Code/looker_connector_auditor.py):
*   Models Looker Studio connection settings across four GTM data sources.
*   Executes **Security Auditing** (flagging unencrypted PostgreSQL JDBC credentials and demanding SSL files).
*   Executes **Performance Auditing** (flagging slow `Table-Selection` queries on large staging tables and advising dbt transformations).
*   Calculates recommended **Google BI Engine RAM reservations** to cache queries and reduce BigQuery scanning bills.

*View project requirements in [Assignment.md](Assignment.md) and the connection routing diagram in [Architecture.md](Architecture.md).*

---

## 📂 Expected Deliverables
*   📝 [Day 26 Study Notes](Notes.md) — Looker dashboard design, custom SQL, and BI Engine.
*   📝 [Connector Setup Guide](Exercises.md) — BigQuery and Postgres credential steps.
*   📝 [Auditor Project Spec](Assignment.md) — Project requirements.
*   📊 [Query Caching Flowchart](Architecture.md) — Looker query routing and cache checks.
*   💻 [Connector Auditor Script](Code/looker_connector_auditor.py) — Executable connection auditing program.

---

## 📝 Notes & Reflection
*   **Key Insight**: Implementing joins at the warehouse level (dbt) instead of using Looker's visual "Data Blending" prevents slow dashboard widget render times.
*   **Study Log**: Read notes in [Notes.md](Notes.md).
*   **Daily Log**: Read reflections in [Reflection.md](Reflection.md).
