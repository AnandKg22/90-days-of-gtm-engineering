# Exercises - Day 037: GDPR Deletion Policy

This document details the GDPR / CCPA Data Deletion policy pipeline and data masking rules used to secure personally identifiable information (PII).

---

## 📋 GDPR / CCPA User Deletion Policy Workflow

To comply with "Right to Be Forgotten" requests, the engineering team executes the following database sequence:

```
[ Deletion Request ] ──► [ Lookup user_uuid by Email ] ──► [ Anonymize PII Vault Row ]
                                                                   │
                                                      (Preserve Transactional Metrics)
                                                                   ▼
[ Write Audit Receipt ] ◄── [ Set Name/Email to Anonymized Tokens ] ◄┘
```

### Deletion Policy Steps:
1.  **Ingestion**: Capture the user's deletion request via a support ticket or opt-out form.
2.  **Lookup ID**: Search the PII Vault for the user's email to find their unique `user_uuid`.
3.  **PII Anonymization**: Update the PII Vault record for the user:
    *   `raw_name` ──> `ANONYMIZED_USER`
    *   `raw_email` ──> `SHA256(raw_email)`
    *   `raw_phone` ──> `REDACTED`
4.  **Preserve Transactions**: Keep all financial records linked to the `user_uuid` (orders, invoices, MRR deltas). This ensures financial reporting remains accurate.
5.  **Audit Log Receipt**: Write a log entry to `compliance_audit_logs` recording the transaction:
    *   `{"audit_id": 901, "action": "DELETE_USER", "user_uuid": "...", "timestamp": "..."}`
    *   Do NOT include the user's raw email or name in this audit log.

---

## 🔒 PII Masking Rules Matrix

In Looker dashboards and debug logs, mask PII to protect user privacy:

*   **Email Masking Rule**: Keep the first and last letters of the mailbox username, masking the rest.
    *   *Example*: `dean@imsgoa.org` ──> `d***n@imsgoa.org`
*   **Phone Masking Rule**: Mask the middle digits of the phone number, leaving the country code and last 4 digits visible.
    *   *Example*: `+91-98765-43210` ──> `+91-*****43210`
