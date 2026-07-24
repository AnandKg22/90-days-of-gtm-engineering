# Project Assignment - Day 013: GTM Relational Analytics DB

This project requires developing a Python/SQLite database simulator that creates PostgreSQL-compatible schemas, seeds GTM leads and deals, runs funnel calculations, and audits query optimization using execution plan analysis.

---

## 🎯 Requirements

Your Python/SQLite application must:
1.  Construct an in-memory database replica.
2.  Execute DDL SQL statements to build:
    *   `leads` table (UTM campaign columns and unique email constraint).
    *   `deals` table (linked to leads with cascade deletion).
    *   Indices on `leads(utm_source)` and `deals(lead_id)`.
3.  Seed mock records representing various marketing channels (Google ads, newsletter emails, organic SEO) and associated deals.
4.  Execute SQL queries to report:
    *   **Revenue by Source**: Closed won deal values grouped by `utm_source`.
    *   **Funnel Conversion Rate %**: Total leads divided by won deals.
5.  Execute an `EXPLAIN QUERY PLAN` command on a join lookup to verify that SQLite utilizes the indexes (Index Scan) rather than doing a full database scan (Table Scan).

---

## 💻 Deliverable Code

A complete, working database script has been created and placed in [Code/postgres_gtm.py](Code/postgres_gtm.py). It builds the database, executes queries, and prints the performance analysis report.
