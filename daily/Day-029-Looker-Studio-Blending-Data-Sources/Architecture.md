# GTM Architecture - Day 029: Looker Data Blending & SQL Joins

This document details the GTM architecture comparing browser-side Data Blending against pre-joined database SQL views.

---

## 🔄 Client-Side Data Blending vs. Warehouse SQL Joins

The diagram below details the processing workloads, showing why joining datasets inside the cloud warehouse prevents browser rendering lockups:

```mermaid
graph TD
    subgraph Client-Side Data Blending (Browser Overhead)
        HubSpot[(HubSpot Connector)] -->|1. Fetch Contacts| Browser[Looker Browser JS Engine]
        Stripe[(Stripe Connector)] -->|2. Fetch Payments| Browser
        Browser -->|3. Run Javascript Left Join| Blend[Blended Data Source]
        Blend -->|4. Display Chart| Widget[Widget Grid]
    end
    
    subgraph Warehouse Pre-Joined View (Optimized)
        SQL_Join[SQL Left Join View] -->|1. SELECT * FROM v_leads_billing| BQ[(GCP BigQuery)]
        BQ -->|2. Load Pre-joined rows| Clean_Connector[Looker Data Source]
        Clean_Connector -->|3. Display Chart Instantly| Widget_Optimized[Widget Grid]
    end
```

---

## ⚙️ SQL Join Query Mapping

To optimize GTM dashboards, avoid Looker Blending. Deploy this SQL Left Outer Join view in the warehouse database:

```sql
CREATE VIEW v_leads_payments_funnel AS
SELECT 
    l.email AS lead_email,
    l.utm_source,
    l.employees,
    p.amount_usd,
    p.plan_tier,
    CASE 
        WHEN p.amount_usd IS NOT NULL THEN 1 
        ELSE 0 
    END AS is_converted
FROM `vivaexams-production.vivaexams_gtm.dim_leads` l
LEFT OUTER JOIN `vivaexams-production.vivaexams_gtm.fact_payments` p 
  ON l.email = p.customer_email;
```
