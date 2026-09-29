# Project Assignment - Day 047: Proposal Automation Tool

This project requires developing a Python Proposal Automation Tool. It compiles customized business proposals including scopes of work, pricing schedules, ROI calculations, and approval workflows.

---

## 🎯 Requirements

Your Proposal Tool must:
1.  **Map Pricing Tiers**:
    *   *Enterprise Tier*: $95k/yr software license + $15k implementation setup fee.
    *   *Mid-Market Tier*: $45k/yr software license + $7.5k implementation setup fee.
2.  **Generate Dynamic Scopes of Work (SOW)**:
    *   Include Phase 1 (API connection), Phase 2 (Schema mapping), and Phase 3 (Shadow testing) steps tailored to the prospect's technology stack.
3.  **Perform ROI Calculations**:
    *   Calculate annual operational losses based on the customer's wasted hours and labor rate.
    *   Calculate Year 1 net savings and ROI percentages relative to the software contract value.
4.  **Enforce Discount Compliance Gates**:
    *   If the requested discount exceeds 20.0%, route the proposal's approval status to "PENDING VP APPROVAL".
    *   If the requested discount is under 20.0% but above 0%, mark it "APPROVED BY SALES DIRECTOR".
    *   If no discount is requested, mark it "AUTO-APPROVED".
5.  **Output Structured Reports**:
    *   Format proposals as professional text documents containing executive overviews, SOW phases, commercial terms, ROI models, and approval statuses.

---

## 💻 Deliverable Code

A complete, working Proposal Automation Tool has been created and is available in [Code/proposal_generator.py](Code/proposal_generator.py). It runs proposal compilations on Stark Industries, Wayne Enterprises, and Cyberdyne Systems.