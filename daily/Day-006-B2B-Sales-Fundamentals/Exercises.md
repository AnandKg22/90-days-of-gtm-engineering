# Exercises - Day 006: Sales Pipeline Mapping

This document contains the mapped B2B sales pipeline stages and win probability parameters designed for VivaExams institutional contracts.

---

## 📊 VivaExams Sales Pipeline Stages

Each stage represents a deal checkpoint with specific entry criteria and associated win probabilities used for forecasting:

| Stage Name | Win Probability | Entry Criteria | System Action |
| :--- | :--- | :--- | :--- |
| **1. Discovery Scheduled** | 10% | Contact schedules a demo call (e.g. via Calendly). Deal record is created. | Create HubSpot Deal, set owner, log meeting details. |
| **2. Demo Completed** | 35% | Meeting takes place. Rep presents the VivaExams proctoring dashboard and cadet grading tools. | Log call transcript, update deal stage. |
| **3. Proposal Sent** | 60% | Client requests pricing. SOW and bulk licensing proposal are delivered. | Trigger SOW Proposal Generator, log sent date. |
| **4. Contract Review** | 85% | Client accepts terms. DocuSign agreement is sent to the Dean/Director for signature. | Trigger DocuSign envelope, notify AE in Slack. |
| **5. Closed Won** | 100% | DocuSign signed and initial invoice payment cleared via Stripe. | Trigger Stripe Invoice, provision cadet seats. |
| **6. Closed Lost** | 0% | Client cancels deal or declines proposal. Requires selecting a Lost Reason. | Log Lost Reason (e.g. Price, Competitor, No Budget). |

---

## 🔮 Forecasting Example Scenario

If we have three active deals in the pipeline:
1.  **Tolani Maritime Academy**: $10,000 in *Contract Review* (85% prob)
2.  **AMET University**: $20,000 in *Demo Completed* (35% prob)
3.  **IMSGOA Maritime College**: $5,000 in *Proposal Sent* (60% prob)

### 1. Unweighted Pipeline Value (Total Gross Pipeline)
$$Total = \$10,000 + \$20,000 + \$5,000 = \$35,000$$

### 2. Weighted Pipeline Value (Expected Forecast)
$$Weighted = (\$10,000 \times 0.85) + (\$20,000 \times 0.35) + (\$5,000 \times 0.60)$$
$$Weighted = \$8,500 + \$7,000 + \$3,000 = \$18,500$$

This weighted forecast tells the executive team that we can expect to close **$18,500** in contract revenue from our active pipeline.