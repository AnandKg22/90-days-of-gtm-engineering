# Reflection - Day 008: CRM Fundamentals

A personal log reflecting on the learning outcomes and concepts mastered on Day 8.

---

## 💡 Key Takeaways & Lessons Learned

1.  **SQL Joins Power GTM Insights**: Understanding relational databases is the base of GTM Engineering. Being able to run SQL queries linking contacts, companies, deals, and activities allows us to build customized analytics dashboards that CRM platforms can't support out-of-the-box.
2.  **Junction Tables Resolve Complex B2B Committees**: The buying committee model (from Day 7) is represented in databases using Many-to-Many association tables (`CONTACTS_DEALS`). This prevents duplicating contact details across multiple deal records.
3.  **Referential Integrity Safeguards CRM Syncs**: Implementing database constraints (like `ON DELETE CASCADE` and foreign key verification) ensures that when a company is deleted, its stale orphan deals are cleaned up, preventing database bloat.

---

## 💻 Script Verification

I ran the `Code/mini_crm.py` script to verify our SQL queries and data seed results.
*   **Result**: 
    *   `Query 1`: Correctly maps contacts to their respective employer companies.
    *   `Query 2`: Correctly returns the sales deals pipeline (AMET, Tolani, IMSGOA deals, amounts, and stages).
    *   `Query 3`: Correctly logs activities (such as emails and calls) associated with our contacts.
*   **Insight**: This in-memory SQLite schema is the exact blueprint we will use in Phase 2 to mirror HubSpot/Salesforce data directly into our local PostgreSQL analytics replica.

---

## 🎯 Plan for Tomorrow
Tomorrow is Day 9: **CRM Customization**. I will focus on configuring custom fields, mapping database schemas, and setting up automated Webhook integrations to sync data.
