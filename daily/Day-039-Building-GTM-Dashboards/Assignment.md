# Project Assignment - Day 039: GTM Control Center

This project requires developing a Python GTM Control Center. It aggregates a deals database, calculates top-level SaaS metrics, visualizes pipeline stages, enables interactive filters and drill-downs, and simulates real-time data ingestion and stage progressions.

---

## 🎯 Requirements

Your Python application must:
1.  **Define a Deals Database**:
    *   Store records with fields: `deal_id`, `company`, `value` (ARR), `stage` (Discovery to Closed Won), `sales_rep`, `region` (AMER, EMEA, APAC), and `segment` (Enterprise, Mid-Market, SMB).
2.  **Calculate Core SaaS & GTM KPIs**:
    *   `ARR` (Bookings) & `MRR` (monthly contribution).
    *   `Pipeline Value` (total active deals value).
    *   `Weighted Sales Forecast` (deal value multiplied by close probability).
    *   `Average Deal Size` (won deals ARR / won deal count).
    *   `Lead Win Rate` (won deals / total deals).
    *   `Customer Economics` (LTV and LTV:CAC Ratio based on an assumed average CAC of $8,500).
3.  **Visualize Funnel Stage Distribution**:
    *   Render a text-based ASCII bar chart in the console representing the count of deals per sales stage.
4.  **Implement Dynamic Dashboard Filters**:
    *   Allow metrics and funnel distribution to be filtered by `region` or `segment`.
5.  **Support Granular Drill-Downs**:
    *   Compile performance summaries by `sales_rep` (total deals, win rate, bookings, active pipeline).
    *   List raw deals belonging to specific pipeline stages.
6.  **Simulate Real-Time Updates**:
    *   Expose interfaces to update a deal's stage (recalculating KPIs).
    *   Expose interfaces to ingest new deals in real-time.

---

## 💻 Deliverable Code

A complete, working GTM Control Center script has been created and placed in [Code/gtm_control_center.py](Code/gtm_control_center.py). It implements the database engine, executes the dashboard renders, compiles rep report metrics, and displays real-time update pipelines.