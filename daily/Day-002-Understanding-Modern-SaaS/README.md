# Day 002: Understanding Modern SaaS

## Objective
Understand the SaaS subscription economics, recurring billing models, and the unit economics metrics governing SaaS companies.

## Topics Covered
- SaaS business model
- Subscription revenue
- ARR / MRR
- CAC / LTV
- Churn
- Payback period

## Subtopics
- Monthly billing
- Annual billing
- Gross revenue
- Net revenue
- Expansion revenue

---

## 🛠️ Practical Exercise: SaaS Metrics Calculation

In this exercise, we laid out the Excel database and formula models required to calculate core customer metrics:
*   **Active Subscriptions Count**: `=COUNTIF(Customers!D:D, "Active")`
*   **MRR (Monthly Recurring Revenue)**: `=SUMIF(Customers!D:D, "Active", Customers!C:C)`
*   **ARR (Annual Recurring Revenue)**: `=MRR * 12`
*   **Average CAC**: `=AVERAGE(Customers!E:E)`
*   **Logo Churn Rate**: `=COUNTIF(Customers!D:D, "Churned") / COUNTA(Customers!A:A)`
*   **LTV**: `=ARPU / Churn_Rate`

*View full spreadsheets setup guidelines in [Exercises.md](Exercises.md).*

---

## 🏫 Daily Project / Assignment: Revenue Dashboard Engine

We built an executable Python command-line engine in [Code/metrics_calculator.py](Code/metrics_calculator.py) that processes raw customer records and prints an executive financial dashboard:
*   Parses customer arrays containing MRR, CAC, and Status.
*   Calculates active MRR/ARR, average account CAC, customer LTV, and CAC Payback Periods.
*   Identifies business health warnings (e.g. flagging our mock LTV:CAC ratio of 1.52x as being below the target 3.0x limit, indicating high marketing costs or churn).

*View the project requirements in [Assignment.md](Assignment.md) and the system diagram in [Architecture.md](Architecture.md).*

---

## 📂 Expected Deliverables
*   📝 [Day 2 Study Notes](Notes.md) — Math formulas for subscription mechanics and billing.
*   📝 [Excel Formulas Guide](Exercises.md) — Spreadsheet cell codes.
*   📝 [Dashboard Specification](Assignment.md) — Project requirements.
*   📊 [Telemetry Flow Diagram](Architecture.md) — Stripe webhook integration flow.
*   💻 [Metrics Calculator Script](Code/metrics_calculator.py) — Executable dashboard backend.

---

## 📝 Notes & Reflection
*   **Key Insight**: Monthly billing drives high conversion but introduces high churn risk. Annual billing improves cash flow but requires deferred accounting.
*   **Study Log**: Read notes in [Notes.md](Notes.md).
*   **Daily Log**: Read reflections in [Reflection.md](Reflection.md).
