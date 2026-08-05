# Reflection - Day 020: Data Warehousing (BigQuery)

A personal log reflecting on the learning outcomes and concepts mastered on Day 20.

---

## 💡 Key Takeaways & Lessons Learned

1.  **Columar Databases charge on scans**: Unlike relational systems (which charge on CPU usage), BigQuery charges based on the terabytes of data scanned. Writing loose `SELECT *` queries will generate massive monthly bills. Selecting explicit columns is mandatory.
2.  **Table Partitioning is the best cost control**: Partitioning tables by date and enforcing date filters on queries limits the data scan to specific partitions. It prevents scanning the entire database history, reducing costs by up to 99%.
3.  **Arrays bypass Join Overhead**: Storing telemetry events as repeated arrays of structs inside the contact record eliminates the need for expensive database joins, allowing fast, parallel event processing.

---

## 💻 Script Verification

I ran the `Code/bigquery_simulator.py` script to verify our SQL `UNNEST` simulation and partition checks.
*   **Result**: 
    *   *Query 1 (Unoptimized)*: Successfully returns matching records but flags a `[WARNING] Full Table Scan Detected` since no date partition key filter was found.
    *   *Query 2 (Optimized)*: Correctly filters by date key, outputting a `[SUCCESS] Partition Pruning Active` message and reducing estimated slot usage.
*   **Insight**: This simulation models the cost-saving checks GTM Engineers must audit before deploying queries in GCP.

---

## 🎯 Plan for Tomorrow
Tomorrow is Day 21: **dbt (Data Build Tool)**. I will focus on understanding dbt's role in analytics engineering, writing dbt models, configuring staging/marts folders, and compiling SQL transformation DAGs.
