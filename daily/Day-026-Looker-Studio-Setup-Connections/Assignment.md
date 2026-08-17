# Project Assignment - Day 026: Looker Studio Connection Auditor

This project requires developing a Python Looker Studio Connection Auditor script. It evaluates data source connector metadata, checks for secure JDBC certificates, audits database query methods (custom SQL vs. raw tables), and computes performance optimization warnings.

---

## 🎯 Requirements

Your Python application must:
1.  Define a dictionary representing Looker Studio Connector configurations containing:
    *   `connector_type` (BigQuery, PostgreSQL, Sheets).
    *   `auth_method` (OAuth2, JDBC-SSL, None).
    *   `query_method` (Table-Selection, Custom-SQL, Sheet-Range).
    *   `scan_volume_gb` (simulated database table size).
2.  Implement a **Security Auditor**:
    *   If a `PostgreSQL` connector does not use SSL certificate keys, trigger a security exception.
3.  Implement a **Performance Auditor**:
    *   Check the `query_method`. If it uses `Table-Selection` on tables larger than 10 GB, output a **Query Latency Warning** (recommending replacing it with a warehouse custom SQL View or dbt Mart).
    *   For `BigQuery` connectors, calculate recommended **BI Engine caching capacity** based on the database `scan_volume_gb`.
4.  Execute mock connection checks and log results to the console.

---

## 💻 Deliverable Code

A complete, working connector auditor script has been created and placed in [Code/looker_connector_auditor.py](Code/looker_connector_auditor.py). It models the connection configurations, runs the security checks, and outputs performance logs.
