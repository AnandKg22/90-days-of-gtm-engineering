# Reflection - Day 031: Revenue Metrics

A personal log reflecting on the learning outcomes and concepts mastered on Day 31.

---

## 💡 Key Takeaways & Lessons Learned

1.  **MRR must be broken into granular waterfall buckets**: Simply measuring total MRR growth masks underlying retention problems. For example, if you add $5,000 in New MRR but lose $5,000 in Churned MRR, your business is flat, indicating a major product churn issue.
2.  **SaaS valuations run on ARR**: Annual Recurring Revenue (ARR) is the key metric used by investors and executives to value a company. It is calculated by multiplying the current month's ending MRR by 12.
3.  **Audit subscription state logs historically**: Transactional databases only show the current state of a contract (e.g. "Active"). GTM Engineers must design history tables to capture state changes, enabling historical MRR reporting.

---

## 💻 Script Verification

I ran the `Code/revenue_metrics.py` script to test MRR waterfall grouping, ARR run rates, and customer/revenue churn rates.
*   **Result**: 
    *   *Month 1 (July 2026)*: Starting MRR = $0.00, New MRR = $5,000.00, Expansion = $300.00. Ending MRR = $5,300.00. ARR Run Rate = $63,600.00. Churn rates = 0.0%.
    *   *Month 2 (August 2026)*: Starting MRR = $5,300.00, New MRR = $3,000.00, Contraction = $500.00, Churned = $1,500.00. Net New MRR = +$1,000.00. Ending MRR = $6,300.00. ARR = $75,600.00.
    *   *August Churn Rates*: Customer Churn = 33.3% (1 out of 3 customers cancelled), Revenue Churn = 28.3% (lost $1,500 of $5,300 starting MRR), triggering a revenue churn warning.
*   **Insight**: This verifies how subscription delta calculations isolate churn problems and track financial health.

---

## 🎯 Plan for Tomorrow
Tomorrow is Day 32: **Expansion Metrics (NDR, GRR)**. I will focus on Net Dollar Retention, Gross Dollar Retention, expansion campaigns, upsells, and cross-sells.
