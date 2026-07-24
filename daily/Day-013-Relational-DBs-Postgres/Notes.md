# Study Notes - Day 013: Relational Databases (Postgres)

Today's studies focused on relational databases (PostgreSQL), data types, constraints, SQL queries, normalization, indexing, and query optimization.

---

## 1. PostgreSQL in GTM Engineering

Standard CRMs are transactional (good for editing single leads), but poor for heavy analytics. GTM Engineers replicate CRM data to a local PostgreSQL database to:

*   **Run complex queries**: Joining CRM deals, Stripe invoice logs, and Google Ad touchpoints.
*   **Enforce data integrity**: Using Primary Keys (PK), Foreign Keys (FK), and `NOT NULL` constraints.
*   **Scale analytics**: Storing millions of click events and running fast cohort reports.

---

## 2. Deep-Dive: Relational Databases Subtopics

To manage data replication pipelines, a GTM Engineer must master these three database subtopics:

### 1. Database Design (Normalization)
*   **Definition**: Organizing database columns and tables to minimize redundancy and dependency:
    *   *First Normal Form (1NF)*: Ensure columns contain atomic values (no lists of tech stacks inside a single cell).
    *   *Second Normal Form (2NF)*: Ensure all non-key columns depend entirely on the primary key.
    *   *Third Normal Form (3NF)*: Eliminate transitive dependencies (e.g. storing company size on the contact table; it belongs on the company table).
*   **GTM Application**: Clean schemas prevent data corruption when syncing records across tools.

### 2. SQL Syntax (Queries & Joins)
*   **Definition**: Writing SQL statements to manipulate and retrieve data.
*   **GTM Application**: You must write queries to aggregate pipeline values and conversion metrics:
    *   `LEFT JOIN`: Retrieves all contacts and their companies (even if the contact has no company).
    *   `GROUP BY` & `SUM`: Aggregates deal values by lead acquisition channel.

### 3. Query Optimization (Indexes & Execution Plans)
*   **Definition**: Increasing query execution speed, particularly as database tables scale to millions of rows.
*   **GTM Application**:
    *   **B-Tree Indexes**: Created on columns frequently used in joins or lookups (e.g., `email`, `company_id`, `created_at`).
    *   **EXPLAIN ANALYZE**: A Postgres command that prints the query planner's execution steps, showing whether it is scanning the whole table (slow) or using an index (fast).
