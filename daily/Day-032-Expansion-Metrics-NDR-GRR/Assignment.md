# Project Assignment - Day 032: Cohort NDR & GRR Calculator

This project requires developing a Python Cohort NDR & GRR Calculator. It processes starting cohort lists and year-end contract snapshots, categorizes contract changes into expansion/contraction/churn buckets, computes NDR and GRR ratios, and logs GTM cohort health alerts.

---

## 🎯 Requirements

Your Python application must:
1.  Define a cohort database list of records containing:
    *   `company_id`, `start_mrr`, `end_mrr`.
2.  Implement **Contract Change Categorization**:
    *   Compare `end_mrr` to `start_mrr` for each record and aggregate:
        *   `Expansion MRR`: Sum of positive differences (`end_mrr - start_mrr`).
        *   `Contraction MRR`: Sum of negative differences for partially retained accounts (`start_mrr - end_mrr`).
        *   `Churned MRR`: Sum of starting MRR for accounts that cancelled (`end_mrr = 0`).
3.  Implement **Retention Calculations**:
    *   `Net Dollar Retention (NDR) %`: $\frac{\text{Start MRR} + \text{Expansion} - \text{Contraction} - \text{Churn}}{\text{Start MRR}} \times 100$.
    *   `Gross Dollar Retention (GRR) %`: $\frac{\text{Start MRR} - \text{Contraction} - \text{Churn}}{\text{Start MRR}} \times 100$.
4.  Implement **Cohort Health Alerts**:
    *   If `NDR < 100.0%`, log a warning: "Failing to expand existing base. Churn outpaces upsells."
    *   If `GRR < 80.0%`, log a critical alert: "Unstable customer base. High cancellation risk."
5.  Print the cohort summary metrics and retention report to the console.

---

## 💻 Deliverable Code

A complete, working cohort metrics script has been created and placed in [Code/expansion_metrics.py](Code/expansion_metrics.py). It models the logs, executes the retention math, and prints the tables.
