# Project Assignment - Day 006: Pipeline Kanban Board

This project requires developing a Python sales pipeline simulation that acts as an in-memory CRM Kanban Board, tracking opportunities and rendering forecasting statistics.

---

## 🎯 Requirements

Your Python simulation must:
1.  Model a B2B deal object with fields: `id`, `name`, `amount`, and `stage`.
2.  Define pipeline stages with associated win probabilities:
    *   `Discovery`: 10%
    *   `Demo`: 35%
    *   `Proposal`: 60%
    *   `Legal`: 85%
    *   `Won`: 100%
    *   `Lost`: 0%
3.  Implement methods to:
    *   Add a deal.
    *   Move a deal's stage.
    *   Print an ASCII layout of the Kanban Board, grouping deals by stage.
    *   Compute the **Total Pipeline Value** (unweighted sum) and the **Weighted Revenue Forecast** (weighted sum).

---

## 💻 Deliverable Code

A complete, working simulation script has been created and placed in [Code/pipeline_kanban.py](Code/pipeline_kanban.py). It implements these requirements, runs a series of deal status updates, and outputs a formatted forecast summary.