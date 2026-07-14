# SQL for GTM Engineers & Revenue Analytics

Analyzing sales conversion pipelines, calculating customer cohorts, and computing revenue metrics requires high-performance SQL query design.

---

## 1. Common Table Expressions (CTEs)

CTEs organize queries into readable steps. They are essential for processing multi-stage pipelines:

```sql
WITH lead_stages AS (
    SELECT id, email, created_at, stage
    FROM contacts
),
deal_values AS (
    SELECT company_id, SUM(amount) AS total_pipeline
    FROM deals
    WHERE stage != 'Closed Lost'
    GROUP BY company_id
)
SELECT ls.email, dv.total_pipeline
FROM lead_stages ls
JOIN companies c ON ls.company_id = c.id
JOIN deal_values dv ON dv.company_id = c.id;
```

---

## 2. Analytical Window Functions

Window functions perform calculations across related rows without collapsing them into a single result.

### 1. Row Number (Identify First Contact Activity)

```sql
-- Rank activity touchpoints for each contact by date
WITH ranked_activities AS (
    SELECT contact_id, type, activity_date,
           ROW_NUMBER() OVER(PARTITION BY contact_id ORDER BY activity_date ASC) as seq_num
    FROM activities
)
SELECT contact_id, type, activity_date
FROM ranked_activities
WHERE seq_num = 1; -- First touchpoint
```

### 2. Lead & Lag (Calculate Stage Conversion Durations)

```sql
-- Find time elapsed between successive pipeline stage updates
SELECT deal_id, stage, updated_at,
       LAG(updated_at) OVER(PARTITION BY deal_id ORDER BY updated_at ASC) as prev_stage_time,
       updated_at - LAG(updated_at) OVER(PARTITION BY deal_id ORDER BY updated_at ASC) as duration_in_stage
FROM deal_stage_history
ORDER BY deal_id, updated_at;
```

---

## 3. High-Value GTM SQL Queries

### Query 1: Pipeline Velocity

$$Pipeline \; Velocity = \frac{Number \; of \; Deals \times Average \; Deal \; Size \times Win \; Rate \%}{Sales \; Cycle \; Length \; (Days)}$$

```sql
WITH metrics AS (
    -- Total Won deals
    SELECT 
        COUNT(id) FILTER(WHERE stage = 'Closed Won') AS won_deals_count,
        AVG(amount) FILTER(WHERE stage = 'Closed Won') AS avg_deal_size,
        
        -- Win Rate = Won / (Won + Lost)
        (COUNT(id) FILTER(WHERE stage = 'Closed Won')::FLOAT / 
         NULLIF(COUNT(id) FILTER(WHERE stage IN ('Closed Won', 'Closed Lost')), 0)) * 100 AS win_rate,
         
        -- Average Sales Cycle Duration
        AVG(EXTRACT(EPOCH FROM (updated_at - created_at))/86400) FILTER(WHERE stage = 'Closed Won') AS avg_sales_cycle_days
    FROM deals
)
SELECT 
    won_deals_count,
    avg_deal_size,
    win_rate,
    avg_sales_cycle_days,
    -- Pipeline velocity per day
    (won_deals_count * avg_deal_size * (win_rate / 100.0)) / NULLIF(avg_sales_cycle_days, 0) AS velocity_score
FROM metrics;
```

### Query 2: Monthly Cohort Retention

```sql
-- Cohort analysis by user signup month
WITH cohorts AS (
    SELECT id, email, 
           DATE_TRUNC('month', created_at) AS cohort_month
    FROM contacts
),
activity_months AS (
    SELECT DISTINCT c.cohort_month,
           c.id AS contact_id,
           DATE_TRUNC('month', a.activity_date) AS active_month,
           EXTRACT(MONTH FROM AGE(DATE_TRUNC('month', a.activity_date), c.cohort_month)) AS period_month
    FROM cohorts c
    JOIN activities a ON c.id = a.contact_id
)
SELECT cohort_month,
       COUNT(DISTINCT contact_id) FILTER(WHERE period_month = 0) AS Month_0,
       COUNT(DISTINCT contact_id) FILTER(WHERE period_month = 1) AS Month_1,
       COUNT(DISTINCT contact_id) FILTER(WHERE period_month = 2) AS Month_2,
       COUNT(DISTINCT contact_id) FILTER(WHERE period_month = 3) AS Month_3
FROM activity_months
GROUP BY cohort_month
ORDER BY cohort_month;
```
