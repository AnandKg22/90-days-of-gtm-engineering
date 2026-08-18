# GTM Architecture - Day 027: Calculated Fields & Custom Queries

This document details the GTM architecture comparing client-side Looker Studio formula execution against serverless warehouse-level custom SQL View pre-aggregation.

---

## 🔄 Client-Side vs. Warehouse-Side Calculations

The diagram below details the processing workloads, showing why offloading CASE/CAST formulas to database views reduces rendering lag:

```mermaid
graph TD
    subgraph Looker Studio Frontend (Slow Client-side Loop)
        Client[Looker Browser App] -->|1. Fetch Raw Columns| DB[(Raw Database Tables)]
        Client -->|2. Run CONCAT, CASE, CAST formulas| Rendering[Calculate row-by-row in Javascript]
        Rendering -->|3. Display Chart| Widget[Dashboard Scorecard Widget]
    end
    
    subgraph Warehouse Pre-aggregation (Fast SQL View)
        DB_V2[(BigQuery Warehouse)] -->|1. Pre-calculate views via SQL DDL| View[Custom SQL / dbt Marts View]
        View -->|2. Fetch pre-compiled columns| Client_Optimized[Looker Browser App]
        Client_Optimized -->|3. Display Chart instantly| Widget_Optimized[Dashboard Scorecard Widget]
    end
```

---

## ⚙️ Custom SQL Syntax mapping

To bypass browser-side processing, calculated fields are pre-compiled using database views:

```sql
CREATE VIEW v2_leads_analytical AS
SELECT 
    id,
    CONCAT(first_name, ' ', last_name) AS full_name,
    LOWER(email) AS clean_email,
    CASE 
        WHEN employees > 50 THEN 'Enterprise'
        ELSE 'SME'
    END AS segment,
    SAFE_CAST(seats_count AS INT64) AS seats
FROM raw_leads;
```
