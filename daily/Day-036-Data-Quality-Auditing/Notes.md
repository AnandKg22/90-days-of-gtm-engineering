# Study Notes - Day 036: Data Quality & Auditing

Today's studies focused on data quality indicators, schema validations, check constraints, duplicate detection, SQL cleaning queries, and database optimization strategies.

---

## 1. What is GTM Data Quality?

Bad data in B2B databases leads to lost revenue (e.g. sending emails to invalid addresses, calculating negative MRR values, or calling the same duplicate lead multiple times).

GTM Engineers run automated **Data Auditing** programs to check and enforce data quality rules:
*   **Schema Validation**: Checking that data fits type rules (e.g., date formats, integer bounds).
*   **Check Constraints**: Enforcing logical constraints at the database level.
*   **Missing Values (NULLs)**: Identifying empty fields where values are required (e.g. missing domains).
*   **Duplicate Detection**: Merging multiple records matching the same identifier (e.g. same email).

---

## 2. Deep-Dive: Data Quality Subtopics

To construct automated data sanitization pipelines, a GTM Engineer must master these three subtopics:

### 1. Database Design (DDL Check Constraints)
*   **Definition**: Writing data validation rules directly inside DDL table definitions to block invalid inputs at the database engine level:
    ```sql
    CREATE TABLE fact_deals (
        deal_id INT PRIMARY KEY,
        email VARCHAR(255) NOT NULL,
        amount_usd NUMERIC(10, 2),
        deal_stage VARCHAR(50),
        
        -- Enforce logical bounds at DDL tier
        CONSTRAINT chk_positive_amount CHECK (amount_usd >= 0.0),
        CONSTRAINT chk_valid_email CHECK (email LIKE '%@%'),
        CONSTRAINT chk_valid_stage CHECK (deal_stage IN ('Lead', 'MQL', 'SQL', 'Opportunity', 'Won'))
    );
    ```

### 2. SQL Syntax (Audit & Cleaning Queries)
*   **Definition**: Writing SQL statements to scan databases, count schema errors, and identify duplicate rows:
    *   **Find Duplicates**: Isolating duplicate accounts using window functions:
        ```sql
        WITH ranked_records AS (
            SELECT 
                lead_id,
                email,
                row_timestamp,
                ROW_NUMBER() OVER (PARTITION BY email ORDER BY row_timestamp DESC) AS rank
            FROM raw_leads
        )
        SELECT * FROM ranked_records WHERE rank > 1; -- Duplicate records
        ```

### 3. Query Optimization (Clean-Index Schedules)
*   **Definition**: Optimizing database read speeds during cleaning schedules.
*   **GTM Application**: Scanning billions of rows for duplicates stalls operational databases.
    *   **Indexes**: Build B-Tree indexes on lookup columns (`email`, `transition_date`) to accelerate duplicate identification queries.
    *   **Incremental Logs**: Rather than running full database scans daily, query only the changed rows since the last sync using timestamp watermarks.
