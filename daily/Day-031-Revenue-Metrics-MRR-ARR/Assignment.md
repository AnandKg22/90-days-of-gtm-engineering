# Project Assignment - Day 031: Subscription MRR Waterfall Compiler

This project requires developing a Python Subscription MRR Waterfall Compiler. It parses raw subscription logs, groups them by month, categorizes events into waterfall buckets (New, Expansion, Contraction, Churn), calculates ending MRR and ARR run rates, and computes customer and revenue churn percentages.

---

## 🎯 Requirements

Your Python application must:
1.  Define a dataset of subscription events containing:
    *   `customer_id`, `event_type` (signup, upgrade, downgrade, cancel), `mrr_delta`, `date` (format: YYYY-MM-DD).
2.  Implement **Waterfall Categorization**:
    *   Group events by calendar month.
    *   Evaluate and sum values for:
        *   `New MRR`: Delta from `signup` events.
        *   `Expansion MRR`: Positive delta from `upgrade` events.
        *   `Contraction MRR`: Negative delta from `downgrade` events.
        *   `Churned MRR`: Negative delta from `cancel` events.
3.  Implement **Waterfall Calculations**:
    *   `Starting MRR` (corresponds to prior month's Ending MRR).
    *   `Net New MRR`: $\text{New} + \text{Expansion} - \text{Contraction} - \text{Churn}$.
    *   `Ending MRR` and `ARR Run Rate` (`Ending MRR * 12`).
4.  Implement **SaaS Churn Metrics**:
    *   `Customer Churn Rate (%)`: $\frac{\text{Cancelled Customers}}{\text{Starting Customers}} \times 100$.
    *   `Revenue Churn Rate (%)`: $\frac{\text{Churned MRR}}{\text{Starting MRR}} \times 100$.
5.  Print the step-by-step monthly waterfall tables to the console.

---

## 💻 Deliverable Code

A complete, working waterfall compiler script has been created and placed in [Code/revenue_metrics.py](Code/revenue_metrics.py). It models the logs, executes the financial calculations, and prints the tables.
