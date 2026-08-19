# Day 028: Looker Studio (Parameters & Filters)

## Objective
Configure interactive dashboard filters (Dropdowns, Input Boxes, and Date Range selectors), declare custom user parameters inside Looker Studio data sources, reference parameters inside custom SQL queries using `@` syntax, and optimize BigQuery data scans using partition pruning date mappings.

## Topics Covered
- Client-side filters vs. Server-side parameters
- Interactive dashboard controls
- Custom SQL parameters (`@` syntax)
- Partition pruning via date parameters (`@DS_START_DATE`)
- Database query cost reduction

## Subtopics (Developed in Notes)
- Dashboard Design (Interactive Filter Controls)
- SQL Syntax (Custom SQL Parameters)
- Query Optimization (Partition Pruning via Date Parameters)

---

## 🛠️ Practical Exercise: Dashboard Filters & Parameters

In this exercise, we mapped out canvas control configurations inside Looker Studio:
*   **Industry Selector Dropdown**: Sets a client-side filter on the `industry` dimension.
*   **Analysis Window Date Selector**: Binds system parameters `@DS_START_DATE` and `@DS_END_DATE` to date partitions.
*   **Min Deal Value Input Box**: Maps parameter `@ds_min_amount` to a custom SQL query, filtering records on the database engine.

*View complete control layouts and parameterized queries in [Exercises.md](Exercises.md).*

---

## 🏫 Daily Project / Assignment: Parameterized SQL Query Engine

We built an executable Python parameterized query executor and cost auditor in [Code/parameterized_query.py](Code/parameterized_query.py):
*   Models a database deal table with close dates and deal values.
*   Accepts user inputs (representing minimum deal value and date ranges) and compiles them into database filters.
*   Compares **Client-Side Filtering** (scanning 100% of rows to filter in the dashboard) against **Server-Side Parameterized Filtering** (pruning partitions based on date parameters).
*   Calculates and logs query cost reductions.

*View project requirements in [Assignment.md](Assignment.md) and the pipeline diagram in [Architecture.md](Architecture.md).*

---

## 📂 Expected Deliverables
*   📝 [Day 28 Study Notes](Notes.md) — Client-side filters, parameters, custom SQL variables, and partition pruning.
*   📝 [Filter & Parameter Blueprints](Exercises.md) — Canvas controls and parameterized queries.
*   📝 [Query Engine Spec](Assignment.md) — Project requirements.
*   📊 [Query Flow Diagram](Architecture.md) — Looker parameters-to-database routing flow.
*   💻 [Parameterized Query Engine](Code/parameterized_query.py) — Executable parameter binding and audit program.

---

## 📝 Notes & Reflection
*   **Key Insight**: Binding date parameters directly to partitioned tables ensures cloud warehouses only scan matching partitions, reducing query costs by up to 99%.
*   **Study Log**: Read notes in [Notes.md](Notes.md).
*   **Daily Log**: Read reflections in [Reflection.md](Reflection.md).
