# Day 013: Relational DBs (Postgres)

## Objective
Design and implement a PostgreSQL data warehouse schema for GTM replica datasets, build index optimizations, and execute SQL join queries that aggregate pipeline conversions and campaign revenue.

## Topics Covered
- Relational tables and columns
- Primary and Foreign Key constraints
- SQL queries and aggregations
- Index optimization

## Subtopics (Developed in Notes)
- Database Design (Normalization)
- SQL Syntax (Queries & Joins)
- Query Optimization (Indexes & Execution Plans)

---

## 🛠️ Practical Exercise: PostgreSQL Schema Design

In this exercise, we designed an optimized PostgreSQL database structure to house replicated GTM data:
*   **Leads Table**: Capture contact details and UTM source/medium/campaign parameters.
*   **Deals Table**: Tracks contract values, stages, and foreign keys referencing the leads table.
*   **Performance Indexes**: Created B-Tree index constraints (`idx_leads_utm_source`, `idx_deals_lead_id`) to optimize queries.
*   **SQL Dashboards Queries**: Created query models to compile Closed Won revenue per UTM campaign and funnel conversion rates.

*View DDL scripts and query layouts in [Exercises.md](Exercises.md).*

---

## 🏫 Daily Project / Assignment: GTM Relational Analytics DB

We built an executable Python analytics database in [Code/postgres_gtm.py](Code/postgres_gtm.py):
*   Runs DDL queries creating `leads` and `deals` tables along with search indices.
*   Seeds mock campaign acquisition and sales data.
*   Executes join reports computing campaign MRR and lead-to-won conversion rates.
*   Runs `EXPLAIN QUERY PLAN` commands to audit execution strategies, verifying that B-Tree index scans are utilized.

*View project requirements in [Assignment.md](Assignment.md) and the system diagram in [Architecture.md](Architecture.md).*

---

## 📂 Expected Deliverables
*   📝 [Day 13 Study Notes](Notes.md) — Normalization, SQL syntax, and index designs.
*   📝 [PostgreSQL Schema DDL](Exercises.md) — Table schemas and analytics queries.
*   📝 [Relational DB Spec](Assignment.md) — Project requirements.
*   📊 [Database Index Diagram](Architecture.md) — Data flow and B-Tree index logic.
*   💻 [Postgres Replica Script](Code/postgres_gtm.py) — Executable SQL analytics engine.

---

## 📝 Notes & Reflection
*   **Key Insight**: Enforcing strict referential integrity (foreign keys) and optimizing queries with index scans prevents pipeline reporting failures as leads scale to millions.
*   **Study Log**: Read notes in [Notes.md](Notes.md).
*   **Daily Log**: Read reflections in [Reflection.md](Reflection.md).
