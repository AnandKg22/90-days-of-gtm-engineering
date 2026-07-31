# Study Notes - Day 017: Reverse ETL (Warehouse to CRM Sync)

Today's studies focused on Reverse ETL concepts (Census/Hightouch), database source views, destination mapping schemas, API rate limit pooling, and incremental sync methods.

---

## 1. What is Reverse ETL?

Standard ETL (Extract, Transform, Load) aggregates data from sales tools *into* a central data warehouse for analytics. **Reverse ETL** does the opposite: it syncs computed analytics scores (such as customer health scores, trial usage data, or aggregate seats) from the data warehouse *back* into the daily business tools (CRMs like HubSpot/Salesforce, support desks like Zendesk, or email tools).

```
[ CRM / Billing Tools ] ──────(ETL / Stitch)──────> [ PostgreSQL Warehouse ]
                                                           │
                                                   (Compute Analytics)
                                                           ▼
[ CRM Custom Fields ] ◄──(Reverse ETL / Census)── [ Analytical SQL Views ]
```

### Why use Reverse ETL?
*   **Actionable Data**: Sales reps don't look at SQL databases. Pushing a "Customer Churn Risk: HIGH" label directly into their HubSpot screen lets them act instantly.
*   **Unified Truth**: Business logic (like calculating LTV or contract utilization) is defined once in the SQL warehouse, ensuring all SaaS tools use the same calculations.

---

## 2. Deep-Dive: Reverse ETL Subtopics

To implement a Reverse ETL pipeline, a GTM Engineer must master these three subtopics:

### 1. Database Design (Source SQL Views)
*   **Definition**: Writing SQL query views in PostgreSQL that aggregate raw event logs into consolidated company profiles.
*   **GTM Application**: You construct a view summarizing VivaExams activity:
    *   `company_domain`, `total_exams_graded`, `average_score`, `last_activity_date`.
    *   This view serves as the input source for the Reverse ETL engine.

### 2. Destination API Integration (Batch Upsert)
*   **Definition**: Syncing warehouse records to target REST APIs using batch operations and tracking update logs.
*   **GTM Application**: To avoid hitting CRM rate limits, the sync engine groups records and calls batch upsert endpoints:
    *   *Incremental Sync*: The engine tracks a watermark (`last_sync_timestamp`) and only syncs records that changed since the last run, reducing API calls by 90%.

### 3. Sync Schema Configuration (Property Mapping)
*   **Definition**: Designing JSON metadata files that map source SQL columns to target CRM fields.
*   **GTM Application**: Creating mapping files that define key columns and sync properties:
    *   *Key Column*: `company_domain` (Postgres) ──> `domain` (HubSpot).
    *   *Mappings*: `average_score` ──> `exam_pass_rate_percent`.
