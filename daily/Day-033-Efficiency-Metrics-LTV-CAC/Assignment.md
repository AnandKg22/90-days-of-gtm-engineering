# Project Assignment - Day 033: LTV:CAC & Payback Calculator

This project requires developing a Python GTM Efficiency Calculator. It parses ad network campaign spend and acquired deal datasets, aggregates totals by marketing channel, computes blended CAC, calculates Gross Margin LTV, evaluates LTV:CAC ratios and payback periods, and outputs GTM channel ROI recommendations.

---

## 🎯 Requirements

Your Python application must:
1.  Define two datasets:
    *   `marketing_spend`: A list of spend events containing `channel` and `amount_spent`.
    *   `acquired_deals`: A list of won accounts containing `customer_id`, `annual_value`, `channel`.
2.  Implement **CAC Calculations**:
    *   Group spend and acquired counts by channel (`google`, `linkedin`, `email`).
    *   Calculate CAC for each channel: $\text{CAC} = \frac{\text{Total Spend}}{\text{Total Customers Acquired}}$.
3.  Implement **LTV Calculations**:
    *   For each channel, calculate LTV using a constant **80.0% Gross Margin** and **12.0% Annual Churn Rate**:
        *   $\text{LTV} = \frac{\text{Average Annual Contract Value} \times 0.80}{0.12}$.
4.  Implement **Efficiency Metrics**:
    *   `LTV:CAC Ratio`: $\frac{\text{LTV}}{\text{CAC}}$.
    *   `CAC Payback Period (Months)`: $\frac{\text{CAC}}{\text{Average Monthly Value} \times 0.80}$.
5.  Implement **ROI Alerts**:
    *   If `LTV:CAC < 3.0x`, log a warning: "Unprofitable channel. Reduce spend."
    *   If `Payback Period > 12.0 months`, log a warning: "Slow payback. High cash flow risk."
6.  Print the channel performance report table to the console.

---

## 💻 Deliverable Code

A complete, working efficiency metrics script has been created and placed in [Code/efficiency_metrics.py](Code/efficiency_metrics.py). It models the datasets, executes the financial calculations, and prints the tables.
