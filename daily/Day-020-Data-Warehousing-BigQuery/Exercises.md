# Exercises - Day 020: BigQuery Schema Design

This document details the BigQuery schema configuration and analytical SQL queries designed to utilize nested and repeated fields.

---

## 📂 BigQuery Table Schema JSON Definition

To store B2B leads and their activity history, we design a single denormalized BigQuery table with a `RECORD` (Struct) field of type `REPEATED` (Array):

```json
[
  {
    "name": "email",
    "type": "STRING",
    "mode": "REQUIRED",
    "description": "Unique email address of the lead"
  },
  {
    "name": "company_name",
    "type": "STRING",
    "mode": "NULLABLE"
  },
  {
    "name": "touchpoints",
    "type": "RECORD",
    "mode": "REPEATED",
    "description": "Array of nested clickstream events",
    "fields": [
      {
        "name": "source",
        "type": "STRING",
        "mode": "REQUIRED"
      },
      {
        "name": "medium",
        "type": "STRING",
        "mode": "REQUIRED"
      },
      {
        "name": "url",
        "type": "STRING",
        "mode": "REQUIRED"
      },
      {
        "name": "timestamp",
        "type": "TIMESTAMP",
        "mode": "REQUIRED"
      }
    ]
  }
]
```

---

## 🔍 BigQuery SQL Query Examples

### 1. Count page views grouped by URL (using `UNNEST`)
This flattens the repeated `touchpoints` array into temporary rows to run aggregates:
```sql
SELECT 
    tp.url,
    COUNT(1) AS total_views
FROM `vivaexams_gtm.leads`,
UNNEST(touchpoints) AS tp
GROUP BY tp.url
ORDER BY total_views DESC;
```

### 2. Find leads acquired via Google PPC who visited pricing
Filters on both root columns and nested record parameters:
```sql
SELECT 
    email,
    company_name,
    tp.url,
    tp.source
FROM `vivaexams_gtm.leads`,
UNNEST(touchpoints) AS tp
WHERE tp.source = 'google' 
  AND tp.medium = 'cpc'
  AND tp.url = '/pricing';
```
