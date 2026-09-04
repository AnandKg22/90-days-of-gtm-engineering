# Prompts - Day 039: GTM Dashboard Automation

This library contains system and user prompts used to automate the design, SQL queries, and calculated fields for GTM dashboards.

---

### 1. KPI Dashboard Layout Planner Prompt
Use this prompt to outline a structured dashboard layout based on target audience and business metrics:
```markdown
You are a GTM Systems Architect. I need to design a Looker Studio executive dashboard for our B2B SaaS startup. 
We have the following tables: `fact_deals` and `dim_reps`.
Please provide:
1. A wireframe layout outline (headers, metrics blocks, charts, tables) optimized for executive-level readability.
2. The list of top 6 metrics to display in scorecard elements, including formulas.
3. The choice of visualizations (e.g., funnel chart, bar chart, line chart) for pipeline distribution and forecast-to-target tracking.
```

---

### 2. SQL Forecasting Query Generator Prompt
Use this prompt to write data warehouse aggregation queries:
```markdown
Translate the following forecasting requirements into a clean, optimized Google BigQuery SQL query:
- Base table: `vivaexams-production.vivaexams_gtm.fact_deals`
- Required outputs: Grouped by `region` and `segment`.
- Metrics:
  1. Total number of deals.
  2. Total ARR from Closed Won deals.
  3. Total value of active pipeline (excluding Won and Lost).
  4. Weighted forecast ARR using close probabilities: Discovery (10%), Qualification (25%), Proposal (50%), Negotiation (80%), Closed Won (100%).
- Ensure query speed is optimized by using partitioned dates where applicable.
```

---

### 3. Looker Studio Calculated Field Assistant Prompt
Use this prompt to write complex CASE statements or calculated fields in Looker Studio:
```markdown
Write a Looker Studio calculated field formula for:
1. Categorizing deal sizes: values above $100k as "Enterprise", between $25k and $100k as "Mid-Market", and below $25k as "SMB".
2. Flagging deals that have been in active pipeline stages (excluding Closed Won/Lost) for more than 90 days as "Stalled", else "Healthy".
Provide the CASE statement syntax ready to be copy-pasted into the Looker Studio formula editor.
```
