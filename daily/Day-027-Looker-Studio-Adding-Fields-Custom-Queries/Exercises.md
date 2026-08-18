# Exercises - Day 027: Calculated Fields Formulas

This document details the Calculated Field formulas and Custom SQL wrappers used to transform raw columns inside the Looker Studio dashboard.

---

## 📋 Looker Studio Calculated Fields Matrix

These formulas are declared directly inside the Looker Studio data source field editor:

| Field Name | Return Type | Looker Studio Formula | Description |
| :--- | :--- | :--- | :--- |
| **`Lead Full Name`** | Text | `CONCAT(first_name, " ", last_name)` | Merges split names for clean dashboard listing. |
| **`Acquisition Segment`**| Text | `CASE WHEN employees > 50 THEN "Enterprise" ELSE "SME" END` | Groups leads by employee volume. |
| **`License Quantity`** | Number | `CAST(seats_count AS NUMBER)` | Converts text strings to numeric fields to run sums. |
| **`Domain Link`** | URL | `HYPERLINK(CONCAT("https://", domain), domain)` | Generates a clickable link directly inside tables. |

---

## ⚙️ Custom SQL Connector Wrapper
To optimize rendering speed, we pre-compile these calculated columns in our BigQuery database before exposing them to Looker Studio:

```sql
SELECT 
    id AS lead_id,
    CONCAT(first_name, ' ', last_name) AS lead_full_name,
    LOWER(email) AS clean_email,
    CASE 
        WHEN employees > 50 THEN 'Enterprise'
        ELSE 'SME'
    END AS acquisition_segment,
    SAFE_CAST(seats_count AS INT64) AS license_quantity
FROM `vivaexams-production.vivaexams_gtm.raw_leads`
```
