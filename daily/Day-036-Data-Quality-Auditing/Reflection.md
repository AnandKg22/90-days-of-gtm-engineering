# Reflection - Day 036: Data Quality & Auditing

A personal log reflecting on the learning outcomes and concepts mastered on Day 36.

---

## 💡 Key Takeaways & Lessons Learned

1.  **Enforce constraints at the database level**: Relying solely on client-side JS forms to sanitize inputs leaves the database vulnerable to bad API calls or manual uploads. Check constraints must be written in the SQL DDL statements.
2.  **Quarantine instead of discarding**: Discarding bad rows makes it hard to identify where the bad data is coming from. Quarantining bad records to an error log database allows engineers to trace the issues back to malformed HubSpot forms or broken API payloads.
3.  **Timestamp audits solve duplicates**: When two leads share the same email, sorting them chronologically and keeping the most recent timestamp ensures sales reps call the lead with the newest intent information.

---

## 💻 Script Verification

I ran the `Code/data_auditor.py` script to test data cleansing rules, duplicate checks, and JSON exports.
*   **Result**: 
    *   *Total Inspected*: 6 records.
    *   *Passed Clean*: 2 records (Dean - ID 201, Captain - ID 206).
    *   *Quarantined*: 4 records (ID 202 - older duplicate, ID 203 - invalid email, ID 204 - negative amount, ID 205 - missing company).
    *   *Log File*: Written successfully as `quarantine_log.json`.
    *   *Warning Alert*: Triggered a dataset error rate warning (66.7% quarantine rate).
*   **Insight**: This proves how automated audit scorecards identify bad input webhooks before they pollute downstream reports.

---

## 🎯 Plan for Tomorrow
Tomorrow is Day 37: **Data Compliance & Governance (GDPR, CCPA)**. I will focus on data privacy regulations, personally identifiable information (PII) hashing, data masking, deletion requests, and audit logs.
