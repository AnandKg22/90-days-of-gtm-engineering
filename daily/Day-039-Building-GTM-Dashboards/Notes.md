# Study Notes - Day 039: Building GTM Dashboards

Today's studies focused on designing GTM executive dashboards, selecting operational and financial KPIs, building funnel visualizations, implementing weighted sales forecasting, and optimizing dashboard query speeds via caching and warehouse structures.

---

## 1. Core GTM KPI Selection

An executive GTM dashboard must balance high-level financial metrics with operational health indicators. The core metrics include:

### Financial Metrics
*   **Annual Recurring Revenue (ARR) & Monthly Recurring Revenue (MRR)**: The foundation of B2B SaaS health. Represents the predictable and recurring revenue components.
*   **Average Deal Size (ACV/ARPU)**: Calculated as `Total Closed Won ARR / Total Won Customers`. Tracks whether sales are moving upstream.

### Unit Economics
*   **Customer Acquisition Cost (CAC)**: Total sales and marketing spend over a given period divided by the number of new customers acquired.
*   **Lifetime Value (LTV)**: The estimated total revenue a customer will generate. Commonly modeled as `Avg ARR * Average Customer Lifespan (Years)`.
*   **LTV:CAC Ratio**: Measure of GTM efficiency. A healthy B2B SaaS target is `> 3.0x`. A ratio of `5.0x` or higher indicates exceptional efficiency, while `< 3.0x` suggests overspending.

### Funnel & Velocity Metrics
*   **Pipeline Volume**: The total value of all active deals (excluding Closed Won and Closed Lost).
*   **Lead-to-Win Rate**: The percentage of leads or opportunities that convert to Closed Won. Monitors the quality of pipeline generation and sales execution.

---

## 2. Sales Forecasting Models: Weighted vs. Unweighted

A critical component of GTM planning is forecasting bookings. There are two primary approaches:

### 1. Unweighted Pipeline
*   **Formula**: $\sum (\text{Value of all active opportunities})$
*   **Limitation**: Assumes all deals have a 100% chance of closing. Leads to overly optimistic projections, especially with early-stage deals.

### 2. Weighted Pipeline (Standard Practice)
*   **Formula**: $\sum (\text{Opportunity Value} \times \text{Stage Probability})$
*   **Mechanism**: Each stage in the CRM is mapped to a historical close probability:
    *   *Discovery*: 10%
    *   *Qualification*: 25%
    *   *Proposal*: 50%
    *   *Negotiation*: 80%
    *   *Closed Won*: 100%
*   **Result**: Provides a realistic forecast of expected bookings that finance and operations teams can rely on.

---

## 3. Deep-Dive: GTM Dashboard Subtopics

To construct performant, enterprise-grade GTM dashboards, a GTM Engineer must master these areas:

### 1. Dashboard Design & Metrics Selection
*   **Definition**: Selecting and arranging visualizations based on the viewer's persona:
    *   **Executive Board**: Focuses on MRR, ARR, LTV:CAC, and Top-level forecasting.
    *   **Sales Managers**: Focuses on rep performance, win rates, stage bottlenecks, and pipeline hygiene.
    *   **Marketing Operations**: Focuses on lead source attribution, MQL-to-SQL rates, and CAC by campaign.
*   **UX Principles**: Display high-level summary cards (KPI blocks) at the top, followed by pipeline distributions (funnel charts), and raw tables for granular drill-downs at the bottom.

### 2. SQL Syntax (Funnel Aggregation & Forecast Queries)
*   **Definition**: Writing SQL aggregation queries in the warehouse to feed BI dashboards.
*   **GTM Application**: Calculating pipeline distributions, conversion rates, and stage-weighted forecasts from deal tables:
    ```sql
    SELECT 
        stage,
        COUNT(deal_id) AS deal_count,
        SUM(value) AS total_value,
        SUM(value * CASE 
            WHEN stage = 'Discovery' THEN 0.10
            WHEN stage = 'Qualification' THEN 0.25
            WHEN stage = 'Proposal' THEN 0.50
            WHEN stage = 'Negotiation' THEN 0.80
            WHEN stage = 'Closed Won' THEN 1.00
            ELSE 0.00
        END) AS weighted_forecast
    FROM fact_deals
    GROUP BY stage;
    ```

### 3. Query Optimization (Clustered & Partitioned Tables)
*   **Definition**: Optimizing database schemas to keep dashboard widgets loading in sub-second times.
*   **GTM Application**: If dashboards query raw transaction tables directly, every filter change triggers a full table scan, increasing costs and loading times.
    *   **Partitioning**: Partition the deals database by date (`created_date`) so filters can scan data within specific quarters or months.
    *   **Clustering**: Cluster tables by `region` or `segment`. When dashboard filters are applied, the query engine skips irrelevant data blocks entirely.
    *   **BI Cache**: Use tools like BigQuery BI Engine or Looker Studio caching to store query results in RAM.

---

## 4. Summary of Dashboard Optimization Rules

| Optimization Method | Target Problem | Implementation |
| :--- | :--- | :--- |
| **BigQuery BI Engine** | High dashboard query costs & slow loading | Reserve RAM in BigQuery console for active tables. |
| **B-Tree Indexing** | Slow PostgreSQL filter queries | Build index on `(region, segment)` or `(sales_rep_id)`. |
| **dbt Incremental Models** | Outdated dashboard data | Materialize deals as pre-aggregated tables refreshed hourly. |
| **Partitioning** | Large table scans on date filters | Partition table by `DATE(created_at)`. |
