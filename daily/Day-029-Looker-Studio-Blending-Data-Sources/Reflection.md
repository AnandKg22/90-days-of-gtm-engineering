# Reflection - Day 029: Blending Data Sources

A personal log reflecting on the learning outcomes and concepts mastered on Day 29.

---

## 💡 Key Takeaways & Lessons Learned

1.  **Left Outer Joins preserve conversion funnels**: Using an Inner Join on B2B leads and payments drops all non-converting leads, rendering lead-to-customer conversion metrics useless. Always use Left Outer Joins as the default GTM join operator.
2.  **Avoid browser-side joins (Looker Blending)**: Looker Blending queries each source database independently and executes joins in browser memory. On datasets exceeding 1,000 records, this client-side overhead causes browser lag. Joins belong in the warehouse.
3.  **Validate Join Keys**: When blending data from Stripe (using emails) and Salesforce (using contact IDs), you need a mapping table to align keys. Otherwise, the joins fail, returning empty columns.

---

## 💻 Script Verification

I ran the `Code/data_blender.py` script to test data blending types, record integrity, and client latency.
*   **Result**: 
    *   *Inner Join*: Returned only 3 records, dropping the 2 unconverted prospects.
    *   *Left Join*: Retained all 5 prospects, populating converted payments and leaving unconverted rows as `NULL`.
    *   *Data Audit*: Successfully flagged the 2 lost records in the Inner Join, showing how it biases conversion reports.
*   **Insight**: This confirms why GTM architectures must use Left Joins to maintain funnel visibility.

---

## 🎯 Plan for Tomorrow
Tomorrow is Day 30: **Cohort Analysis**. I will focus on understanding cohort retention models, grouping customers by signup weeks/months, and calculating weekly active user (WAU) retention graphs.
