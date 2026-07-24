# Reflection - Day 013: Relational DBs (Postgres)

A personal log reflecting on the learning outcomes and concepts mastered on Day 13.

---

## 💡 Key Takeaways & Lessons Learned

1.  **Analytical Reports belong in a Replica, not CRM**: Attempting to run complex multi-touch attribution or cohort conversions directly inside HubSpot or Salesforce is extremely limited and slow. Replicating the raw fields to a local PostgreSQL instance is the industry standard for GTM Engineering.
2.  **Indexing is mandatory for scale**: As traffic lists grow, unindexed SQL queries degrade. Creating B-Tree index keys on lookup properties (like foreign keys and UTM sources) is necessary to keep dashboards responsive.
3.  **Auditing with EXPLAIN**: Using `EXPLAIN QUERY PLAN` tells us exactly how the SQL engine compiles our commands, showing us if our index keys are actually being utilized.

---

## 💻 Script Verification

I ran the `Code/postgres_gtm.py` script to verify our SQL replica operations.
*   **Result**: 
    *   `Report 1`: Successfully aggregates Won revenue by UTM source (Google cpc closed $20,000.00; Newsletter email closed $12,000.00).
    *   `Report 2`: Correctly calculates the Funnel Conversion Rate (33.33% of leads converted to Won).
    *   `Optimization Audit`: The `EXPLAIN QUERY PLAN` output verifies that the engine uses `idx_leads_utm_source` (covering search criteria) and `idx_deals_lead_id` (covering joins).
*   **Insight**: This confirms our schema design is optimized for high-volume analytics queries.

---

## 🎯 Plan for Tomorrow
Tomorrow is Day 14: **Non-Relational DBs (MongoDB)**. I will focus on understanding document stores, MongoDB JSON collections, BSON structures, and designing schemas to track dynamic lead activities.
