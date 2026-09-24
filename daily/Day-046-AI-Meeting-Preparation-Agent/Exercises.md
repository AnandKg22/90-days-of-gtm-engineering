# Exercises - Day 046: Discovery & Persona Analysis

This document details practical exercises on designing stakeholder persona profiles and SPIN discovery scripts.

---

## 📋 Exercise 1: Multi-Stakeholder Map

### Scenario:
You are selling an enterprise database synchronization platform to **Wayne Enterprises**.
Map the motivations and concerns of the three key buying roles:

### Solution Matrix:
1.  **Lucius Fox (CEO / Business Operations Lead)**:
    *   *Motivation*: API security, reducing maintenance overhead, developer experience.
    *   *Objection*: "We have internal developers. We can build a custom database sync ourselves."
    *   *Reframing*: Highlight the opportunity cost of developer time and the ongoing API maintenance burden.
2.  **Alfred Pennyworth (Chief Finance Director)**:
    *   *Motivation*: Budget control, billing accuracy, ROI within 90 days.
    *   *Objection*: "A custom internal script costs us nothing upfront, while your subscription is $120k/yr."
    *   *Reframing*: Detail manual sync errors and payment leakage costs, which average 2-4% of total ARR.
3.  **Bruce Wayne (Chairman / Sponsor)**:
    *   *Motivation*: Strategic scale and operational efficiency.
    *   *Objection*: "How does this scale across our global subsidiaries?"
    *   *Reframing*: Showcase multi-tenant cloud sync endpoints (AWS/GCP) and unified compliance portals.

---

## ⚙️ Exercise 2: Building SPIN Questions for Stark Industries

### Scenario:
Stark Industries uses GCP, Snowflake, and custom billing scripts. They face lead routing delays and invoice sync gaps.

### SPIN Question Compilation:
*   **Situation Question**:
    *   "How are your custom scripts currently syncing customer lead scores in Snowflake back to the GCP database?"
*   **Problem Question**:
    *   "When custom sync scripts fail or lag, how does your sales operations team identify which records failed?"
*   **Implication Question**:
    *   "If an invoice sync gap causes a billing delay, what is the impact on your cash flow and customer satisfaction?"
*   **Need-Payoff Question**:
    *   "If we replaced custom billing scripts with a native, automated sync that runs in under 30 seconds, how much developer time would that save your engineering team weekly?"