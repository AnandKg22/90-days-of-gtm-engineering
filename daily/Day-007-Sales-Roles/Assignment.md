# Project Assignment - Day 007: Sales Org Hand-off Tracker

This project requires developing a Python simulation that maps sales organization roles (SDRs, AEs, CSMs) and logs customer data ownership hand-offs sequentially.

---

## 🎯 Requirements

Your Python simulation must:
1.  Define commercial team members with roles: `SDR`, `AE`, and `CSM`.
2.  Model a prospect record containing: `id`, `name`, `assigned_sdr`, `assigned_ae`, `assigned_csm`, `stage`, and a history list.
3.  Implement a hand-off pipeline that executes:
    *   **Phase 1: Qualification**: SDR qualifies the lead, shifting the stage to `Meeting Booked` and transferring lead ownership to the assigned AE.
    *   **Phase 2: Closed Won**: AE wins the deal, shifting the stage to `Closed Won` and transferring account onboarding ownership to the assigned CSM.
4.  Log timestamps and generate mock notifications (Slack alerts/emails) at each hand-off point.

---

## 💻 Deliverable Code

A complete, working simulation script has been created and placed in [Code/org_chart.py](Code/org_chart.py). It models the roles, tracks prospect state records, and outputs a formatted transition log.