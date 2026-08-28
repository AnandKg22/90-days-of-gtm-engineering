# Study Notes - Day 034: Funnel Metrics & Conversion Rates

Today's studies focused on B2B SaaS sales funnel stages (Lead, MQL, SQL, Opportunity, Closed Won), stage conversion rates, funnel velocity (days between transitions), conversion lag, database schemas for history tracking, and SQL window query functions.

---

## 1. The B2B SaaS Sales Funnel

To optimize customer acquisition, GTM teams map the journey into discrete sales stages:

```
[ Lead: Website signup ] ──────(30% MQL Conversion)──────> [ MQL: Marketing Qualified ]
                                                                 │
                                                      (50% SQL Conversion)
                                                                 ▼
[ Opportunity: Active Deal ] ◄───(40% Opportunity Conversion)─── [ SQL: Sales Qualified ]
               │
      (25% Closed Won)
               ▼
       [ Closed Won! ]
```

### Key Metrics
*   **Stage Conversion Rate**: The percentage of prospects who successfully move from one stage to the next.
*   **Funnel Velocity (Days)**: The average number of days a prospect spends in a specific stage before transitioning.
*   **Conversion Lag (Cycle Time)**: The total duration (in days) from the user's initial Lead creation to the final Closed Won payment.

---

## 2. Deep-Dive: Funnel Metrics Subtopics

To construct automated velocity dashboards, a GTM Engineer must master these three subtopics:

### 1. Database Design (Opportunity Stage History Logs)
*   **Definition**: Designing schemas that record every stage transition:
    *   **Deals**: Stores current deal status (`deal_id`, `company_key`, `amount`, `current_stage`).
    *   **Deal Stage Logs**: A historical log table capturing every stage change (`id`, `deal_id`, `from_stage`, `to_stage`, `transition_date`).
*   **GTM Application**: Capturing history timestamps is mandatory; transactional tables only store current stages, making velocity calculations impossible.

### 2. SQL Syntax (Velocity & Stage Lag Queries)
*   **Definition**: Writing SQL queries utilizing window functions (like `LEAD` or `LAG`) to calculate the time difference in days between consecutive log timestamps:
    ```sql
    WITH stage_transitions AS (
        SELECT 
            deal_id,
            to_stage AS stage_name,
            transition_date AS stage_start,
            LEAD(transition_date) OVER (PARTITION BY deal_id ORDER BY transition_date) AS stage_end
        FROM deal_stage_logs
    )
    SELECT 
        stage_name,
        AVG(JULIANDAY(stage_end) - JULIANDAY(stage_start)) AS average_days_in_stage
    FROM stage_transitions
    WHERE stage_end IS NOT NULL
    GROUP BY 1;
    ```

### 3. Query Optimization (Transition Indexes)
*   **Definition**: Optimizing history query runs.
*   **GTM Application**: Deal stage logs grow by millions of records. Row scans to compute lead-lags take minutes.
    *   **Indexes**: Build a compound B-Tree index on `(deal_id, transition_date)` to speed up window sorting functions.
    *   **Cache summaries**: Compute daily averages and save them to a `monthly_funnel_velocity_summary` table to keep Looker dashboards fast.
