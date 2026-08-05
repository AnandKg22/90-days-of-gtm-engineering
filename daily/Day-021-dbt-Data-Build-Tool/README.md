# Day 021: dbt (Data Build Tool)

## Objective
Understand analytics engineering using dbt, configure staging and marts model directories, write modular SQL files with Jinja macro references, compile Directed Acyclic Graphs (DAG), and build automated schema test assertions.

## Topics Covered
- dbt analytics engineering
- Staging and Marts layers
- Jinja macro ref tags
- DAG execution logic
- Data schema assertions

## Subtopics (Developed in Notes)
- Database Design (dbt Modular Layering)
- SQL Syntax (Jinja & DAG Referencing)
- Query Optimization (Materialization Configurations)

---

## 🛠️ Practical Exercise: dbt Project Schema Design

In this exercise, we designed a dbt transformation project:
*   **Staging Layer**: Models (`stg_leads.sql`, `stg_deals.sql`) that clean raw columns, lowercase emails, and standardize column types using the `{{ source(...) }}` macro.
*   **Marts Layer**: Fact model (`fct_deals.sql`) that joins clean staging views via `{{ ref(...) }}` to generate business-ready revenue datasets.
*   **dbt Project Configurations**: Outlined folders and yml settings defining materializations (Views vs. Tables).

*View complete directory models and Jinja queries in [Exercises.md](Exercises.md).*

---

## 🏫 Daily Project / Assignment: dbt Compiler & DAG Test Engine

We built an executable Python dbt orchestrator simulator in [Code/dbt_transformer.py](Code/dbt_transformer.py):
*   Reads staging and marts SQL templates containing Jinja macros.
*   Resolves the DAG dependency sequence (executing `stg_leads` and `stg_deals` views before building `fct_deals` table).
*   Compiles Jinja macros to raw SQL queries and executes them in an in-memory SQLite database.
*   Executes automated dbt schema tests (assertions checking that deal IDs are unique and not null).

*View project requirements in [Assignment.md](Assignment.md) and the dependency graph in [Architecture.md](Architecture.md).*

---

## 📂 Expected Deliverables
*   📝 [Day 21 Study Notes](Notes.md) — Modular layers, Jinja references, and materializations.
*   📝 [dbt Project Blueprints](Exercises.md) — Folder mappings and model SQL queries.
*   📝 [Compiler Spec](Assignment.md) — Project requirements.
*   📊 [DAG Dependency Graph](Architecture.md) — Visual DAG pipeline diagram.
*   💻 [dbt Compiler Engine](Code/dbt_transformer.py) — Executable dbt compilation and testing simulator.

---

## 📝 Notes & Reflection
*   **Key Insight**: Implementing automated data testing constraints (Unique, Not Null) in the dbt pipeline isolates data errors before they corrupt corporate reports and Looker dashboards.
*   **Study Log**: Read notes in [Notes.md](Notes.md).
*   **Daily Log**: Read reflections in [Reflection.md](Reflection.md).
