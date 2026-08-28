# Project Assignment - Day 034: Funnel Conversion & Velocity Analyzer

This project requires developing a Python Funnel Conversion & Velocity Analyzer. It parses CRM stage log histories, groups transition intervals per deal, calculates the average days spent in each stage (Funnel Velocity), and computes step-by-step stage conversion percentages.

---

## 🎯 Requirements

Your Python application must:
1.  Define a dataset of CRM stage logs containing:
    *   `deal_id`, `stage` (Lead, MQL, SQL, Opportunity, Won), `date` (format: YYYY-MM-DD).
2.  Implement **Stage Transition Parsing**:
    *   For each unique `deal_id`, sort events by date to reconstruct their stage progression.
    *   Calculate the elapsed days spent in each stage before progressing to the next:
        *   `Days in Stage = date(next_stage) - date(current_stage)`.
3.  Implement **Funnel Velocity Ratios**:
    *   For each stage, calculate the average number of days spent before moving forward.
4.  Implement **Conversion Rate Calculations**:
    *   Count the total unique deals that reached each stage.
    *   Calculate:
        *   `Lead-to-MQL Conversion %`
        *   `MQL-to-SQL Conversion %`
        *   `SQL-to-Opportunity Conversion %`
        *   `Opportunity-to-Won Conversion %`
        *   `Overall Funnel Conversion %` (Lead-to-Won).
5.  Print the funnel conversion percentages and velocity tables to the console.

---

## 💻 Deliverable Code

A complete, working funnel metrics script has been created and placed in [Code/funnel_analyzer.py](Code/funnel_analyzer.py). It models the logs, executes the retention and speed math, and prints the tables.
