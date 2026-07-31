# Project Assignment - Day 017: Reverse ETL Sync Engine

This project requires developing a Python Reverse ETL orchestrator script that queries warehouse analytical views, parses property mappings, performs incremental sync filtering, and updates simulated CRM endpoints.

---

## 🎯 Requirements

Your Python sync engine must:
1.  Define a mock warehouse database table of computed metrics containing:
    *   `domain`, `exams_completed`, `avg_score`, `health_status`, `updated_at`.
2.  Implement an **Incremental Sync** filter:
    *   Compare the record's `updated_at` against a stored `last_sync_timestamp`.
    *   Only sync records that have been modified since the last sync.
3.  Load a schema mapping dictionary that translates source fields to CRM API tags:
    *   `exams_completed` ──> `cadet_exams_completed`
    *   `avg_score` ──> `exam_pass_rate_percent`
    *   `health_status` ──> `customer_health_status`
4.  Execute a batch post request updating a mock HubSpot API, printing payloads and returning status responses.

---

## 💻 Deliverable Code

A complete, working sync engine script has been created and placed in [Code/reverse_etl.py](Code/reverse_etl.py). It models the source warehouse, runs the mapping and incremental filters, and outputs the sync log trace.
