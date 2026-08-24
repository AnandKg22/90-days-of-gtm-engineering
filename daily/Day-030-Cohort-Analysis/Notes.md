# Study Notes - Day 030: Cohort Analysis & Retention

Today's studies focused on Cohort Analysis, DAU/WAU/MAU metrics, stickiness ratios, cohort database schemas, SQL retention queries, and partitioning optimization.

---

## 1. What is Cohort Analysis?

A **cohort** is a group of users who share a common characteristic over a specific time window. In B2B SaaS, cohorts are usually defined by **acquisition date** (e.g. all users who signed up in January 2026).

**Cohort Analysis** measures how this group's behavior changes over time. Instead of looking at generic user growth (which hides product issues), cohort analysis shows **retention**—how many users return to use the product weeks or months after signing up.

---

## 2. Deep-Dive: Cohort Analysis Subtopics

To construct retention reporting pipelines, a GTM Engineer must master these three cohort subtopics:

### 1. Database Design (Activity Log Tables)
*   **Definition**: Designing the underlying tables that log user behaviors:
    *   **User Table**: Stores user signup dates (`user_id`, `created_at`).
    *   **Activity Logs**: Tracks every time a user logs in or runs an event (`user_id`, `event_name`, `timestamp`).
*   **GTM Application**: Database schemas must keep log rows narrow and index `user_id` and `timestamp` columns to ensure fast aggregation runs.

### 2. SQL Syntax (Retention Queries)
*   **Definition**: Writing multi-step SQL queries to group users into cohorts and track activity intervals:
    *   **Step 1**: Find each user's signup week using a CTE:
        ```sql
        WITH cohort_start AS (
            SELECT user_id, MIN(DATE_TRUNC(created_at, WEEK)) AS cohort_week
            FROM users GROUP BY 1
        )
        ```
    *   **Step 2**: Join activity logs to the cohort date, calculating the interval difference in weeks:
        ```sql
        SELECT 
            c.cohort_week,
            DATE_DIFF(DATE_TRUNC(a.timestamp, WEEK), c.cohort_week, WEEK) AS week_number,
            COUNT(DISTINCT a.user_id) AS active_users
        FROM activity_logs a
        JOIN cohort_start c ON a.user_id = c.user_id
        GROUP BY 1, 2
        ```
    *   **Step 3**: Pivot the results to build the final cohort retention matrix grid.

### 3. Query Optimization (Partitioning & Indexing Logs)
*   **Definition**: Optimizing database read performance.
*   **GTM Application**: Activity log tables grow by millions of rows daily. Running cohort queries across full tables will freeze databases.
    *   **Partitioning**: Partition the log table by date (`timestamp`).
    *   **Indexes**: Create a compound B-Tree index on `(user_id, timestamp)` to speed up min-date evaluations.
    *   **Materialized Views**: Pre-compile daily active user aggregates every night, querying only the pre-compiled views for Looker charts.
