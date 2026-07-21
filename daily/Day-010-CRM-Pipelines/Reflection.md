# Reflection - Day 010: CRM Pipelines & Velocity Analytics

A personal log reflecting on the learning outcomes and concepts mastered on Day 10.

---

## 💡 Key Takeaways & Lessons Learned

1.  **Pipeline Velocity is the ultimate health metric**: Simply knowing the deal volume is not enough. If deals spend an average of 45 days in the "Contract Review" stage, it indicates legal bottlenecks or buying committee friction. Programmatically tracking durations isolates these issues.
2.  **Multi-currency normalizations prevent reporting distortions**: In global GTM, transactions are made in local currencies. Normalizing them to a single base currency (like USD) using daily API rates is mandatory to generate unified executive pipeline reports.
3.  **Auditing Transitions requires History Logs**: standard CRMs only show the current deal stage. To calculate pipeline velocity, you must design a separate history/audit table that logs timestamps for every entry and exit.

---

## 💻 Script Verification

I ran the `Code/pipeline_transitions.py` script to test the transitions, velocity tracking, and exchange rate logic.
*   **Result**: 
    *   `Tolani cadet deal (INR)` is successfully converted to `$9,960.00 USD`.
    *   `Singapore deal (SGD)` is successfully converted to `$9,990.00 USD`.
    *   The transition timestamps capture durations (e.g. Tolani spent ~1.50s in Discovery, ~3.00s in Proposal, and is now active in Won).
*   **Insight**: Automating these calculations in our local data warehouse will allow us to query and isolate friction points across all sales reps instantly.

---

## 🎯 Plan for Tomorrow
Tomorrow is Day 11: **Lead Source**. I will focus on understanding acquisition channels (organic, paid, outbound), configuring UTM parameters, and designing data capture systems.
