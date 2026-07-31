# Exercises - Day 017: Reverse ETL Blueprint

This document details the Reverse ETL data mapping configuration designed to sync Postgres analytical records back into the CRM.

---

## 📋 Postgres-to-HubSpot Reverse ETL Blueprint

This matrix maps computed database columns to target custom fields on the HubSpot Company object:

| Step | Source SQL View Column | Target CRM Property API | Data Type | Sync Mode | Behavior |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | `company_domain` (Key) | `domain` (Unique Identifier) | `string` | **UPSERT** | Matches Postgres domain to HubSpot Company record. |
| **2** | `total_exams_completed` | `cadet_exams_completed` | `number` | **UPDATE** | Syncs total cadet mock tests run. |
| **3** | `average_pass_rate` | `exam_pass_rate_percent` | `number` | **UPDATE** | Syncs average test score. |
| **4** | `health_status` | `customer_health_status` | `string` | **UPDATE** | Syncs health categorizations (`Good`, `At Risk`, `Churned`). |
| **5** | `last_activity_date` | `last_app_activity_date` | `date` | **UPDATE** | Syncs the last day a cadet logged in. |

---

## ⚙️ Source PostgreSQL Analytical SQL View
This view aggregates click events in our database and generates the dataset for the sync engine:

```sql
CREATE VIEW company_gtm_metrics AS
SELECT 
    c.domain AS company_domain,
    COUNT(e.id) AS total_exams_completed,
    ROUND(AVG(e.score), 2) AS average_pass_rate,
    CASE 
        WHEN AVG(e.score) >= 75 THEN 'Good'
        WHEN AVG(e.score) >= 50 AND AVG(e.score) < 75 THEN 'At Risk'
        ELSE 'Critical Churn Risk'
    END AS health_status,
    MAX(e.created_at) AS last_activity_date
FROM exam_events e
JOIN companies c ON e.company_id = c.id
GROUP BY c.domain;
```
