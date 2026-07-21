# Day 010: CRM Pipelines

## Objective
Understand CRM pipeline transitions, configure multi-currency conversions, and build tracking scripts that calculate stage duration (pipeline velocity) to isolate sales bottlenecks.

## Topics Covered
- Multi-currency pipeline setups
- Pipeline stage transitions
- Stage change automation triggers
- Pipeline velocity analytics

## Subtopics (Developed in Notes)
- Workflow Automation Triggers
- Deal Stage History (Pipeline Velocity)
- Multi-currency Setup & Normalization

---

## 🛠️ Practical Exercise: Multi-Currency Calculations

In this exercise, we designed currency conversion pipelines to normalize global deals to a base currency (USD):
*   **Exchange Rate Rules**: US Dollar (`USD` @ `1.0`), Indian Rupee (`INR` @ `0.012`), Singapore Dollar (`SGD` @ `0.74`).
*   **Normalized Valuation Math**:
    *   *Tolani Cadet Licenses*: `INR 830,000` ──> **$9,960.00 USD**.
    *   *Singapore Campus Deal*: `SGD 13,500` ──> **$9,990.00 USD**.
*   **SQL Database View**: Constructed a SQL VIEW joining currency rates to raw deal amounts, preparing normalized data for pipeline metrics dashboards.

*View conversion definitions and SQL statements in [Exercises.md](Exercises.md).*

---

## 🏫 Daily Project / Assignment: Pipeline Stage Transition Tracker

We built an executable Python pipeline analytics script in [Code/pipeline_transitions.py](Code/pipeline_transitions.py):
*   Tracks deal objects (`id`, `name`, `local_amount`, `currency_code`) and logs transitions across stages.
*   Calculates **Pipeline Velocity** (duration spent in each stage using timestamp deltas).
*   Normalizes deal amounts dynamically using exchange rate multipliers to compile unified USD forecasts.

*View project requirements in [Assignment.md](Assignment.md) and the system diagram in [Architecture.md](Architecture.md).*

---

## 📂 Expected Deliverables
*   📝 [Day 10 Study Notes](Notes.md) — Pipeline metrics, velocity, and multi-currency rules.
*   📝 [Multi-currency Spec](Exercises.md) — Exchange rate calculations and SQL views.
*   📝 [Transition Script Spec](Assignment.md) — Project requirements.
*   📊 [Velocity Database Diagram](Architecture.md) — Transition log schema.
*   💻 [Velocity Analytics Script](Code/pipeline_transitions.py) — Executable transition tracking program.

---

## 📝 Notes & Reflection
*   **Key Insight**: Stage history logging (storing timestamps on enter and exit) allows companies to audit velocity cohorts and pinpoint where deals stall in the buying journey.
*   **Study Log**: Read notes in [Notes.md](Notes.md).
*   **Daily Log**: Read reflections in [Reflection.md](Reflection.md).
