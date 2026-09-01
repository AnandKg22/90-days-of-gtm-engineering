# Exercises - Day 036: Database Validation Rules

This document details the database schema validation rules and duplicate check definitions used to enforce data quality standards.

---

## 📋 Database Schema Validation Constraints

These constraints are configured at the database DDL layer to enforce column standards and block bad inputs:

| Target Column | SQL Data Type | DDL Constraint Syntax | Purpose Description |
| :--- | :--- | :--- | :--- |
| **`deal_id`** | `INT` | `PRIMARY KEY NOT NULL` | Unique identifier; prevents null record keys. |
| **`email`** | `VARCHAR(255)` | `CHECK (email LIKE '%_@_%._%')` | Enforces standard email formats, requiring `@` and `.`. |
| **`amount_usd`** | `NUMERIC(10,2)`| `CHECK (amount_usd >= 0.0)` | Prevents negative pricing values. |
| **`deal_stage`** | `VARCHAR(50)` | `CHECK (deal_stage IN ('Lead', ...))` | Restricts stage inputs to valid pipeline categories. |
| **`close_date`** | `DATE` | `NOT NULL` | Enforces closing date requirements for reporting accuracy. |

---

## ⚙️ SQL Duplicate Detection Logic

To find and merge duplicate records, we partition the dataset by the unique identifier (`email`) and sort by timestamp to keep the most recent update:

```sql
WITH duplicate_ranker AS (
    SELECT 
        lead_id,
        email,
        created_at,
        ROW_NUMBER() OVER (
            PARTITION BY email 
            ORDER BY created_at DESC
        ) AS rank_index
    FROM raw_crm_leads
)

SELECT 
    lead_id,
    email,
    created_at
FROM duplicate_ranker
-- Records with rank_index > 1 are duplicates and should be quarantined/purged
WHERE rank_index > 1; 
```
