# Study Notes - Day 027: Looker Studio Calculated Fields & Custom SQL

Today's studies focused on Looker Studio calculated fields (dimensions vs. metrics), parameters, conditional `CASE` formulas, data type `CAST` conversions, and query execution optimizations.

---

## 1. Looker Studio Calculated Fields

Calculated fields allow GTM Engineers to write formulas that transform data directly inside the Looker Studio reporting interface.

*   **Calculated Dimensions**: Create new descriptive fields by transforming strings, categories, or dates (e.g. merging `first_name` and `last_name` into `fullname`).
*   **Calculated Metrics**: Create new numeric aggregations (e.g. dividing `Revenue` by `Leads` to calculate `Avg Deal Value`).

---

## 2. Deep-Dive: Looker Studio Fields Subtopics

To construct flexible, high-performance dashboards, a GTM Engineer must master these three subtopics:

### 1. Dashboard Design (Calculated Fields & String Formulas)
*   **Definition**: Writing frontend formulas to format columns inside Looker charts:
    *   `CONCAT(first_name, " ", last_name)`: Combines names.
    *   `LOWER(email)`: Standardizes email casing to prevent duplicate rows.
    *   `REGEXP_EXTRACT(url, '^/([^/]+)')`: Extracts the parent directory path from a URL.
*   **GTM Application**: Formatting CRM fields into readable text for executive scorecards.

### 2. SQL Syntax (CASE & CAST Functions)
*   **Definition**: Applying conditional branches and datatype conversions in queries.
    *   **CASE Statement**: Sets conditions to segment metrics:
        ```sql
        CASE 
            WHEN amount_usd >= 15000 THEN "Tier 1: Enterprise"
            WHEN amount_usd >= 5000 AND amount_usd < 15000 THEN "Tier 2: Mid-Market"
            ELSE "Tier 3: SME"
        END
        ```
    *   **CAST Function**: Converts field types (e.g. converting a raw string of numbers to an integer to run sum calculations):
        ```sql
        CAST(seat_count_string AS INT64)
        ```

### 3. Query Optimization (Frontend vs. Warehouse Execution)
*   **Definition**: Deciding *where* to run calculation calculations.
*   **GTM Application**:
    *   *Frontend Execution*: Writing calculated fields inside Looker Studio. This runs calculations in the browser, which causes sluggish rendering if the dashboard has 10+ widgets or processes 10,000+ rows.
    *   *Warehouse Execution*: Writing calculations inside the database custom SQL connector or dbt models. This pre-calculates columns before Looker fetches them, reducing browser load times to zero. Always pre-calculate complex CASE statements in the warehouse.
