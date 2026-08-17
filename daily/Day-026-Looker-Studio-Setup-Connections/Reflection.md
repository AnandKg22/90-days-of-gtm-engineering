# Reflection - Day 026: Looker Studio Setup

A personal log reflecting on the learning outcomes and concepts mastered on Day 26.

---

## 💡 Key Takeaways & Lessons Learned

1.  **Do not let Looker perform complex joins**: Data Blending inside Looker Studio is slow and inefficient. Performing database joins at the warehouse layer using dbt or custom SQL views before linking to Looker ensures fast dashboard load times.
2.  **BI Engine memory reservations cut costs to zero**: Reserving BI Engine RAM in GCP caches repeat queries. This prevents Looker widgets from repeatedly scanning physical tables, saving query scan charges.
3.  **JDBC requires mandatory SSL**: Database connections are public pathways. Setting up standard JDBC connections to PostgreSQL requires mandatory SSL certificate uploads to prevent data sniffing.

---

## 💻 Script Verification

I ran the `Code/looker_connector_auditor.py` script to test security audits, latency warnings, and cache recommendations.
*   **Result**: 
    *   *PostgreSQL - Lead Logs*: Flagged a `[SECURITY RISK]` because it lacked JDBC-SSL encryption, and recommended certificate uploads.
    *   *BigQuery - Won Deals Mart*: Passed performance audits due to using `Custom-SQL`, and received a recommended BI Engine reservation of 440 MB.
    *   *BigQuery - Raw Event Log Staging*: Triggered a `[PERFORMANCE WARNING]` for running `Table-Selection` on a large 85 GB staging table, recommending custom SQL or dbt marts.
*   **Insight**: This auditor validates the checks GTM Engineers must run before exposing warehouse data to cloud BI tools.

---

## 🎯 Plan for Tomorrow
Tomorrow is Day 27: **Looker Studio (Adding Fields & Custom Queries)**. I will focus on writing calculated fields using Looker formulas (CONCAT, CASE, SAFE_CAST), building parameters, and executing custom SQL queries to build flexible reporting models.
