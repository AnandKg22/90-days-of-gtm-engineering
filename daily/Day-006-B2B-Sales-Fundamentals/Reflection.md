# Reflection - Day 006: B2B Sales Fundamentals

A personal log reflecting on the learning outcomes and concepts mastered on Day 6.

---

## 💡 Key Takeaways & Lessons Learned

1.  **Weighted Pipeline vs Gross Pipeline**: Executives do not rely on Gross Pipeline (which is just the sum of all deals), because not all deals close. The only way to predict hiring budgets and dry-dock investments is through **Weighted Revenue Forecasting** (summing deal value multiplied by probability).
2.  **Explicit CRM Stages prevent Pipeline Inflation**: Sales reps naturally feel optimistic and might mark early-stage deals as "near won." Defining strict entry criteria for each stage (e.g. *Proposal Sent* requires uploading the SOW document to the deal record) keeps the pipeline data honest.
3.  **Webhook Sync speeds up Operations**: Waiting for a daily batch sync of sales deals is too slow. Real-time webhooks (such as `deal.stage_change`) are required to trigger instant provisioning and alerts.

---

## 💻 Script Verification

I ran the `Code/pipeline_kanban.py` script to test our Kanban Board and forecasting logic.
*   **Result**: 
    *   *Initial State*: Gross pipeline: $35,000.00. Expected forecast: $11,000.00. (AMET in Demo was weighted at $7,000, IMSGOA in Proposal at $3,000, Tolani in Discovery at $1,000).
    *   *After Updates*: Gross pipeline: $35,000.00. Expected forecast: $30,250.00. (AMET was Won at $20,000, IMSGOA in Legal at $4,250, Tolani in Proposal at $6,000).
*   **Insight**: Winning a deal shifts it to 100% weight, immediately increasing the recognized forecast. Shifting other deals forward increases their win probabilities, stabilizing our revenue expectations.

---

## 🎯 Plan for Tomorrow
Tomorrow is Day 7: **Sales Roles**. I will focus on understanding the operational hand-offs, workflows, and KPIs of SDRs, AEs, Customer Success, and RevOps.
