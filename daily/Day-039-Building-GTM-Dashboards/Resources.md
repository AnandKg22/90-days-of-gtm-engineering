# Resources - Day 039: GTM Dashboards

This document lists reference guides, tools, and reading materials on KPI dashboard design, database caching, and sales forecasting methodologies.

---

## 🔗 Looker Studio & BI Documentation
- [Google Looker Studio Help Center](https://support.google.com/looker-studio) — Official guide for connecting sources, creating calculated fields, and sharing reports.
- [Looker Studio Calculated Fields Guide](https://support.google.com/looker-studio/answer/6299685) — Learn mathematical functions, CASE expressions, and text parsing formulas.
- [BigQuery BI Engine Overview](https://cloud.google.com/bigquery/docs/bi-engine-intro) — Google Cloud's fast, in-memory analysis service for Looker Studio dashboards.

---

## 📊 B2B SaaS Metrics & Forecasting
- [Andreessen Horowitz (a16z): 16 SaaS Metrics](https://a16z.com/16-saas-metrics-2/) — Industry standard definitions for ARR, MRR, LTV, CAC, and bookings.
- [Salesforce Forecasting Guide](https://www.salesforce.com/products/sales-cloud/resources/sales-forecasting-guide/) — Best practices for managing pipeline close probabilities and forecasting types.
- [dbt Analytics Engineering Guide](https://docs.getdbt.com/docs/introduction) — Learn how to pre-aggregate sales metrics in the warehouse before sending data to BI tools.

---

## 🛠️ Database Performance & Indexing
- [PostgreSQL Indexing Tutorial](https://www.postgresql.org/docs/current/indexes.html) — Technical guide for setting up multi-column B-Tree indexes for fast dashboard filtering.
- [BigQuery Table Partitioning & Clustering](https://cloud.google.com/bigquery/docs/partitioned-tables) — Speed up dashboards and reduce query billing costs.
