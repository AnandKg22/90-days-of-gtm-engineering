# Reflection - Day 037: Data Compliance & Governance

A personal log reflecting on the learning outcomes and concepts mastered on Day 37.

---

## 💡 Key Takeaways & Lessons Learned

1.  **PII Isolation secures database models**: Storing sensitive fields (names, emails) alongside transaction histories in a single table is a security risk. Separating PII into a restricted PII Vault table linked by UUIDs is the standard best practice.
2.  **Anonymization preserves financial metrics**: To comply with GDPR's Right to Be Forgotten, you do not need to delete transactional histories. Overwriting raw contact details with redacted tokens (e.g. `ANONYMIZED_USER`) keeps purchase values intact for MRR reports while complying with deletion requests.
3.  **One-way hashing allows clean joins**: Generating SHA-256 hashes of emails allows GTM teams to link ad click tables to customer tables without exporting or exposing raw emails, ensuring GDPR and CCPA compliance.

---

## 💻 Script Verification

I ran the `Code/compliance_masker.py` script to test data masking rules, SHA-256 hashing, GDPR anonymization overrides, and audit log generation.
*   **Result**: 
    *   *Masking output*: Properly converted `dean@imsgoa.org` to `d***n@imsgoa.org` and phone numbers to `+91-*****43210`.
    *   *Anonymization output*: Successfully processed user `usr_01` (Vikram Singh), resetting his name to `ANONYMIZED_USER` and redacting his phone number.
    *   *Data retention check*: Checked that his purchase history ($15,000) remained intact in the finance view, confirming data completeness.
    *   *Audit Log*: Written successfully as `compliance_audit.json`.
*   **Insight**: This proves how PII isolation allows companies to satisfy deletion requests while maintaining financial history.

---

## 🎯 Plan for Tomorrow
Tomorrow is Day 38: **Security & Access Control (RBAC, SSO)**. I will focus on Role-Based Access Control, Single Sign-On, OAuth scopes, client credentials, database permissions, and API tokens.
