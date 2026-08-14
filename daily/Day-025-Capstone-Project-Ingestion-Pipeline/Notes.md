# Study Notes - Day 025: Capstone Project (Ingestion Pipeline)

Today's studies focused on integrating the concepts of Phase 2 (Data & Integrations) into a unified, end-to-end Data Ingestion Pipeline. We reviewed secure webhook receivers, data transformations, database loading, error logging, and recovery mechanisms.

---

## 1. End-to-End Data Ingestion Architecture

A production-grade GTM Data Ingestion Pipeline must coordinate multiple systems to ingest, transform, and store data securely:

```
[ Webhook Event / API Source ] 
               │
               ▼
[ Webhook Ingestion Layer ] ────(Signature Validation)────> [ Reject HTTP 401 ]
               │
               ▼
[ Processing Queue (Redis) ]
               │
               ▼
[ Transformation Engine ] ──────(Schema Validation)───────> [ Dead Letter Queue ]
               │
               ▼
[ Load / Database Engine ] ─────(SQL Insert/Upsert)───────> [ Looker BI Analytics ]
```

---

## 2. Deep-Dive: Ingestion Pipeline Subtopics

To construct the Capstone Ingestion pipeline, a GTM Engineer must master these three subtopics:

### 1. Database Design (Target Analytical Schemas)
*   **Definition**: Designing the target warehouse tables (Star Schema) to store ingested telemetry:
    *   **Staging Tables**: Capture raw, uncleaned payloads for history logging.
    *   **Dimension Tables**: Maintain clean customer contexts (`dim_companies`, `dim_dates`).
    *   **Fact Tables**: Track numeric business occurrences (`fact_deals`).
*   **GTM Application**: Schema modeling ensures that when Stripe and HubSpot push data, the relational keys sync perfectly for BI query runs.

### 2. API Integration (Secure Webhook Ingest)
*   **Definition**: Constructing public endpoints that parse inbound HTTP requests, validate HMAC signature headers, and unpack JSON payloads.
*   **GTM Application**: Building webhook handlers that intercept Stripe transactions, calculate hashes using shared secrets to verify sender authenticity, and return instant `200 OK` responses.

### 3. Schema Configuration & Exception Recovery (DLQ & Retries)
*   **Definition**: Enforcing strict payload structural validations and handling transient or permanent failures.
*   **GTM Application**: Setting up ingestion policies:
    *   *Retry loop*: Retrying network connection timeouts (HTTP 503) using exponential backoff.
    *   *Abortion / DLQ*: Immediately rejecting structural errors (HTTP 400), writing the payload to a `dead_letter_queue` database table, and triggering alerts.
