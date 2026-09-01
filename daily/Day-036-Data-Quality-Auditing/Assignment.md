# Project Assignment - Day 036: Data Auditing & Quality Cleaner

This project requires developing a Python Data Auditing & Quality Cleaner. It parses a raw, dirty CRM lead dataset, runs formatting and constraint checks, resolves duplicates, handles missing values, writes quarantined rows to a local log file, and prints a data quality scorecard.

---

## 🎯 Requirements

Your Python application must:
1.  Define a dirty CRM dataset containing:
    *   `lead_id`, `email`, `company_name`, `deal_amount`, `timestamp` (format: YYYY-MM-DD).
    *   Include test anomalies: duplicate emails, negative deal values, missing companies (nulls), and malformed emails.
2.  Implement **Schema Validation & Constraint Checks**:
    *   Verify that `email` contains both `@` and `.`.
    *   Verify that `deal_amount >= 0.0`.
    *   Verify that `company_name` is not null or empty.
3.  Implement **Duplicate Resolution**:
    *   Find records with duplicate emails. Retain only the record with the most recent `timestamp`, and flag older ones as duplicates.
4.  Implement **Quarantine Logging**:
    *   Write all rejected records and duplicate records to a quarantine log list, along with their validation error reasons.
    *   Save this quarantined dataset to a local JSON file named `quarantine_log.json`.
5.  Print the Data Quality Scorecard to the console, showing counts for Total Rows, Passed Rows, Quarantined Rows, Duplicate Rows, and error summaries.

---

## 💻 Deliverable Code

A complete, working data auditing script has been created and placed in [Code/data_auditor.py](Code/data_auditor.py). It models the logs, executes the cleaning rules, writes the quarantine file, and prints the scorecard.
