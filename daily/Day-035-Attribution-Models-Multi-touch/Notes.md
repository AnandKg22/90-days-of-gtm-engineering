# Study Notes - Day 035: Multi-Touch Attribution Models

Today's studies focused on First Touch, Last Touch, Linear, Time Decay, Position Based (U-Shaped) attribution models, user click tracking database schemas, SQL weight calculators, and query optimizations.

---

## 1. Marketing Attribution Models

B2B customer journeys are complex, with prospects clicking multiple ads before converting. **Attribution Modeling** determines how credit (and revenue) is distributed among those touchpoints.

| Attribution Model | Revenue Allocation Rules | Best Use Case |
| :--- | :--- | :--- |
| **First Touch** | 100% of conversion credit goes to the first touchpoint. | Brand awareness campaigns. |
| **Last Touch** | 100% of conversion credit goes to the final click before conversion. | High-intent conversion channels. |
| **Linear** | Revenue is split equally across all touchpoints. | Balanced campaigns with low touch volume. |
| **Time Decay** | Touchpoints closer in time to conversion receive exponentially more credit. | Short-cycle conversion events. |
| **Position-Based (U-Shaped)** | 40% to First Touch, 40% to Last Touch, 20% split among middle touches. | Standard B2B enterprise sales cycles. |

---

## 2. Deep-Dive: Attribution Modeling Subtopics

To construct automated ROI dashboards, a GTM Engineer must master these three subtopics:

### 1. Database Design (User Click Tracking Tables)
*   **Definition**: Designing schemas that log user ad clicks and conversion amounts:
    *   **User Clicks**: Tracks every user touchpoint (`click_id`, `user_id`, `utm_source`, `timestamp`).
    *   **Conversions**: Records won deals (`user_id`, `deal_value`, `conversion_date`).
*   **GTM Application**: Schemas must maintain historical click chains associated with user cookie IDs or email matches to reconstruct the purchase timeline.

### 2. SQL Syntax (Touchpoint Weight Aggregations)
*   **Definition**: Writing SQL window queries to identify the sequence of user touches and compute weights:
    ```sql
    WITH ordered_touches AS (
        SELECT 
            user_id,
            utm_source,
            ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY timestamp ASC) AS touch_index,
            COUNT(1) OVER (PARTITION BY user_id) AS total_touches
        FROM user_clicks
    )
    ```
    Comparing `touch_index` to `total_touches` allows you to isolate First Touch (`touch_index = 1`) and Last Touch (`touch_index = total_touches`) to apply weights.

### 3. Query Optimization (Attribution View Materializations)
*   **Definition**: Optimizing slow attribution query runs.
*   **GTM Application**: Click logs grow by billions of rows. Running window functions to sort clicks is slow.
    *   **B-Tree Indexes**: Build indexes on `(user_id, timestamp)` to accelerate ROW_NUMBER partitions.
    *   **Materialized Tables**: Write daily cron scripts that pre-calculate the first, last, and middle touchpoints for won deals and save them to a `deal_attribution_summary` table. Looker queries this summary table directly, reducing click log scans.
