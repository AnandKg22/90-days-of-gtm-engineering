# Project Assignment - Day 021: dbt Compiler & DAG Test Engine

This project requires developing a Python dbt compiler simulation that reads modular SQL models, parses Jinja `ref` references to build execution DAGs, compiles code to native SQL queries, executes them sequentially in SQLite, and runs schema constraints validations.

---

## 🎯 Requirements

Your Python simulation must:
1.  Define a dictionary of dbt SQL model templates containing `{{ source(...) }}` and `{{ ref(...) }}` references.
2.  Implement a **DAG Compiler**:
    *   Parse the model files to extract dependencies.
    *   Determine the correct execution sequence (e.g., executing staging models first, then joining them in marts).
3.  Implement a **Jinja Compiler**:
    *   Compile `{{ source('raw_crm', 'leads') }}` into the physical raw table name `raw_leads`.
    *   Compile `{{ ref('stg_leads') }}` into the staging view name `stg_leads`.
4.  Execute the compiled SQL statements in an in-memory SQLite database seeded with raw campaign details.
5.  Implement a **dbt Schema Test Runner**:
    *   Execute SQL test checks verifying that the primary keys in the compiled tables are `unique` and `not_null`.
    *   If a constraint fails, log a testing exception alert.

---

## 💻 Deliverable Code

A complete, working dbt simulator script has been created and placed in [Code/dbt_transformer.py](Code/dbt_transformer.py). It models the compilation sequence, executes queries, runs schema validation checks, and outputs the performance reports.
