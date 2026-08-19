# Study Notes - Day 028: Looker Studio Parameters & Filters

Today's studies focused on Looker Studio filters (dropdowns, input boxes, date controls), parameter declarations, custom SQL parameter variables, and partition-pruning optimizations.

---

## 1. Parameters vs. Filters in Looker Studio

*   **Interactive Filters**: Slice data *after* it is loaded in the browser. For example, if Looker loads 1,000 deal rows, a dropdown filter for "SME" simply hides the "Enterprise" rows from the chart.
*   **Parameters**: Pass user-defined variables *before* the database runs the query. A parameter value is sent directly to the database engine, forcing it to filter records on disk before sending them to the browser.

---

## 2. Deep-Dive: Looker Studio Parameters Subtopics

To design responsive, cost-effective dashboards, a GTM Engineer must master these three subtopics:

### 1. Dashboard Design (Interactive Filter Controls)
*   **Definition**: Placing controls on the canvas to enable self-serve report filtering:
    *   **Dropdown List**: Allows users to filter charts by category (e.g. `industry` or `lead_source`).
    *   **Date Range Control**: Standardizes date window checks.
    *   **Input Box**: Allows users to type custom search text (e.g., entering a specific domain).

### 2. SQL Syntax (Custom SQL Parameters)
*   **Definition**: Declaring parameters in Looker and referencing them in custom SQL queries using the `@` symbol:
    *   You define a parameter named `min_deal_value` (type: number, default: 1000).
    *   You write the custom SQL connector query referencing this parameter:
        ```sql
        SELECT 
            deal_id,
            company_name,
            amount_usd
        FROM `vivaexams_gtm.fact_deals`
        WHERE amount_usd >= @min_deal_value;
        ```
    *   When a user types `5000` in the dashboard input box, Looker runs the query with `@min_deal_value = 5000`.

### 3. Query Optimization (Partition Pruning via Date Parameters)
*   **Definition**: Forcing Looker's date selector to prune database table partitions on disk.
*   **GTM Application**:
    *   Looker Studio provides built-in system parameters: `@DS_START_DATE` and `@DS_END_DATE`.
    *   When querying partitioned tables in BigQuery, you bind these parameters directly to the SQL `WHERE` clause:
        ```sql
        SELECT * 
        FROM `vivaexams_gtm.partitioned_events`
        WHERE _PARTITIONDATE BETWEEN PARSE_DATE('%Y%m%d', @DS_START_DATE) 
                                 AND PARSE_DATE('%Y%m%d', @DS_END_DATE);
        ```
    *   This ensures BigQuery only scans table partitions within the selected date window, preventing expensive full table scans.
