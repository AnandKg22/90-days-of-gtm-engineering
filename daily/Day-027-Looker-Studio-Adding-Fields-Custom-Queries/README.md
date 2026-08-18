# Day 027: Looker Studio (Adding Fields & Custom Queries)

## Objective
Configure calculated fields (dimensions and metrics) inside Looker Studio data sources, write conditional `CASE` statements and type `CAST` conversions, and evaluate the query performance differences of executing formulas client-side vs. database-side.

## Topics Covered
- Calculated Dimensions vs. Metrics
- Looker Studio text formulas (CONCAT, LOWER)
- SQL CASE conditional logic
- SQL CAST & SAFE_CAST functions
- Caching performance of custom queries

## Subtopics (Developed in Notes)
- Dashboard Design (Calculated Fields & String Formulas)
- SQL Syntax (CASE & CAST Functions)
- Query Optimization (Frontend vs. Warehouse Execution)

---

## 🛠️ Practical Exercise: Calculated Fields Formulas

In this exercise, we designed custom field formulas inside the Looker Studio dashboard:
*   **Lead Full Name**: Merges first and last name strings: `CONCAT(first_name, " ", last_name)`.
*   **Acquisition Segment**: Groups leads by employee sizes: `CASE WHEN employees > 50 THEN "Enterprise" ELSE "SME" END`.
*   **License Quantity**: Converts string counts to integers: `CAST(seats_count AS NUMBER)`.
*   **Custom SQL Wrapper**: Wrote a pre-compiled SQL database view to pre-calculate these fields in BigQuery.

*View complete formula sheets and custom SQL scripts in [Exercises.md](Exercises.md).*

---

## 🏫 Daily Project / Assignment: Calculated Fields & Custom SQL Engine

We built an executable Python Looker calculated fields parser and performance auditor in [Code/calculated_fields_engine.py](Code/calculated_fields_engine.py):
*   Parses core Looker formula operations: `CONCAT`, `CASE`, and `CAST`.
*   Simulates **Frontend Rendering** (looping through rows inside the client browser to apply string splits and conditional checks).
*   Simulates **Warehouse pre-compilation** (instantly loading completed column keys from custom SQL views).
*   Compares execution speeds, outputting optimization alerts when frontend lag becomes significant.

*View project requirements in [Assignment.md](Assignment.md) and the database optimization diagram in [Architecture.md](Architecture.md).*

---

## 📂 Expected Deliverables
*   📝 [Day 27 Study Notes](Notes.md) — Dimension/metric formulas, CASE logic, and warehouse pre-aggregations.
*   📝 [Formula Blueprints](Exercises.md) — Looker formulas and Custom SQL view queries.
*   📝 [Calculations Spec](Assignment.md) — Project requirements.
*   📊 [Processing Flowchart](Architecture.md) — Client vs. Serverless processing workloads diagram.
*   💻 [Formula Engine Script](Code/calculated_fields_engine.py) — Executable calculated fields parsing program.

---

## 📝 Notes & Reflection
*   **Key Insight**: Implementing `SAFE_CAST` (in BigQuery) or `TRY_CAST` (in Snowflake) in database views prevents dashboard widget crashes when raw tables contain corrupted text strings.
*   **Study Log**: Read notes in [Notes.md](Notes.md).
*   **Daily Log**: Read reflections in [Reflection.md](Reflection.md).
