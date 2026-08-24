# GTM Architecture - Day 030: Cohort Retention Pipelines

This document details the GTM database pipeline mapping raw event tables to cohort grids.

---

## 🔄 Cohort Analysis ETL Processing Flow

The diagram below details the data transformation sequence, showing how first-action dates are extracted, deltas calculated, and pivoted:

```mermaid
graph TD
    Logs[(Raw Activity Logs Table)] -->|1. SELECT user_id, MIN(event_date)| Cohort_Start[Cohort Acquisition Date view]
    
    Cohort_Start -->|2. Join with raw logs| Join[Joined Log Table]
    
    Join -->|3. Calculate day difference| Days[Elapsed Day Delta]
    
    Days -->|4. Divide by 7| Weeks[Weekly Interval Buckets: W0, W1, W2, W3]
    
    Weeks -->|5. Pivot & COUNT(DISTINCT user_id)| Grid[Cohort Weekly Retention Grid]
```

---

## ⚙️ SQL Cohort Pivot Schema

To compile cohort grids in Looker Studio, the warehouse runs an aggregate pivot query joining first event CTEs with activity records:

```sql
WITH user_signup AS (
    SELECT user_id, MIN(event_date) AS signup_date
    FROM activity_logs
    GROUP BY 1
),
user_deltas AS (
    SELECT 
        s.signup_date,
        a.user_id,
        (a.event_date - s.signup_date) / 7 AS week_index
    FROM activity_logs a
    JOIN user_signup s ON a.user_id = s.user_id
)

SELECT 
    DATE_TRUNC(signup_date, WEEK) AS cohort_week,
    COUNT(DISTINCT user_id) AS cohort_size,
    COUNT(DISTINCT CASE WHEN week_index = 0 THEN user_id END) AS week_0,
    COUNT(DISTINCT CASE WHEN week_index = 1 THEN user_id END) AS week_1,
    COUNT(DISTINCT CASE WHEN week_index = 2 THEN user_id END) AS week_2,
    COUNT(DISTINCT CASE WHEN week_index = 3 THEN user_id END) AS week_3
FROM user_deltas
GROUP BY 1
ORDER BY cohort_week ASC;
```
