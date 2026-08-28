# Exercises - Day 034: Sales Funnel Conversion Charts

This document details the Sales Funnel Conversion Rate Grid and velocity definitions used to audit prospect progression.

---

## 📊 Sales Funnel Conversion Rate Matrix

This grid displays the progression counts and conversion rates across the B2B SaaS buyer journey:

| Funnel Stage | Volume (Accounts) | Overall Funnel Conversion | Stage-to-Stage Conversion | Stage Target Description |
| :--- | :--- | :--- | :--- | :--- |
| **`Lead`** | `1,000` | `100.0%` | `100.0%` | Initial website demo registration. |
| **`MQL`** | `300` | `30.0%` | **`30.0%`** (Lead ──> MQL) | Marketing Qualified: downloads syllabus. |
| **`SQL`** | `150` | `15.0%` | **`50.0%`** (MQL ──> SQL) | Sales Qualified: booked call with AE. |
| **`Opportunity`**| `60` | `6.0%` | **`40.0%`** (SQL ──> Opp) | Active negotiation; proposal dispatched. |
| **`Closed Won`** | `15` | `1.5%` | **`25.0%`** (Opp ──> Won) | Contract signed; Stripe invoice settled. |

---

## ⚙️ Funnel Velocity Metrics

In addition to conversion percentages, we track the speed of transitions:

1.  **Lead to MQL Lag**: Speed of marketing nurturing (target: `< 2 days`).
2.  **MQL to SQL Lag**: Speed of SDR outreach and booking (target: `< 5 days`).
3.  **SQL to Opportunity Lag**: Speed of AE qualification checks (target: `< 7 days`).
4.  **Opportunity to Closed Won Lag**: Negotiation and procurement cycle times (target: `< 30 days`).
5.  **Total Conversion Cycle Time**: Sum of all transition lags from initial Lead creation to final Won payment.
