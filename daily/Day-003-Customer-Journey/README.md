# Day 003: Customer Journey

## Objective
Understand user progression through the lifecycle stages, and learn how to track customer touchpoints, buyer intent signals, and B2B committee decision-making.

## Topics Covered
- Awareness
- Interest
- Consideration
- Evaluation
- Purchase
- Onboarding
- Adoption
- Expansion

## Subtopics
- Customer touchpoints
- Buyer intent
- Decision making

---

## 🛠️ Practical Exercise: CloudSentry Customer Journey

In this exercise, we mapped the B2B SaaS customer journey for **CloudSentry** (an AI-powered cloud cost optimization and compliance platform):
1.  **Inquiry**: Lead signs up for a trial account or downloads a cloud security checklist (Lead).
2.  **Qualification**: Lead profile is enriched and identified as a mid-market organization with AWS integration needs (SQL).
3.  **Evaluation**: Lead schedules an enterprise demo or sets up a cloud integration sandbox (Opportunity).
4.  **Enrollment**: Customer signs an annual service contract and pays the initial subscription invoice (Customer).
5.  **Retention & Growth**: Customer integrates additional multi-cloud workloads and upgrades to the premium compliance module (Expansion).

*View the complete mapping stages in [Exercises.md](Exercises.md).*

---

## 🏫 Daily Project / Assignment: Journey Mapping Board

We built an automated state-machine engine in [Code/journey_board.py](Code/journey_board.py) to track user lifecycles:
*   Processes streams of telemetry events (page views, signups, payments).
*   Triggers active alerts when high-intent touchpoints occur (such as a lead visiting the `/pricing` page).
*   Controls strict transition thresholds to advance prospects automatically (`Visitor -> Lead -> SQL -> Opportunity -> Customer`).

*View the project requirements in [Assignment.md](Assignment.md) and the system diagram in [Architecture.md](Architecture.md).*

---

## 📂 Expected Deliverables
*   📝 [Day 3 Study Notes](Notes.md) — Insights on touchpoints, intent, and buying committees.
*   📝 [CloudSentry Journey Outline](Exercises.md) — Detailed SaaS customer mapping.
*   📝 [State Machine Specification](Assignment.md) — Project requirements.
*   📊 [State Engine Diagram](Architecture.md) — Telemetry-to-database webhook architecture.
*   💻 [State Machine Script](Code/journey_board.py) — Executable pipeline tracker.

---

## 📝 Notes & Reflection
*   **Key Insight**: Explicit state machine rules prevent pipeline data pollution in the CRM, while intent triggers identify hot prospects for outbound sales.
*   **Study Log**: Read notes in [Notes.md](Notes.md).
*   **Daily Log**: Read reflections in [Reflection.md](Reflection.md).
