# Reflection - Day 039: Building GTM Dashboards

A personal log reflecting on the learning outcomes and concepts mastered on Day 39.

---

## 💡 Key Takeaways & Lessons Learned

1.  **Weighted Pipeline yields realistic forecasts**: Simply summing active deal values (unweighted pipeline) leads to inflated bookings forecasts. Applying historical stage close probabilities (e.g., Proposal = 50%, Negotiation = 80%) enables finance and operations to build reliable cash flow models.
2.  **Dashboard design must fit the persona**: Executives need a high-level view of bookings, pipeline volume, and SaaS unit economics (LTV:CAC). Sales representatives need list views, staled deal alerts, and individual performance win rates.
3.  **BI Engine and indexes are critical for dashboard speed**: Dynamic dashboard filters trigger queries on every change. In-memory caching (like BigQuery BI Engine) and multi-column indexes prevent page latency and control database scanning costs.

---

## 💻 Script Verification

I ran the `Code/gtm_control_center.py` script to verify the KPIs, funnel visualization, dynamic filtering, rep drill-downs, and real-time updates:
*   **Initial KPIs**: Calculated total ARR bookings ($227,000.00), active pipeline ($370,000.00), and weighted forecast ($388,000.00). Renders a clean ASCII funnel bar chart showing deal distribution across stages.
*   **Filtered Views**: Successfully applied filters by Region (AMER) which narrowed down ARR bookings to $132,000.00 and adjusted the funnel bar chart.
*   **Drill-down Reports**: Generated performance tables for Sarah Connor (25% win rate, $120,000 bookings), Bruce Wayne (66.7% win rate, $107,000 bookings), and Deckard Shaw (0% win rate).
*   **Real-time Updates**: Simulates moving Deal #103 to "Closed Won" and adding a new $200k Enterprise deal. Recalculates total ARR to $272,000.00, active pipeline to $525,000.00, and weighted forecast to $510,500.00.
*   **Insight**: This models how live data streams dynamically update Looker dashboards for real-time visibility.

---

## 🎯 Plan for Tomorrow

Tomorrow is Day 40: **Phase 2 Capstone Project (AI Revenue Automation Platform v1)**. I will integrate the automation workflows, lead scoring, database ingestion, and dashboard models developed throughout Phase 2 into a single cohesive capstone platform.
