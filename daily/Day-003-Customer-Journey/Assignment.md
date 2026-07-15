# Project Assignment - Day 003: Journey Mapping Board

This project requires creating an automated pipeline tracker that consumes user activity logs and evaluates their current lifecycle stage based on predefined business rules.

---

## 🎯 Requirements

Your Python simulation must:
1.  Track individual customer profiles by `user_id`.
2.  Consume a chronological list of user telemetry events.
3.  Implement a lifecycle state machine that transitions the user across:
    `Visitor ──> Lead ──> SQL ──> Opportunity ──> Customer`
4.  Trigger system alerts when high-value events occur (e.g., when a lead visits `/pricing`, trigger a Slack warning to sales).

---

## 📂 System Rules

Your pipeline engine must evaluate events against these conditions:
*   **Visitor**: Default state when a profile starts (logs page views).
*   **Lead**: Transition when user performs `form_signup` (capturing email).
*   **SQL (Sales Qualified)**: Transition when user profile is enriched and company employee count is greater than 50.
*   **Opportunity**: Transition when user triggers `demo_booked` or `sales_call_scheduled`.
*   **Customer**: Transition when user triggers `payment_confirmed` (from Stripe).

---

## 💻 Deliverable Code

A complete, working simulation script has been developed and placed in [Code/journey_board.py](Code/journey_board.py). It models these transitions on mock customer events and prints a step-by-step trace of the sales pipeline state changes.