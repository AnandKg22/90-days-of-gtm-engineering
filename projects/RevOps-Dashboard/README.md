# Day 039: Building GTM Dashboards

## Objective
Build interactive, real-time executive dashboards that visualize GTM KPIs, map sales funnel stages, forecast revenue based on weighted pipelines, support dynamic filters (region, segment), and allow granular drill-downs for operational insights.

## Topics Covered
- KPI dashboards & executive reporting
- Sales forecasting models (weighted probability)
- Pipeline visualization & funnel stages
- Dynamic dashboard filters & drill-downs
- Real-time dashboard updates & data ingestion

## Subtopics (Developed in Notes)
- Dashboard Design (KPIs and Metrics Selection)
- SQL Syntax (Funnel Aggregation & Forecast Queries)
- Query Optimization (Clustered & Partitioned Tables for Dashboards)

---

## 🛠️ Practical Exercise: Funnel Analysis & Weighted Forecasting

In this exercise, we designed a GTM funnel visualization and forecasting model:
*   **Funnel Stages**: Discovery (10%), Qualification (25%), Proposal (50%), Negotiation (80%), Closed Won (100%), Closed Lost (0%).
*   **Weighted Value**: Calculating expected revenue of active deals by multiplying their values by their stage probabilities.
*   **Conversion Optimization**: Visualizing lead-to-win conversion rate across regions and segments to isolate bottlenecks.

*View complete forecasting logic and SQL queries in [Exercises.md](Exercises.md).*

---

## 🏫 Daily Project / Assignment: GTM Control Center

We built an executable Python executive dashboard simulator in [Code/gtm_control_center.py](Code/gtm_control_center.py):
*   Computes core GTM metrics: ARR, MRR, Avg Deal Size, Lead Win Rate, LTV, and LTV:CAC Ratio.
*   Renders a text-based ASCII funnel chart showing deal distribution.
*   Supports dynamic dashboard filters by **Region** and **Segment**.
*   Supports drill-downs by **Sales Rep** and **Funnel Stage**.
*   Simulates real-time data updates (deal creation, stage progression) and recalculates all metrics instantly.

*View project requirements in [Assignment.md](Assignment.md) and the dashboard system design in [Architecture.md](Architecture.md).*

---

## 📂 Expected Deliverables
*   📝 [Day 39 Study Notes](Notes.md) — Metrics selection, dashboard layouts, SQL queries, and caching rules.
*   📝 [Forecasting & SQL Spec](Exercises.md) — Funnel calculations and sample queries.
*   📝 [Simulator Spec](Assignment.md) — Project requirements.
*   📊 [Dashboard Architecture](Architecture.md) — Data flow and pipeline architecture.
*   💻 [GTM Control Center Simulator](Code/gtm_control_center.py) — Executable CLI executive dashboard.
*   📋 [GTM Dashboard Cheat Sheet](CheatSheet.md) — Formulas, SQL queries, and BI configurations.
*   🤖 [Dashboard Prompts](Prompts.md) — Prompts for automating dashboard creation.
*   🔗 [Dashboard Resources](Resources.md) — Reference documentation, tools, and platforms.
*   📝 [Daily Reflection](Reflection.md) — Key takeaways and lessons learned.

---

## 📝 Notes & Reflection
*   **Key Insight**: Implementing weighted forecasting on GTM dashboards helps finance and operations teams predict future ARR with high accuracy rather than relying on unweighted pipelines.
*   **Study Log**: Read notes in [Notes.md](Notes.md).
*   **Daily Log**: Read reflections in [Reflection.md](Reflection.md).

---

## 👤 Author & Connect

Developed by **Anand Kumar** — Go-To-Market Architect & Revenue Engineer.
*   **Website**: [akstack.com](https://akstack.com)
*   **GitHub**: [github.com/AnandKg22](https://github.com/AnandKg22)
*   **LinkedIn**: [linkedin.com/in/anandkg22](https://www.linkedin.com/in/anandkg22/)
