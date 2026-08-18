# Reflection - Day 027: Calculated Fields

A personal log reflecting on the learning outcomes and concepts mastered on Day 27.

---

## 💡 Key Takeaways & Lessons Learned

1.  **Offload calculations to the Database**: While Looker formulas (`CONCAT`, `CASE`) are convenient for quick checks, executing them client-side inside the browser becomes a bottleneck for large datasets. Compiling them inside PostgreSQL Views or BigQuery custom SQL is the best practice.
2.  **Use SAFE_CAST to protect queries**: Relational databases fail and abort queries if a cast fails (e.g. trying to cast `"twenty"` to an integer). Using `SAFE_CAST` (in BigQuery) or `TRY_CAST` (in Snowflake) returns `NULL` instead of crashing, keeping dashboards live.
3.  **CASE logic standardizes CRM data**: Raw sales data is messy. Applying conditional CASE branches standardizes attributes (such as grouping company sizes into discrete SME vs. Enterprise tiers) directly at the analytical tier.

---

## 💻 Script Verification

I ran the `Code/calculated_fields_engine.py` script to compare frontend formula parser loops against warehouse SQL views.
*   **Result**: 
    *   *Frontend Loop*: Took ~33.82 ms (simulating browser-side row loop rendering lag).
    *   *Warehouse SQL View*: Loaded in ~0.01 ms (pre-calculated on disk).
    *   *Speed Increase*: Measured at ~3300x faster execution.
*   **Insight**: The speed audit confirms why complex text consolidations and conditional segments should be written as database views.

---

## 🎯 Plan for Tomorrow
Tomorrow is Day 28: **Looker Studio (Parameters & Filters)**. I will focus on configuring user interactive filters, setting up input controls, mapping dropdown selectors, and binding variables to custom SQL query parameters.
