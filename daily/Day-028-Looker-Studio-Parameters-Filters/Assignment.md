# Project Assignment - Day 028: Parameterized SQL Query Engine

This project requires developing a Python Looker Studio Parameterized SQL Query Engine. It parses custom input parameters (min deal values and date ranges) and demonstrates how database-level parameter bindings prune data scans and reduce query costs compared to browser-side filters.

---

## 🎯 Requirements

Your Python application must:
1.  Define a database table containing:
    *   `deal_id`, `company_name`, `amount_usd`, `close_date`.
2.  Implement a **Parameterized Query Executor**:
    *   Accept parameters: `min_amount`, `start_date`, `end_date`.
    *   Compile the parameters into a SQL query `WHERE` filter clause.
3.  Implement a **Cost & Scan Auditor**:
    *   Compare two execution paths:
        *   **Client-Side Filtering (Unoptimized)**: Fetches all rows from the database, then filters them in the application layer. Computes 100% database scan volume.
        *   **Server-Side Parameterized Filtering (Optimized)**: Applies filters at the database engine query layer. Computes only the subset of scanned rows.
4.  Log the query outputs and cost saving aggregates to the console.

---

## 💻 Deliverable Code

A complete, working parameterized query engine script has been created and placed in [Code/parameterized_query.py](Code/parameterized_query.py). It models the table, executes queries using parameters, and prints performance audits.
