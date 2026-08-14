# GTM Architecture - Day 025: Capstone Ingestion Pipeline

This document details the Capstone Ingestion Pipeline data flow architecture.

---

## 🔄 End-to-End Capstone Ingestion Pipeline

The flowchart below maps out the sequence of webhook ingestion, auth checks, validations, backoff retries, and database writes:

```mermaid
graph TD
    Start[Inbound HTTP POST Webhook] --> TokenCheck{Is Ingest Token Valid?}
    TokenCheck -->|No| AuthError[HTTP 401: Unauthorized]
    
    TokenCheck -->|Yes| Ingest[Read Event Type & Schema]
    Ingest --> SchemaCheck{Passes Schema Validations?}
    
    SchemaCheck -->|No| DLQ[Insert into dead_letter_queue table]
    DLQ --> Slack[Dispatch Slack alert to engineering]
    
    SchemaCheck -->|Yes: deal.closed| RateCheck{Encounter HTTP 429?}
    RateCheck -->|Yes| Backoff[Trigger Backoff delay & Retry]
    Backoff --> SchemaCheck
    
    RateCheck -->|No| DB_Insert[Write to SQLite/Warehouse Database]
    DB_Insert -->|Upsert Company Dimension| DimTable[(dim_companies)]
    DB_Insert -->|Insert Deal Fact| FactTable[(fact_deals)]
```

---

## ⚙️ Capstone SQL Reporting Schema

Our analytics dashboard executes multi-table SQL joins between the ingested company dimension and deal fact tables to compute account sales:

```sql
SELECT 
    c.company_name,
    c.size_tier,
    SUM(f.amount_usd) AS total_sales,
    SUM(f.license_seats) AS total_seats
FROM fact_deals f
JOIN dim_companies c ON f.company_key = c.company_key
GROUP BY c.company_name, c.size_tier
ORDER BY total_sales DESC;
```
