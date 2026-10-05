# Study Notes - Day 048: AI Customer Success (Retention & Health)

Today's studies focused on Customer Success (CS) engineering, calculating Customer Health Scores (CHS), tracking Net Revenue Retention (NRR), setting up automated escalation alerts for churn-risk accounts, and identifying expansion opportunities.

---

## 1. Customer Health Score (CHS) Modeling

A **Customer Health Score (CHS)** is a multi-dimensional metric that indicates the likelihood of a customer renewing their subscription:

### CHS Formula Framework:
We model a 100-point scale:
1.  **Product Adoption Rate (60% weight)**: Seat usage or compute credit consumption (e.g. 90% seat utilization = 54 points).
2.  **Onboarding Status (15% weight)**: Confirms the core setup milestones have been completed (Completed = 15 points, Incomplete = 0 points).
3.  **Support Ticket Sentiment (25% weight)**: Evaluates customer friction. Subtracts 5 points per active open ticket.

### Health Score Tiers:
*   **Green ($\ge 80$)**: Healthy account. Low churn risk; target for expansion/upsell.
*   **Yellow ($50 - 79$)**: Stable account. Watch for onboarding delays or stagnant usage.
*   **Red ($< 50$)**: High churn risk. Requires immediate human-in-the-loop escalation.

---

## 2. Retention Metrics: NRR & GRR

Customer Success teams are measured on two primary revenue retention metrics:

### 1. Gross Revenue Retention (GRR)
Measures the percentage of recurring revenue retained from existing customers, excluding expansion:
$$\text{GRR} = \frac{\text{Ending ARR} - \text{Expansion ARR}}{\text{Starting ARR}} \times 100\%$$
*Note*: GRR can never exceed 100%.

### 2. Net Revenue Retention (NRR)
Measures the total recurring revenue retained from existing customers, including expansion, cross-sells, and upgrades:
$$\text{NRR} = \frac{\text{Starting ARR} + \text{Expansion} - \text{Downgrades} - \text{Churn}}{\text{Starting ARR}} \times 100\%$$
*Note*: A healthy B2B enterprise SaaS company target is $\text{NRR} > 110\%$.

---

## 3. Churn Mitigation & Escalation Rules

When an account enters the **Red Tier** (Health $< 50$):
*   **Internal Warning**: Trigger webhooks pushing critical alerts containing CSM assignments and health scores to internal Slack channels.
*   **CRM Task Log**: Create high-priority review tasks in the CRM.
*   **Stakeholder Outreach**: Generate draft email outreach for the CSM to coordinate a technical review call.
*   **Support Priority**: Escalate their open tickets to high-priority queues.
