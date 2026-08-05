# Reflection - Day 021: dbt (Data Build Tool)

A personal log reflecting on the learning outcomes and concepts mastered on Day 21.

---

## 💡 Key Takeaways & Lessons Learned

1.  **Modular SQL transforms avoid copy-paste errors**: Writing monolithic SQL files with 500 lines of CTEs is impossible to maintain. Breaking them down into staging, intermediate, and marts layers makes data transformations clean and reusable.
2.  **dbt DAG solves dependency sequencing**: Manually coordinating when views and tables compile in the database is prone to errors. Using Jinja `{{ ref(...) }}` allows dbt to build the execution tree automatically.
3.  **Data Testing catches pipeline failures early**: Running automated schema tests (Unique, Not Null) on primary keys identifies data replication issues before they corrupt executive Looker dashboards.

---

## 💻 Script Verification

I ran the `Code/dbt_transformer.py` script to verify our DAG compilation, SQLite execution, and test runner.
*   **Result**: 
    *   *DAG sequence*: Correctly executes `stg_leads` and `stg_deals` before joining them in `fct_deals`.
    *   *Jinja compilation*: Successfully compiles source and ref macros to native SQLite commands.
    *   *Data verification*: Correctly matches IMSGOA ($8,000.00) and AMET ($15,000.00) won deals.
    *   *Schema testing*: Both Unique and Not Null checks pass.
*   **Insight**: This proves how dbt standardizes data transformation pipelines and secures data quality.

---

## 🎯 Plan for Tomorrow
Tomorrow is Day 22: **Integration Challenges**. I will focus on diagnosing API rate limits, handling sync errors, mapping custom identifiers, and resolving schema conflicts across multi-system GTM stacks.
