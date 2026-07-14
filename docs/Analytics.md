# Revenue, Funnel & Cohort Analytics

Measuring business health requires tracking leading, lagging, and pipeline conversion metrics in custom dashboards.

---

## 1. Funnel Analytics (Conversion Rates)

A SaaS sales funnel requires monitoring conversion rates at each transition:

```
[Website Visit] ──> [10% Signup] ──> [MQL] ──> [30% Demo Booked] ──> [SQL] ──> [20% Closed Won]
```

### Funnel Metrics Definitions

*   **TOFU (Top of Funnel)**: Unique visitors, signups, free trial accounts.
*   **MOFU (Middle of Funnel)**: Product activations, demo bookings, proposal downloads.
*   **BOFU (Bottom of Funnel)**: Trial conversions, contract negotiations, closed deals.
*   **Conversion Rate**:
    $$Conversion \; Rate \% = \frac{Converted \; Leads}{Total \; Leads} \times 100$$

---

## 2. Revenue Attribution Models

Attribution defines which marketing channels get credit for a closed deal.

```
Touchpoints:  [Ad Click] ──> [Ebook Download] ──> [Demo Request] ──> [Closed Won]
```

1.  **First-Touch**: Gives 100% of the deal credit to the channel that drove the initial click (`Ad Click`).
2.  **Last-Touch**: Gives 100% of the credit to the final channel (`Demo Request`).
3.  **Linear**: Distributes credit equally across all touchpoints ($33\%$ each).
4.  **U-Shaped / Position-Based**: Gives $40\%$ to first touch, $40\%$ to last touch, and distributes the remaining $20\%$ among the middle touches.

---

## 3. Leading vs. Lagging Indicators

*   **Lagging Indicators (Historical)**:
    *   ARR, MRR, expansion revenue, logo churn, net revenue retention.
*   **Leading Indicators (Predictive)**:
    *   Weekly active users (WAU), pipeline value added, new demo request volume, email response rates, SLA response speeds.
