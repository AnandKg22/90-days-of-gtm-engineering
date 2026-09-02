# Project Assignment - Day 037: PII Masking & Compliance Engine

This project requires developing a Python PII Masking & Compliance Engine. It processes customer contact details, implements PII email/phone masking, generates SHA-256 hashes of identifiers, processes GDPR "Right to Be Forgotten" anonymization requests, and records compliance audits to a local log file.

---

## 🎯 Requirements

Your Python application must:
1.  Define a customer contact dataset containing:
    *   `user_id`, `name`, `email`, `phone`, `total_purchases_usd`.
2.  Implement **PII Masking**:
    *   `mask_email()`: Mask the mailbox name, leaving only the first and last letters visible (e.g., `dean@imsgoa.org` ──> `d***n@imsgoa.org`).
    *   `mask_phone()`: Mask the middle digits, keeping only the country code and last 4 digits visible.
3.  Implement **Cryptographic Hashing**:
    *   `hash_email()`: Generate SHA-256 hashes of emails to allow database joins without exposing raw text.
4.  Implement **GDPR Right to Be Forgotten**:
    *   `anonymize_user(user_id)`: Overwrite raw identifiers with anonymized tokens (`ANONYMIZED_USER`, phone redactions, email hashes) while leaving the `total_purchases_usd` field unchanged to preserve financial reporting.
5.  Implement **Compliance Auditing**:
    *   Write a log entry to a local JSON file named `compliance_audit.json` for every anonymization request completed.
6.  Print the raw, masked, and anonymized records to the console.

---

## 💻 Deliverable Code

A complete, working compliance engine script has been created and placed in [Code/compliance_masker.py](Code/compliance_masker.py). It models the datasets, executes the masking and hashing algorithms, updates the records, and writes the audit log.
