# Reflection - Day 035: Attribution Models

A personal log reflecting on the learning outcomes and concepts mastered on Day 35.

---

## 💡 Key Takeaways & Lessons Learned

1.  **Single-touch models skew marketing budgets**: Last-Touch models attribute 100% of revenue to the final conversion click (e.g. brand searches), penalizing top-of-funnel channels (like LinkedIn video ads) that introduced the customer in the first place.
2.  **U-Shaped (Position-Based) models balance the funnel**: Allocating 40% to the first click (discovery), 40% to the last click (closing), and 20% to the middle nurturing touches provides a holistic representation of B2B purchase loops.
3.  **Window functions enable click indexing**: Running `ROW_NUMBER()` and `COUNT()` partitioned by `user_id` inside SQL CTEs is the most performant method to identify first and last touches sequentially before applying weights.

---

## 💻 Script Verification

I ran the `Code/attribution_engine.py` script to test multi-touch weight distributions and channel ROI calculations.
*   **Result**: 
    *   *Google*: First Touch = $12,000, Last Touch = $7,000, Linear = $7,833.33, U-Shaped = $8,500.00.
    *   *LinkedIn*: First Touch = $5,000, Last Touch = $10,000, Linear = $5,833.33, U-Shaped = $6,500.00.
    *   *Email*: First Touch = $0, Last Touch = $0, Linear = $3,333.33, U-Shaped = $2,000.00.
    *   *Attribution Variance*: Google Ads shifted from $7,000 under Last-Touch to $8,500 under U-Shaped, demonstrating how single-touch models ignore Google's top-of-funnel value.
*   **Insight**: This proves how multi-touch attribution changes ad-spend ROI decisions for marketing teams.

---

## 🎯 Plan for Tomorrow
Tomorrow is Day 36: **Data Quality & Auditing**. I will focus on schema validations, check constraints, handling missing values, duplicate detection, and writing database cleaning scripts.
