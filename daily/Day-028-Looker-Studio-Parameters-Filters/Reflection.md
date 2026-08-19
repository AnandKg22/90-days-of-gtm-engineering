# Reflection - Day 028: Parameters & Filters

A personal log reflecting on the learning outcomes and concepts mastered on Day 28.

---

## 💡 Key Takeaways & Lessons Learned

1.  **Parameters enforce query-level optimizations**: Slicing data using browser dropdown filters is simple, but it requires loading all raw records first. Passing parameters directly to database queries is much more efficient since it filters records before they cross the network.
2.  **Date parameters prune partitions**: Binding `@DS_START_DATE` and `@DS_END_DATE` to partitioned columns ensures BigQuery only scans the target date slices. This prevents expensive full table scans.
3.  **Input controls simplify self-serve analytics**: Exposing variables as input boxes (e.g. letting users adjust minimum deal amounts dynamically) allows non-technical sales leaders to run complex data scenarios.

---

## 💻 Script Verification

I ran the `Code/parameterized_query.py` script to test query filtering, row scans, and cost savings.
*   **Result**: 
    *   *Case 1 (Client-side)*: Scanned all 5 database records (100% table scan overhead) to filter a single company.
    *   *Case 2 (Parameterized)*: Passed `@ds_min_amount = $10,000` and date boundaries, scanning only 3 rows (pruning the other 2 partitions).
    *   *Cost reduction*: Audited a **40.0% database scan volume reduction** on this small dataset.
*   **Insight**: This proves that binding parameters directly to SQL filters limits raw data reads, securing dashboard performance.

---

## 🎯 Plan for Tomorrow
Tomorrow is Day 29: **Looker Studio (Blending Data Sources)**. I will focus on understanding the mechanics of joining multiple disparate data sources (like matching Stripe billing rows to Google Analytics session logs) inside Looker's Blending Canvas, mapping join keys, and managing left-outer joins.
