# Reflection - Day 017: Reverse ETL (Census/Hightouch)

A personal log reflecting on the learning outcomes and concepts mastered on Day 17.

---

## 💡 Key Takeaways & Lessons Learned

1.  **Reverse ETL makes data warehouse metrics actionable**: Pushing data like aggregate logins or average grades directly into HubSpot Company objects allows sales reps to see how active a client is. It saves them from querying database tables.
2.  **Incremental Syncs preserve API Limits**: Running full syncs of 100,000 accounts every hour will crash CRM API limits. Enforcing watermarks (`updated_at > last_sync_time`) ensures we only push records that actually changed.
3.  **Decoupled calculations reduce errors**: Rather than calculating the "Health Status" directly inside the sync code, we define it inside a PostgreSQL View. This keeps the database as the single source of truth for business logic.

---

## 💻 Script Verification

I ran the `Code/reverse_etl.py` script to test the incremental sync, column mapping, and mock API posting logic.
*   **Result**: 
    *   *Incremental Filtering*: Successfully ignores `ametuniv.edu.in` (which was updated at 1783900000, below the watermark), selecting only `tolani.edu` and `imsgoa.org`.
    *   *Transformations*: Correctly maps Postgres columns to HubSpot tags (e.g. converting `total_exams_completed` to `cadet_exams_completed`).
    *   *Batch Sync*: The mock HubSpot API successfully logs the batch update of the 2 modified company profiles.
*   **Insight**: This proves how Reverse ETL optimizes API usage while syncing key business intelligence from databases to sales CRMs.

---

## 🎯 Plan for Tomorrow
Tomorrow is Day 18: **Customer Data Platforms (CDP) / Segment**. I will focus on understanding how CDPs aggregate user events across multiple channels and route them to analytics and marketing tools.
