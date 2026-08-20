# Day 029: Looker Studio (Blending Data Sources)

## Objective
Configure Data Blends inside Looker Studio to join disparate SaaS datasets (HubSpot CRM and Stripe Billing), define join keys and operator rules, evaluate SQL join models (Left, Inner, and Full Joins), and analyze the browser performance cost of client-side blending.

## Topics Covered
- Looker Studio Blending panel
- Join Keys mapping
- SQL Join Operators (Left, Inner, Full Outer)
- Client-side browser blending overhead
- Lead-to-customer conversion metrics

## Subtopics (Developed in Notes)
- Dashboard Design (The Blending Canvas)
- SQL Syntax (Relational Join Operators)
- Query Optimization (The Cost of Client-Side Blending)

---

## 🛠️ Practical Exercise: Data Blending Blueprints

In this exercise, we designed a Looker Studio data blend profile:
*   **Left Table**: `HubSpot Contacts` (Dimensions: `email`, `source`, `employees`).
*   **Right Table**: `Stripe Charges` (Dimensions: `customer_email`, `plan_tier`, Metrics: `amount`).
*   **Join Key**: `email` (Left) <==> `customer_email` (Right).
*   **Join Operator**: **Left Outer Join** (selected to retain unconverted leads, which are dropped in Inner Joins).

*View complete blend specifications and SQL JOIN views in [Exercises.md](Exercises.md).*

---

## 🏫 Daily Project / Assignment: Looker Data Blender & Join Engine

We built an executable Python data blender simulator in [Code/data_blender.py](Code/data_blender.py):
*   Models two separate GTM datasets representing CRM leads and billing payments.
*   Implements **Inner Join** and **Left Outer Join** functions.
*   Audits **Data Integrity** (measuring how Inner Joins drop non-paying prospects, biasing conversion rate reports).
*   Audits **Performance** (simulating client-side rendering latency and advising database-level dbt joins).

*View project requirements in [Assignment.md](Assignment.md) and the connection routing flowchart in [Architecture.md](Architecture.md).*

---

## 📂 Expected Deliverables
*   📝 [Day 29 Study Notes](Notes.md) — Blending parameters, SQL joins, and browser-side overhead.
*   📝 [Data Blend Blueprint](Exercises.md) — Mapped dimensions, keys, and SQL statements.
*   📝 [Data Blender Spec](Assignment.md) — Project requirements.
*   📊 [Join Pipeline Diagram](Architecture.md) — Browser joins vs. database SQL joins flow.
*   💻 [GTM Data Blender](Code/data_blender.py) — Executable join engine and audit program.

---

## 📝 Notes & Reflection
*   **Key Insight**: Defaulting to Left Outer Joins on GTM dashboards preserves unconverted prospects in tables, enabling RevOps to calculate accurate Lead-to-Customer conversion percentages.
*   **Study Log**: Read notes in [Notes.md](Notes.md).
*   **Daily Log**: Read reflections in [Reflection.md](Reflection.md).
