# Day 025: Capstone Project (Ingestion Pipeline)

## Objective
Conclude **Phase 2: Data & Integrations** by developing an end-to-end Data Ingestion Pipeline Orchestrator that integrates API token authorization, HMAC signature validation, ETL data transformations, Star Schema database loading, and fault-tolerant retry/DLQ routing.

## Topics Covered
- End-to-End Data Ingestion
- Webhook endpoints & API validation
- Star Schema database designs
- Webhook throttling (HTTP 429 retries)
- Dead Letter Queue (DLQ) operations
- Relational BI aggregate queries

## Subtopics (Developed in Notes)
- Database Design (Target Analytical Schemas)
- API Integration (Secure Webhook Ingest)
- Schema Configuration & Exception Recovery (DLQ & Retries)

---

## 🛠️ Practical Exercise: Data Ingestion Strategy

In this exercise, we designed a comprehensive Data Ingestion Strategy Blueprint for the VivaExams platform:
*   **Segment telemetry**: POST Webhook -> API Token -> Map Domain -> Load to Staging table.
*   **Stripe billing**: POST Webhook -> HMAC Signature -> Extract Revenue -> Load to Fact table.
*   **HubSpot contacts**: GET REST -> Bearer Header -> Map size tiers -> Load to Dimension table.

*View complete ingestion strategy details and DLQ table SQL definitions in [Exercises.md](Exercises.md).*

---

## 🏫 Daily Project / Assignment: Capstone Ingestion Pipeline

We built the final Phase 2 Capstone Ingestion Pipeline in [Code/ingestion_pipeline.py](Code/ingestion_pipeline.py):
*   Exposes a mock webhook receiver requiring security token validations.
*   Implements **ETL transformations** (normalizing emails, parsing domains, and categorizing companies into size segments).
*   Upserts records to dimension (`dim_companies`) and fact (`fact_deals`) tables inside an in-memory SQLite database.
*   Implements **Fault Tolerance** (handles simulated 429 rate limit exceptions using exponential backoff retries, and immediately routes structural/foreign-key exceptions to a `dead_letter_queue` table).
*   Compiles a final Capstone Sales Report joining dimension and fact tables.

*View project requirements in [Assignment.md](Assignment.md) and the pipeline sequence diagram in [Architecture.md](Architecture.md).*

---

## 📂 Expected Deliverables
*   📝 [Day 25 Study Notes](Notes.md) — Ingestion architectures, secure webhook receivers, and exception recovery.
*   📝 [Ingestion Strategy Blueprint](Exercises.md) — Ingestion mapping matrix and database tables.
*   📝 [Capstone Project Spec](Assignment.md) — Capstone requirements and test scenarios.
*   📊 [Pipeline Sequence Flow](Architecture.md) — Visual pipeline flowchart and SQL queries.
*   💻 [Capstone Ingestion Pipeline](Code/ingestion_pipeline.py) — Executable end-to-end integration and reporting engine.

---

## 📝 Notes & Reflection
*   **Key Insight**: Enforcing validations and dead letter queue routing during ingestion isolates bad API payloads, ensuring zero transaction loss while protecting warehouse databases.
*   **Study Log**: Read notes in [Notes.md](Notes.md).
*   **Daily Log**: Read reflections in [Reflection.md](Reflection.md).
