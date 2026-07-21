# Project Assignment - Day 010: Pipeline Velocity & Currency Tracker

This project requires developing a Python sales analytics script that tracks deal stage transitions, calculates velocity durations, and normalizes multi-currency values to base USD.

---

## 🎯 Requirements

Your Python simulation must:
1.  Define a deal record containing: `id`, `name`, `local_amount`, `currency_code` (INR, SGD, USD), and `stage`.
2.  Maintain a transition history log recording: `stage_name`, `entered_at` (timestamp), and `exited_at` (timestamp).
3.  Implement methods to:
    *   Transition a deal's stage (setting the previous stage's exit timestamp and the new stage's enter timestamp).
    *   Calculate **Pipeline Velocity** (duration spent in each stage).
    *   Normalize local deal amounts to base USD.
4.  Print a clean pipeline analysis report showing currency conversions and stage durations.

---

## 💻 Deliverable Code

A complete, working simulation script has been created and placed in [Code/pipeline_transitions.py](Code/pipeline_transitions.py). It models these stage transitions, simulates time intervals, and outputs the velocity metrics console.
