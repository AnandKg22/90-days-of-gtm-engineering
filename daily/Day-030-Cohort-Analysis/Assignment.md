# Project Assignment - Day 030: Cohort Retention Analyzer

This project requires developing a Python Cohort Retention Analyzer. It processes raw user activity logs, determines cohort signup windows, groups subsequent engagements into weekly intervals, and compiles weekly retention matrix grids alongside DAU/MAU stickiness ratios.

---

## 🎯 Requirements

Your Python application must:
1.  Define a dataset of user activity logs containing:
    *   `user_id`, `event_name`, `event_date` (format: YYYY-MM-DD).
2.  Implement **Cohort Grouping**:
    *   Find the earliest `event_date` for each unique `user_id` to establish their signup cohort week.
3.  Implement **Retention Delta Calculations**:
    *   Calculate the weekly difference between subsequent user events and their cohort signup week:
        *   `Week Delta = (event_date - signup_date) // 7`
    *   Map these deltas to Week 0, Week 1, Week 2, and Week 3 buckets.
4.  Implement **Stickiness Metrics**:
    *   Calculate Daily Active Users (DAU) on a target peak date.
    *   Calculate Monthly Active Users (MAU) across the entire log.
    *   Output the Stickiness Ratio: `(DAU / MAU) * 100`.
5.  Format and print the final Cohort Weekly Retention Matrix showing percentages.

---

## 💻 Deliverable Code

A complete, working cohort analysis script has been created and placed in [Code/cohort_analysis.py](Code/cohort_analysis.py). It models the logs, executes the retention math, and prints the tables.
