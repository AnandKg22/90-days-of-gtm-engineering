# Reflection - Day 030: Cohort Analysis

A personal log reflecting on the learning outcomes and concepts mastered on Day 30.

---

## 💡 Key Takeaways & Lessons Learned

1.  **Retention is the ultimate SaaS metric**: A company can acquire 1,000 new users weekly, but if cohort analysis shows 0% retention in Month 1, the business will fail due to churn. Cohorts track true product market fit.
2.  **Stickiness (DAU/MAU) measures daily habit formation**: High stickiness ratios (>20%) indicate that the application is integrated into the user's daily work habit. Lower ratios indicate a casual, utility product.
3.  **Optimize log joins with index keys**: Calculating first-action timestamps dynamically across raw logs is a database bottleneck. Pre-compiling signup dates in a dimension table and index-matching them speeds up queries.

---

## 💻 Script Verification

I ran the `Code/cohort_analysis.py` script to test cohort weekly grouping, delta calculations, and stickiness ratios.
*   **Result**: 
    *   *Cohort Week 1 (3 users)*: Week 0 = 100%, Week 1 = 66.7% (2 users), Week 2 = 66.7% (2 users), Week 3 = 33.3% (1 user).
    *   *Cohort Week 2 (2 users)*: Week 0 = 100%, Week 1 = 50.0% (1 user), Week 2 = 50.0% (1 user), Week 3 = 0.0%.
    *   *Product Stickiness*: On target peak date `2026-07-08`, recorded 2 DAU out of 5 total MAU, giving a **40.0% stickiness ratio** (above the 20% target).
*   **Insight**: This verifies how cohort grids identify onboarding drops and measure customer habits.

---

## 🎯 Plan for Tomorrow
Tomorrow is Day 31: **Revenue Metrics (MRR, ARR)**. I will focus on understanding Monthly Recurring Revenue, Annual Recurring Revenue, expansion MRR, churned MRR, and mapping subscription upgrades to finance charts.
