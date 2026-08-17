# Study Notes - Day 026: Looker Studio Setup & Connections

Today's studies focused on Looker Studio data connectors (BigQuery, PostgreSQL, Google Sheets), database credential configurations, custom SQL queries inside Looker, and BI Engine caching optimizations.

---

## 1. Looker Studio in the GTM Stack

**Looker Studio** (formerly Google Data Studio) is Google's serverless business intelligence and visualization tool. In B2B GTM stacks, it is the primary dashboard interface because:
*   It connects natively to Google BigQuery, PostgreSQL, and Google Sheets without needing a server.
*   It is free and supports sharing dashboard links directly with RevOps, Sales leaders, and Executives.

---

## 2. Deep-Dive: Looker Studio Subtopics

To design high-performance dashboards, a GTM Engineer must master these three Looker Studio subtopics:

### 1. Dashboard Design (Visual Layouts & Filters)
*   **Definition**: Formatting layouts to display key business metrics:
    *   **KPI Scorecards**: Display single consolidated numbers (e.g. Total MRR, Active Seats).
    *   **Controls & Filters**: Adding Date Range selectors, Dropdown lists (filtering by size tier or campaign), and search boxes.
    *   **Grid Layouts**: Positioning overview charts (e.g., bar charts of sales by quarter) at the top, and detailed tables at the bottom.

### 2. SQL Syntax (Custom Connector SQL)
*   **Definition**: Writing custom database queries directly inside the Looker Studio connector wrapper.
*   **GTM Application**: Rather than selecting a raw database table and letting Looker perform joins inside its visual editor (which runs slow queries), a GTM Engineer writes a custom SQL query:
    ```sql
    -- Custom BigQuery SQL in Looker Studio
    SELECT 
        c.company_name,
        c.size_tier,
        SUM(f.amount_usd) AS total_revenue
    FROM `vivaexams_gtm.fact_deals` f
    JOIN `vivaexams_gtm.dim_companies` c ON f.company_key = c.company_key
    GROUP BY 1, 2;
    ```

### 3. Query Optimization (Caching & BI Engine)
*   **Definition**: Controlling dashboard loading speed and minimizing data query costs:
    *   **Data Freshness**: Configuring the cache refresh interval (e.g., refreshing every 4 hours instead of every 15 minutes to reduce database queries).
    *   **BigQuery BI Engine**: A fast, in-memory analysis service. Reserving BI Engine memory (e.g., 1 GB) in GCP allows Looker Studio queries to execute instantly without scanning physical tables, cutting costs to zero.
    *   **Avoid Looker Blending**: Looker "Data Blending" (joining sources inside Looker) executes slow client-side queries. Always perform joins in the warehouse using dbt or custom SQL views before connecting to Looker.
