# Day 006: B2B Sales Fundamentals

## Objective
Understand B2B sales cycles and opportunity states, and model pipeline stage progression and probability-weighted revenue forecasting in CRMs.

## Topics Covered
- Pipeline deals
- Lead, Prospect, Opportunity
- Closed Won, Closed Lost

## Subtopics (Developed in Notes)
- The Sales Funnel
- Pipeline Stages
- Revenue Forecasting (Weighted Pipeline)

---

## 🛠️ Practical Exercise: VivaExams Sales Pipeline

In this exercise, we designed a B2B Sales Pipeline with six checkpoints, specifying entry criteria and win probability weights for VivaExams institutional contracts:
1.  **Discovery Scheduled** (10% prob): Scheduled demo call created in HubSpot.
2.  **Demo Completed** (35% prob): AE presents cadet proctoring tools.
3.  **Proposal Sent** (60% prob): SOW proposal delivered.
4.  **Contract Review** (85% prob): DocuSign agreement sent.
5.  **Closed Won** (100% prob): DocuSign signed and payment cleared.
6.  **Closed Lost** (0% prob): Opp cancelled (captures lost reason).

*View complete pipeline entry guidelines in [Exercises.md](Exercises.md).*

---

## 🏫 Daily Project / Assignment: Pipeline Kanban Simulator

We built an executable Python Kanban Board simulator in [Code/pipeline_kanban.py](Code/pipeline_kanban.py):
*   Tracks deal objects (`id`, `name`, `amount`, and `stage`).
*   Transitions opportunities across stages, displaying a clean CLI Kanban layout.
*   Calculates **Unweighted Gross Pipeline** (total pipeline value) and **Weighted Revenue Forecast** (deal amount * win probability %) to project closed ARR.

*View project requirements in [Assignment.md](Assignment.md) and the system diagram in [Architecture.md](Architecture.md).*

---

## 📂 Expected Deliverables
*   📝 [Day 6 Study Notes](Notes.md) — Pipeline stages and forecasting math.
*   📝 [Pipeline Target Models](Exercises.md) — VivaExams sales check points.
*   📝 [Kanban Board Spec](Assignment.md) — Project requirements.
*   📊 [Forecasting Diagram](Architecture.md) — Webhook-to-database forecast update flow.
*   💻 [Kanban Board Simulator](Code/pipeline_kanban.py) — Executable CRM dashboard program.

---

## 📝 Notes & Reflection
*   **Key Insight**: Implementing automated CRM webhook alerts when a deal moves to "Contract Review" (85% win probability) lets the customer success team prepare onboarding workspaces ahead of time.
*   **Study Log**: Read notes in [Notes.md](Notes.md).
*   **Daily Log**: Read reflections in [Reflection.md](Reflection.md).
