# Exercises - Day 021: dbt Project Schema Design

This document details the file directory layout and modular SQL structures designed for our GTM analytics transformations using dbt.

---

## 📂 dbt Project Directory Architecture

```
vivaexams_dbt/
├── dbt_project.yml           # Core dbt project settings & materializations
├── models/
│   ├── staging/
│   │   ├── sources.yml       # Raw warehouse source references
│   │   ├── stg_leads.sql     # Cleans raw campaign lead logs
│   │   └── stg_deals.sql     # Cleans raw deal logs
│   └── marts/
│       ├── schema.yml        # Tests and column definitions
│       └── fct_deals.sql     # Business-ready sales fact table
```

---

## 📝 dbt SQL Model Definitions

### 1. Staging: Leads (`models/staging/stg_leads.sql`)
Cleans and standardizes raw lead tables:
```sql
SELECT 
    id AS lead_id,
    LOWER(email) AS email,
    COALESCE(utm_source, 'direct') AS utm_source,
    COALESCE(utm_medium, 'none') AS utm_medium,
    created_at AS lead_created_at
FROM {{ source('raw_crm', 'leads') }}
```

### 2. Staging: Deals (`models/staging/stg_deals.sql`)
Casts amounts and default values:
```sql
SELECT 
    id AS deal_id,
    lead_id,
    name AS deal_name,
    CAST(amount AS NUMERIC) AS amount_usd,
    stage AS deal_stage
FROM {{ source('raw_crm', 'deals') }}
```

### 3. Marts: Won Deals Fact (`models/marts/fct_deals.sql`)
Joins the staging models to construct the analytics fact sheet:
```sql
WITH deals AS (
    SELECT * FROM {{ ref('stg_deals') }}
),
leads AS (
    SELECT * FROM {{ ref('stg_leads') }}
)

SELECT 
    d.deal_id,
    d.deal_name,
    d.amount_usd,
    l.utm_source,
    l.utm_medium,
    d.deal_stage
FROM deals d
JOIN leads l ON d.lead_id = l.lead_id
WHERE d.deal_stage = 'Won'
```
