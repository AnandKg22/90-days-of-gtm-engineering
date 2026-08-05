# Study Notes - Day 021: dbt (Data Build Tool)

Today's studies focused on analytics engineering with dbt, modular SQL modeling, Jinja macro execution, compiling Directed Acyclic Graphs (DAG), schema testing, and materialization strategies.

---

## 1. Analytics Engineering with dbt

In modern cloud data stacks, raw data is loaded directly into the data warehouse (EL - Extract and Load). **dbt (Data Build Tool)** handles the **T (Transform)**. It allows analytics engineers to write modular `SELECT` statements in SQL, while dbt handles compiling those queries, building tables/views in the warehouse, testing data quality, and generating documentation.

---

## 2. Deep-Dive: dbt Subtopics

To construct robust analytics pipelines in dbt, a GTM Engineer must master these three subtopics:

### 1. Database Design (dbt Modular Layering)
*   **Definition**: Organizing SQL models into distinct folders representing processing maturity:
    *   **Staging (`models/staging/`)**: The entry layer. Models have a 1:1 relationship with raw source tables. They perform basic cleanup (renaming columns, casting data types, converting timestamps) but do not join tables or aggregate metrics. Prefixed with `stg_`.
    *   **Intermediate (`models/intermediate/`)**: The bridge layer. Joins staging models together or performs pre-aggregations. Prefixed with `int_`.
    *   **Marts (`models/marts/`)**: The business-ready layer. Contains final fact and dimension models (e.g. `fct_deals`, `dim_companies`) queried directly by BI tools.
*   **GTM Application**: Modular layering ensures that if a raw HubSpot CRM column name changes, you only edit a single staging file, leaving all downstream dashboards unbroken.

### 2. SQL Syntax (Jinja & DAG Referencing)
*   **Definition**: Writing SQL models with embedded Jinja macro syntax.
*   **GTM Application**: You replace static table names with the `{{ ref('model_name') }}` macro:
    ```sql
    -- fct_deals.sql
    SELECT * 
    FROM {{ ref('stg_deals') }}
    WHERE stage = 'Won';
    ```
    During compilation, dbt parses these `ref` tags to build the **DAG (Directed Acyclic Graph)**, ensuring it executes parent staging models before child marts tables.

### 3. Query Optimization (Materialization Configurations)
*   **Definition**: Specifying how dbt writes the compiled SQL model into the warehouse database:
    *   **View (Default)**: Compiles the SQL as a database `VIEW`. Good for fast iteration and low storage costs.
    *   **Table**: Compiles the SQL and writes it as a physical table. Speeds up read queries for BI tools but consumes storage and takes longer to compile.
    *   **Incremental**: Updates physical tables by only appending rows that changed since the last run. Crucial for scaling tables with billions of rows.
    *   **Ephemeral**: Does not create anything in the database; compiles the code as a CTE (Common Table Expression) inside downstream models.
*   **GTM Application**: Configuring materialization parameters in the yaml file:
    ```yaml
    +materialized: table
    ```
