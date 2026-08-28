# GTM Architecture - Day 034: Sales Funnel & Velocity Pipelines

This document details the GTM database history schema mapping CRM opportunity logs to stage conversion and velocity metrics.

---

## 🔄 Funnel Analytics Processing Flow

The diagram below details the pipeline, showing how stage log timestamps are parsed to calculate velocity:

```mermaid
graph TD
    Logs[(CRM Stage Logs Table)] -->|1. SELECT deal_id, stage, date| Sort[Reconstruct Deal History Timeline]
    
    Sort -->|2. Apply SQL LEAD window| LeadWindow[Calculate next stage date]
    
    LeadWindow -->|3. Subtract dates| Duration[Days Spent per Stage]
    
    Duration -->|4. AVG days by stage| Velocity[Compute Funnel Velocity]
    
    Sort -->|5. COUNT(DISTINCT deal_id) by stage| Conversion[Compute Conversion Ratios]
    
    Velocity -->|6. Load charts| Dashboard[Looker Funnel Velocity Dashboard]
    Conversion -->|6. Load charts| Dashboard
```

---

## ⚙️ SQL Funnel Stage Log Schema

To calculate conversion lag and transition durations, databases run window queries across the following schema:

```sql
CREATE TABLE deal_stage_logs (
    id SERIAL PRIMARY KEY,
    deal_id INT NOT NULL,
    from_stage VARCHAR(100),
    to_stage VARCHAR(100) NOT NULL, -- Lead, MQL, SQL, Opportunity, Won
    transition_date DATE NOT NULL
);
```

### Analytical SQL Window Query:
```sql
WITH ordered_transitions AS (
    SELECT 
        deal_id,
        to_stage AS stage_name,
        transition_date AS stage_start,
        LEAD(transition_date) OVER (PARTITION BY deal_id ORDER BY transition_date) AS stage_end
    FROM deal_stage_logs
)

SELECT 
    stage_name,
    AVG(stage_end - stage_start) AS average_days_in_stage
FROM ordered_transitions
WHERE stage_end IS NOT NULL
GROUP BY 1;
```
