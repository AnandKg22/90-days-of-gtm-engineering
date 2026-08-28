# Reflection - Day 034: Funnel Metrics

A personal log reflecting on the learning outcomes and concepts mastered on Day 34.

---

## 💡 Key Takeaways & Lessons Learned

1.  **Funnel Velocity reveals deals bottlenecking**: Simply tracking conversion rates misses the element of time. If your close rate is 10%, but deals take 9 months to sign, your sales engine is sluggish. Measuring the average days spent per stage highlights exactly where deals stall.
2.  **History logs are required for timelines**: Standard CRMs overwrite stage fields. GTM Engineers must design separate stage log history tables (`deal_stage_logs`) to capture the timestamp of every single transition, enabling time-difference aggregations.
3.  **SQL window functions simplify sequence routing**: Utilizing the `LEAD` function partition-grouped by `deal_id` allows the database to easily compare consecutive timestamps to calculate elapsed days.

---

## 💻 Script Verification

I ran the `Code/funnel_analyzer.py` script to test funnel stage conversions, durations, and velocity reports.
*   **Result**: 
    *   *Stage Counts*: Lead = 5, MQL = 4, SQL = 3, Opportunity = 2, Won = 2.
    *   *Conversion Rates*: Lead-to-MQL = 80.0%, MQL-to-SQL = 75.0%, SQL-to-Opp = 66.7%, Opp-to-Won = 100.0%. Overall conversion = 40.0%.
    *   *Velocity Ratios*: Lead stage average = 2.2 days, MQL = 4.0 days, SQL = 6.0 days, Opportunity = 14.0 days. Total cycle time = 26.2 days.
    *   *Alert Triggers*: Logged a warning warning that negotiation loops (`Opportunity` velocity) exceeded 15 days, which requires optimization.
*   **Insight**: This verifies how analyzing stage lag gives clear, actionable tips to speed up sales cycles.

---

## 🎯 Plan for Tomorrow
Tomorrow is Day 35: **Attribution Models (Multi-touch)**. I will focus on multi-touch attribution algorithms (Linear, Time Decay, Position Based/U-Shaped), SQL queries for touchpoints weight distributions, and compiling marketing ROI attribution models.
