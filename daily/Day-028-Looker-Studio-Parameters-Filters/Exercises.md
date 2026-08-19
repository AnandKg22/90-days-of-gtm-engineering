# Exercises - Day 028: Dashboard Filters & Parameters

This document details the layout filter controls and custom SQL parameterized queries designed to restrict database scans from the Looker Studio dashboard.

---

## 📋 Interactive Controls & Parameter Matrix

These parameters and filters are mounted on the Looker Studio canvas page to enable user-driven filtering:

| Control Type | UI Display Name | Binding Target | Parameter Name | Default Value |
| :--- | :--- | :--- | :--- | :--- |
| **Dropdown List** | `Industry Selector` | Dimension: `industry` | *N/A (Client-side)* | All Industries |
| **Date Range** | `Analysis Window` | Dimension: `close_date` | `@DS_START_DATE`<br>`@DS_END_DATE` | Last 30 Days |
| **Input Box** | `Min Deal Value ($)` | Custom SQL Variable | `@ds_min_amount` | `5000` |

---

## ⚙️ Parameterized BigQuery SQL Query

This custom query receives input values from the dashboard controls and applies them to BigQuery's partitioned table structure:

```sql
SELECT 
    f.deal_id,
    c.company_name,
    c.industry,
    f.amount_usd,
    f.close_date
FROM `vivaexams-production.vivaexams_gtm.fact_deals` f
JOIN `vivaexams-production.vivaexams_gtm.dim_companies` c ON f.company_key = c.company_key
WHERE f.amount_usd >= @ds_min_amount
  AND f.close_date BETWEEN PARSE_DATE('%Y%m%d', @DS_START_DATE) 
                       AND PARSE_DATE('%Y%m%d', @DS_END_DATE);
```
