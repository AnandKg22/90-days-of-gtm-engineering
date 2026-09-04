# Cheat Sheet - Building GTM Dashboards

This cheat sheet compiles formulas, SQL queries, and BI configurations used to build and optimize executive GTM dashboards.

---

## 1. Core GTM Dashboard Formulas

| Metric | Formula | Looker Studio Calculated Field |
| :--- | :--- | :--- |
| **MRR** | `ARR / 12` | `ARR / 12` |
| **LTV** | `Avg Deal Value * contract_length` | `Avg_Deal_ARR * 3.0` |
| **LTV:CAC** | `LTV / CAC` | `LTV / 8500` |
| **Weighted Forecast** | `Value * Stage Close Probability` | `Value * CASE WHEN Stage = 'Negotiation' THEN 0.8 WHEN Stage = 'Proposal' THEN 0.5 ELSE 0.1 END` |

---

## 2. SQL Scripts for Data Warehouses

### Calculate Pipeline Value and Weighted Forecast (BigQuery)
```sql
SELECT 
    region,
    segment,
    COUNT(deal_id) AS total_deals,
    SUM(CASE WHEN stage = 'Closed Won' THEN value ELSE 0 END) AS booked_arr,
    SUM(CASE WHEN stage NOT IN ('Closed Won', 'Closed Lost') THEN value ELSE 0 END) AS active_pipeline,
    SUM(value * CASE 
        WHEN stage = 'Discovery' THEN 0.10
        WHEN stage = 'Qualification' THEN 0.25
        WHEN stage = 'Proposal' THEN 0.50
        WHEN stage = 'Negotiation' THEN 0.80
        WHEN stage = 'Closed Won' THEN 1.00
        ELSE 0.00
    END) AS weighted_forecast
FROM `vivaexams-production.vivaexams_gtm.fact_deals`
GROUP BY region, segment;
```

### Calculate Funnel Conversion Rates (PostgreSQL)
```sql
WITH stage_counts AS (
    SELECT 
        COUNT(CASE WHEN stage = 'Discovery' THEN 1 END) as discovery_count,
        COUNT(CASE WHEN stage = 'Qualification' THEN 1 END) as qualification_count,
        COUNT(CASE WHEN stage = 'Proposal' THEN 1 END) as proposal_count,
        COUNT(CASE WHEN stage = 'Closed Won' THEN 1 END) as won_count
    FROM fact_deals
)
SELECT 
    discovery_count,
    qualification_count,
    proposal_count,
    won_count,
    ROUND((qualification_count::numeric / NULLIF(discovery_count, 0)) * 100, 2) as discovery_to_qual_pct,
    ROUND((won_count::numeric / NULLIF(qualification_count, 0)) * 100, 2) as qual_to_won_pct
FROM stage_counts;
```

---

## 3. Database Indexing & Clustering Optimization

### Speed up Dashboard Filtering in PostgreSQL
```sql
-- Create index on fields frequently used in dashboard drop-down filters
CREATE INDEX idx_deals_dashboard_filters 
ON fact_deals (region, segment, stage);
```

### Enable BigQuery BI Engine Caching
Execute this in Google Cloud Shell to reserve BI Engine memory capacity for rapid dashboard query speeds:
```bash
gcloud reservation bi-reservations create \
    --project="vivaexams-production" \
    --location="us-central1" \
    --size=2.0GB
```

---

## 4. Looker Studio Custom Calculated Fields

*   **Group Regions into Market Zones**:
    ```text
    CASE 
        WHEN Region IN ('AMER', 'LATAM') THEN 'Americas'
        WHEN Region IN ('EMEA', 'UK') THEN 'Europe & MEA'
        ELSE 'Asia Pacific'
    END
    ```
*   **Deal Health Alert Flag**:
    ```text
    CASE 
        WHEN Stage != 'Closed Won' AND Stage != 'Closed Lost' AND Days_In_Stage > 90 THEN '⚠️ STALLED'
        ELSE '✅ ACTIVE'
    END
    ```
