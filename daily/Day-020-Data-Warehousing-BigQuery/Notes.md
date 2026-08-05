# Study Notes - Day 020: Data Warehousing (Google BigQuery)

Today's studies focused on Google BigQuery (GCP), nested and repeated fields, table partitioning/clustering, writing BigQuery SQL arrays, and cost/performance optimization.

---

## 1. Google BigQuery in GCP GTM Stacks

Google BigQuery is a serverless, highly scalable cloud data warehouse. In Google Cloud Platform (GCP) GTM architectures, it serves as the central data repository because it integrates natively with:
*   Google Analytics 4 (GA4) raw event exports.
*   Looker Studio (BI and visualization).
*   Google Ads (for campaign matching).

Unlike traditional relational databases, BigQuery charges based on the **amount of data scanned** by queries, making query optimization a critical skill for GTM Engineers.

---

## 2. Deep-Dive: BigQuery Subtopics

To manage enterprise cloud warehousing pipelines, a GTM Engineer must master these three BigQuery subtopics:

### 1. Database Design (Partitioning & Clustering)
*   **Definition**:
    *   **Time-Unit Partitioning**: Splitting tables by date/timestamp columns (e.g., partitioning `ga4_events` by `_PARTITIONDATE`). When querying, you include a date filter: `WHERE _PARTITIONDATE = '2026-07-13'`. BigQuery only scans that day's partition, reducing costs by 99%.
    *   **Clustering**: Sorting table rows by up to four columns (e.g., clustering by `event_name` or `user_id`). This co-locates matching data on disk, speeding up search and join execution.

### 2. SQL Syntax (Nested & Repeated Fields)
*   **Definition**: BigQuery supports denormalized structures using `STRUCT` (objects) and `ARRAY` (nested lists) data types, avoiding expensive SQL joins.
*   **GTM Application**: You store user page views directly inside a single contact row as an array of structs. To query these nested arrays, you use the `UNNEST` operator to flatten the list:
    ```sql
    SELECT 
        email, 
        tp.url, 
        tp.source
    FROM `vivaexams_gtm.leads`,
    UNNEST(touchpoints) AS tp
    WHERE tp.source = 'google';
    ```

### 3. Query Optimization & Slot Management
*   **Definition**: Minimizing slots (virtual CPU allocation) and query costs.
*   **GTM Application**: You enforce these optimization rules:
    *   *Avoid `SELECT *`*: Explicitly select columns. Scanning extra columns increases query cost.
    *   *Join Order*: Put the largest table first in the join sequence, followed by smaller tables. BigQuery broadcasts small tables to all slots, optimizing memory.
    *   *Use Materialized Views*: Caches aggregate results, skipping table scans for repeat dashboard refreshes.
