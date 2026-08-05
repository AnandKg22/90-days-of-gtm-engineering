# Project Assignment - Day 020: BigQuery Query & Cost Optimizer

This project requires developing a Python simulation of Google BigQuery's nested SQL query engine. It processes nested and repeated JSON records, flattens array fields, and audits query queries for date-partition optimization to prevent expensive scans.

---

## 🎯 Requirements

Your Python simulation must:
1.  Define a dataset of nested records (representing BigQuery's `RECORD` and `REPEATED` schemas) containing:
    *   `email`, `company_name`, `created_date`.
    *   `touchpoints` (array of structs containing: `source`, `medium`, `url`).
2.  Implement a query method that:
    *   Flattens the repeated arrays (simulating SQL `UNNEST`).
    *   Filters records based on nested parameters (e.g., matching a URL).
    *   Aggregates metrics (e.g. counting total page views grouped by URL).
3.  Implement a **Cost Optimizer Auditing Check**:
    *   Analyze the query filters.
    *   If the query does not filter by the partitioned `created_date` key, output a warning alert indicating a **Full Table Scan cost penalty** (simulating Slot overhead).
    *   If the date filter is present, output a **Partition Pruning confirmation** (confirming 99% cost reduction).

---

## 💻 Deliverable Code

A complete, working simulator script has been created and placed in [Code/bigquery_simulator.py](Code/bigquery_simulator.py). It models the dataset, implements the `UNNEST` transformations, runs the partition checks, and outputs the reports.
