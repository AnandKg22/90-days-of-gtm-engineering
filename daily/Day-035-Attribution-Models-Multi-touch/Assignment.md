# Project Assignment - Day 035: Multi-Touch Attribution Engine

This project requires developing a Python Multi-Touch Attribution Engine. It processes ad campaign touchpoint logs and won deal conversions, implements First Touch, Last Touch, Linear, and U-Shaped (40/20/40) credit allocation algorithms, and outputs a comparative revenue matrix across marketing channels.

---

## 🎯 Requirements

Your Python application must:
1.  Define two datasets:
    *   `campaign_clicks`: A log of click touchpoints containing `user_id`, `channel`, `date` (format: YYYY-MM-DD).
    *   `won_conversions`: A list of conversions containing `user_id`, `revenue`.
2.  Implement **Click Sequence Sorting**:
    *   For each converted `user_id`, retrieve all their clicks and sort them chronologically to determine their touchpoint sequence.
3.  Implement **Attribution Models**:
    *   **First Touch**: Allocate 100% of the deal's `revenue` to the first click's channel.
    *   **Last Touch**: Allocate 100% of the deal's `revenue` to the last click's channel.
    *   **Linear**: Split the `revenue` equally among all clicks in the sequence.
    *   **U-Shaped (Position-Based)**: 
        *   If 1 touchpoint: 100% credit to that channel.
        *   If 2 touchpoints: 50% credit to first, 50% to last.
        *   If 3 or more: 40% to first, 40% to last, and 20% distributed equally to all middle touchpoints.
4.  Aggregate and print the total revenue credited to each channel (`google`, `linkedin`, `email`) under all four models.

---

## 💻 Deliverable Code

A complete, working attribution engine script has been created and placed in [Code/attribution_engine.py](Code/attribution_engine.py). It models the logs, executes the allocation algorithms, and prints the tables.
