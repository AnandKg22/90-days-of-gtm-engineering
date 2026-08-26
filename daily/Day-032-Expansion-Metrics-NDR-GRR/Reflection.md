# Reflection - Day 032: Expansion Metrics

A personal log reflecting on the learning outcomes and concepts mastered on Day 32.

---

## 💡 Key Takeaways & Lessons Learned

1.  **NDR measures net growth from existing cohorts**: A healthy B2B SaaS business aims for NDR > 100%. This indicates that upsells (Expansion MRR) outpace contraction and cancellations, meaning the company can double its revenue even without acquiring a single new customer.
2.  **GRR acts as the baseline floor**: Unlike NDR, Gross Dollar Retention (GRR) cannot exceed 100%. It measures baseline stability. If NDR is 120% but GRR is 60%, the business is highly unstable—you are losing customers rapidly but masking it by heavily upselling the survivors. Both metrics must be audited together.
3.  **Snapshot schemas isolate cohort states**: Transactional DBs overwrite customer fields. Capturing monthly snapshots of active MRR per account is mandatory to run date-interval queries.

---

## 💻 Script Verification

I ran the `Code/expansion_metrics.py` script to test cohort retention math and health alert logs.
*   **Result**: 
    *   *Starting Cohort MRR*: $56,000.00.
    *   *Ending Cohort MRR*: $43,000.00.
    *   *SaaS Ratios*: NDR calculated at **76.8%** and GRR at **73.2%**.
    *   *Alert Triggers*: Successfully logged a critical warning (`GRR is unstable (< 80.0%)`) and an NDR warning (`NDR is failing (< 100.0%)`) due to the cancellations of Global Shipping ($8,000) and Pacific Transit ($4,000).
*   **Insight**: This proves that our calculator catches high churn risks before they impact next-year forecasts.

---

## 🎯 Plan for Tomorrow
Tomorrow is Day 33: **Efficiency Metrics (LTV:CAC)**. I will focus on Customer Acquisition Cost (CAC), Lifetime Value (LTV), payback period calculations, and mapping marketing spends to sales velocities.
