# Project Assignment - Day 029: Looker Data Blender & Join Engine

This project requires developing a Python simulator that models Looker Studio's client-side data blending engine. It executes Inner Joins and Left Outer Joins on disjoint GTM datasets, audits records for data loss, and compares browser-side join speeds against pre-compiled warehouse tables.

---

## 🎯 Requirements

Your Python application must:
1.  Define two disjoint datasets:
    *   `hubspot_contacts` (keys: `email`, `lead_source`).
    *   `stripe_payments` (keys: `customer_email`, `amount_usd`).
2.  Implement an **Inner Joiner**:
    *   `inner_join()`: Merge records on `email == customer_email`, discarding unmatched rows.
3.  Implement a **Left Outer Joiner**:
    *   `left_outer_join()`: Merge records while retaining all contacts, filling missing payment amounts with `None`.
4.  Implement a **Data Completeness Auditor**:
    *   Log total contact counts from both join methods. Explain why Inner Joins bias conversion rate calculations.
5.  Implement a **Performance Auditor**:
    *   Compare the speed of joining tables in memory (simulating client-side browser blending) against querying a pre-joined database view.

---

## 💻 Deliverable Code

A complete, working data blender script has been created and placed in [Code/data_blender.py](Code/data_blender.py). It models the datasets, executes the joins, and outputs the performance analysis.
