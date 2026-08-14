# Reflection - Day 025: Capstone Ingestion Pipeline

A personal log reflecting on the learning outcomes and concepts mastered in Phase 2 and implemented in the Day 25 Capstone Project.

---

## 💡 Key Takeaways & Lessons Learned

1.  **Integrated stacks require uniform keys**: To run joins between clickstream tracking logs (Segment), invoice details (Stripe), and contacts (HubSpot), we must enforce a uniform key layout (like email domains). Without a unified key, compiling clean database reports is impossible.
2.  **Defensive Programming is mandatory for Webhooks**: Public webhook endpoints will receive malformed body payloads, foreign key violations, and network timeouts. Implementing validation tries, transient retries, and DLQ dumps is required to keep systems running.
3.  **Data Quality must be validated at every layer**: Staging schemas, dbt tests, and application validations must work together. Verifying schemas *during* ingestion prevents bad records from locking production tables.

---

## 💻 Script Verification

I ran the `Code/ingestion_pipeline.py` capstone script to verify the end-to-end routing.
*   **Result**: 
    *   *Event 1 & 2 (Signup)*: Successfully upserted Tolani and IMSGOA into `dim_companies`, setting correct tiers (Enterprise vs. SME).
    *   *Event 3 (Deal)*: Successfully triggered a simulated 429 error, executed a retry, and inserted the $15,000.00 / 600-seat deal into `fact_deals`.
    *   *Event 4 (Malformed signup)*: Successfully aborted execution (preventing script crash) and routed to the DLQ table.
    *   *Event 5 (Missing Company ID)*: Successfully detected the foreign key violation, aborted writing to the fact table, and routed the payload to the DLQ.
    *   *Sales Report*: Correctly joined dimensions and facts, showing Tolani's $15,000 sales performance and listing the 2 DLQ errors.
*   **Insight**: This capstone implements the exact, high-availability architecture required for enterprise data integration pipelines.

---

## 🎯 Looking Forward to Phase 3: Analytics & Reporting
Having mastered CRM fundamentals (Phase 1) and Data & Integrations (Phase 2), we now move into **Phase 3: Analytics & Reporting** (Days 26-50). I will focus on configuring Looker Studio dashboard visuals, tracking MRR, calculating CAC, and building executive forecasting reports.
