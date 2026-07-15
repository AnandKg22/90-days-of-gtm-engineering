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

## 🛠️ Practical Exercise: IMSGOA Admission Journey

In this exercise, we mapped the specialized, DGS-compliant customer journey for the **Institute of Maritime Studies Goa (IMSGOA)**:
1.  **Inquiry**: Cadet downloads the prospectus (Lead).
2.  **Shortlist**: Passes eligibility checks, technical exams, and interviews (SQL).
3.  **Enrollment**: Completes medical tests, receives ship sponsorship, and pays fees (Customer).
4.  **Alumni**: Cadet completes Pre-Sea, sails for 18 months, and returns to IMSGOA for advanced MEO competency prep courses (Renewal).

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
*   📝 [IMSGOA Journey Outline](Exercises.md) — Detailed maritime cadet mapping.
*   📝 [State Machine Specification](Assignment.md) — Project requirements.
*   📊 [State Engine Diagram](Architecture.md) — Telemetry-to-database webhook architecture.
*   💻 [State Machine Script](Code/journey_board.py) — Executable pipeline tracker.

---

## 📝 Notes & Reflection
*   **Key Insight**: Explicit state machine rules prevent pipeline data pollution in the CRM, while intent triggers identify hot prospects for outbound sales.
*   **Study Log**: Read notes in [Notes.md](Notes.md).
*   **Daily Log**: Read reflections in [Reflection.md](Reflection.md).
