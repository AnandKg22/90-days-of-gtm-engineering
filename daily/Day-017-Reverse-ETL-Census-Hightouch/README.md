# Day 017: Reverse ETL (Census/Hightouch)

## Objective
Understand Reverse ETL concepts, construct database views in PostgreSQL that compute aggregate client metrics, and build incremental sync engines that map and push warehouse values back into CRM properties.

## Topics Covered
- Reverse ETL concepts
- Census & Hightouch engines
- Destination schema mappings
- Incremental sync watermarks

## Subtopics (Developed in Notes)
- Database Design (Source SQL Views)
- Destination API Integration (Batch Upsert)
- Sync Schema Configuration (Property Mapping)

---

## 🛠️ Practical Exercise: Reverse ETL Blueprint

In this exercise, we designed a B2B Reverse ETL Sync Blueprint to map database metrics to HubSpot Company properties:
*   **Source View (`company_gtm_metrics`)**: SQL query aggregating total exams completed, pass rates, and churn risk health status.
*   **Target Mappings**:
    *   `company_domain` ──> `domain` (Unique Identifier Key)
    *   `total_exams_completed` ──> `cadet_exams_completed`
    *   `average_pass_rate` ──> `exam_pass_rate_percent`
    *   `health_status` ──> `customer_health_status`

*View full mapping schemas and SQL view scripts in [Exercises.md](Exercises.md).*

---

## 🏫 Daily Project / Assignment: Reverse ETL Sync Engine

We built an executable Python Reverse ETL sync engine in [Code/reverse_etl.py](Code/reverse_etl.py):
*   Queries a mock SQL warehouse table representing maritime academy metrics.
*   Implements **Incremental Sync** (filtering out unmodified records using timestamp watermarks).
*   Translates column names using a JSON mapping dictionary and posts batch company updates to a mock HubSpot REST API.

*View project requirements in [Assignment.md](Assignment.md) and the system diagram in [Architecture.md](Architecture.md).*

---

## 📂 Expected Deliverables
*   📝 [Day 17 Study Notes](Notes.md) — ETL vs Reverse ETL, incremental sync, and schemas.
*   📝 [Reverse ETL Blueprint](Exercises.md) — SQL source view and property mapping spec.
*   📝 [Sync Engine Spec](Assignment.md) — Project requirements.
*   📊 [Sync Engine Diagram](Architecture.md) — Ingestion flow and config JSONs.
*   💻 [Reverse ETL Script](Code/reverse_etl.py) — Executable database-to-CRM sync program.

---

## 📝 Notes & Reflection
*   **Key Insight**: Implementing incremental sync limits (checking for modified records since the last sync time) reduces CRM API usage and avoids rate limiting on large datasets.
*   **Study Log**: Read notes in [Notes.md](Notes.md).
*   **Daily Log**: Read reflections in [Reflection.md](Reflection.md).
