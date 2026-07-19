# Day 007: Sales Roles

## Objective
Understand commercial roles and responsibilities within a GTM organization (SDR, BDR, AE, SE, CS, RevOps, GTM), and design data-integrity hand-off pipelines that automate client record transfers between teams.

## Topics Covered
- SDR & BDR
- AE & Sales Engineer
- Customer Success
- RevOps & GTM Engineer

## Subtopics (Developed in Notes)
- Daily Activities & System Ownership
- Key Performance Indicators (KPIs)
- Customer Hand-off Workflows

---

## 🛠️ Practical Exercise: Commercial Information Flow

In this exercise, we mapped out the data hand-offs and transaction checkpoints between sales roles:
1.  **Lead creation**: Inbound contact added to HubSpot, assigned to SDR.
2.  **Meeting Booked**: SDR qualifies lead and shares AE's Calendly link. n8n creates a Deal, assigns AE owner, copies SDR notes, and routes Slack notification.
3.  **Onboarding**: AE wins deal. n8n creates a record in Customer Success, assigns CSM via round-robin, notifies CSM in Slack, and triggers customer welcome emails.

*View complete hand-off stages in [Exercises.md](Exercises.md).*

---

## 🏫 Daily Project / Assignment: Sales Org Hand-off Tracker

We built an executable Python simulation in [Code/org_chart.py](Code/org_chart.py) to audit the sales pipeline hand-off trail:
*   Maps roles and details (SDR Rohit, AE Sarah, CSM Amit).
*   Tracks deal ownership transfers from SDR to AE (upon qualification) and AE to CSM (upon Closed Won status).
*   Simulates automated notifications (Slack notifications to AEs and CSMs, client welcome emails) and prints a formatted, timestamped transaction log audit trail.

*View project requirements in [Assignment.md](Assignment.md) and the system diagram in [Architecture.md](Architecture.md).*

---

## 📂 Expected Deliverables
*   📝 [Day 7 Study Notes](Notes.md) — Roles definitions, KPIs, and hand-off frameworks.
*   📝 [Information Flow Outline](Exercises.md) — Step-by-step transaction mapping.
*   📝 [Hand-off Tracker Spec](Assignment.md) — Project requirements.
*   📊 [Sales Org Diagram](Architecture.md) — Systems boundaries and tools hierarchy.
*   💻 [Sales Org Tracker Script](Code/org_chart.py) — Executable hand-off simulation program.

---

## 📝 Notes & Reflection
*   **Key Insight**: Automating the transfer of AE qualification notes to the CSM dashboard eliminates redundant conversations for the customer, lowering customer friction during onboarding.
*   **Study Log**: Read notes in [Notes.md](Notes.md).
*   **Daily Log**: Read reflections in [Reflection.md](Reflection.md).
