# Study Notes - Day 033: Efficiency Metrics (LTV:CAC & Payback)

Today's studies focused on Customer Acquisition Cost (CAC), Lifetime Value (LTV), CAC Payback Period, marketing spend databases, SQL aggregation queries for GTM ROI, and index optimizations.

---

## 1. GTM Efficiency Metrics in B2B SaaS

Acquiring customers at any cost is unsustainable. GTM Engineers track efficiency metrics to ensure marketing and sales channels generate profitable revenue:

### 1. Customer Acquisition Cost (CAC)
The average cost to acquire a single customer:
$$\text{CAC} = \frac{\text{Total Sales \& Marketing Expenses}}{\text{Number of Customers Acquired}}$$

### 2. Customer Lifetime Value (LTV)
The average gross margin revenue a customer generates before churning:
$$\text{LTV} = \frac{\text{Average Revenue Per User (ARPU)} \times \text{Gross Margin (\%) }}{\text{Monthly Churn Rate}}$$

### 3. LTV:CAC Ratio
Measures the return on acquisition spend. Target B2B SaaS benchmarks:
*   `< 3.0x`: Unprofitable. Spending too much to acquire low-value accounts.
*   `3.0x - 5.0x`: Healthy, standard B2B SaaS benchmark.
*   `> 5.0x`: Highly efficient, but suggests under-investing in marketing.

### 4. CAC Payback Period (Months)
The number of months required for a customer to generate enough gross margin revenue to cover their CAC:
$$\text{Payback Period (Months)} = \frac{\text{CAC}}{\text{ARPU} \times \text{Gross Margin (\%) }}$$
*   *Benchmark*: Healthy B2B SaaS target is `< 12 months` for mid-market accounts.

---

## 2. Deep-Dive: Efficiency Metrics Subtopics

To construct automated ROI dashboards, a GTM Engineer must master these three subtopics:

### 1. Database Design (Marketing Cost Tables)
*   **Definition**: Designing schemas that track sales/marketing overheads:
    *   **Marketing Spend**: Stores ad-click costs grouped by channel, campaign, and date (`campaign_id`, `channel_source`, `amount_spent`, `timestamp`).
    *   **Sales Overhead**: Stores monthly headcount and software costs (`department`, `month`, `overhead_cost`).
*   **GTM Application**: Database schemas must use unified campaign IDs to link marketing spend to acquired lead records.

### 2. SQL Syntax (Blended CAC Aggregations)
*   **Definition**: Writing SQL queries that join ad network cost tables with billing databases to calculate CAC per channel:
    ```sql
    WITH spend_summary AS (
        SELECT utm_source, SUM(amount_spent) AS total_spend
        FROM marketing_spend GROUP BY 1
    ),
    customer_summary AS (
        SELECT utm_source, COUNT(1) AS customers_won
        FROM customers WHERE status = 'Won' GROUP BY 1
    )
    SELECT 
        s.utm_source,
        s.total_spend,
        c.customers_won,
        (s.total_spend / c.customers_won) AS channel_cac
    FROM spend_summary s
    JOIN customer_summary c ON s.utm_source = c.utm_source;
    ```

### 3. Query Optimization (Campaign Index Partitioning)
*   **Definition**: Optimizing database read speeds.
*   **GTM Application**: Ad spend tables contain millions of rows of daily click logs.
    *   **Partitioning**: Partition the spend table by date (`timestamp`) to ensure queries only scan target quarters.
    *   **Indexing**: Build compound B-Tree indexes on `(campaign_id, utm_source)` to accelerate ROI JOIN queries.
