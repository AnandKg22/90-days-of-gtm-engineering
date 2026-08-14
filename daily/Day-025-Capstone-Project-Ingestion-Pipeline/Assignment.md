# Capstone Project Assignment - Day 025: GTM Data Ingestion Pipeline

This Capstone Project requires developing a complete Python Data Ingestion Pipeline Orchestrator. It acts as the central hub of our B2B SaaS GTM stack, coordinating webhook ingestion, signature validation, schema parsing, ETL table loading, error logging, and Dead Letter Queue (DLQ) routing.

---

## 🎯 Requirements

Your Capstone Python orchestrator must:
1.  Initialize an in-memory SQLite database containing:
    *   `dim_companies` (Dimension table: `company_key`, `name`, `industry`, `tier`).
    *   `fact_deals` (Fact table: `deal_id`, `company_key`, `amount_usd`, `seats`).
    *   `dead_letter_queue` (Error table: `failed_at`, `source`, `error`, `payload`).
2.  Implement a **Webhook Ingestion Handler**:
    *   Expose a webhook receiver method that checks a pre-shared security header token (`X-Ingest-Token`). If invalid, reject with status `401 Unauthorized`.
3.  Implement **Schema Validation & Transformation (ETL)**:
    *   Verify incoming event structures against expected property types.
    *   Split/normalize names and compute size tiers (SME vs Enterprise) based on employee count.
    *   Upsert company profiles into `dim_companies`.
    *   Write transaction values to `fact_deals`.
4.  Implement **Fault Tolerance & Recovery**:
    *   If a request encounters a simulated temporary rate-limit (429), execute a backoff wait and retry.
    *   If a request encounters a validation error (400) or fails all retries, write the record to `dead_letter_queue` and trigger warning alerts.
5.  Execute an end-to-end simulation:
    *   **Event 1 (Success)**: New company signup.
    *   **Event 2 (Success)**: Stripe payment checkout deal ($12,000, 300 seats).
    *   **Event 3 (Rate Limited)**: Deal upsert that fails once (HTTP 429) then succeeds on retry.
    *   **Event 4 (Critical Failure)**: Malformed JSON body that is rejected immediately (HTTP 400) and written to the DLQ table.
6.  Run query reports joining the fact and dimension tables to print final sales statistics.

---

## 💻 Deliverable Code

A complete, working Capstone Ingestion Pipeline has been created and placed in [Code/ingestion_pipeline.py](Code/ingestion_pipeline.py). It models the full GTM stack integration flows, error audits, and SQL reports.
