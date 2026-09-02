# Study Notes - Day 037: Data Compliance & Governance (GDPR, CCPA)

Today's studies focused on data privacy regulations (GDPR, CCPA), personally identifiable information (PII), hashing, data masking, deletion request workflows, compliance audit logs, and database schema security.

---

## 1. Data Privacy & Compliance in GTM

Modern GTM engineering requires strict adherence to privacy frameworks:
*   **GDPR (EU)**: Grants users the "Right to Be Forgotten" (deletion requests) and requires consent.
*   **CCPA (California)**: Grants users the right to opt-out of data sale and request access/deletion.
*   **PII (Personally Identifiable Information)**: Any data that can identify an individual (e.g., email, name, phone number, IP address).

### Privacy Tactics
*   **Data Masking**: Hiding parts of sensitive strings in logs and reports (e.g. `d***n@imsgoa.org`).
*   **PII Hashing**: Using one-way cryptographic algorithms (like SHA-256) to convert emails to fixed-length strings. This allows you to join tables in the data warehouse without exposing the raw emails.
*   **Anonymization**: Stripping identifiers from purchase logs (replacing them with `ANONYMIZED_USER`) so that transaction history remains intact for financial reports while complying with deletion requests.

---

## 2. Deep-Dive: Data Compliance Subtopics

To construct compliant data warehouses, a GTM Engineer must master these three privacy subtopics:

### 1. Database Design (PII Isolation Tables)
*   **Definition**: Separating PII from transactional data to restrict access:
    *   **Transactional Table**: Stores order histories linked only to anonymous UUIDs (`order_id`, `user_uuid`, `amount_usd`, `purchase_date`).
    *   **PII Vault Table**: Stores sensitive identifiers in an encrypted database with restricted access (`user_uuid`, `raw_name`, `raw_email`, `raw_phone`).
*   **GTM Application**: When a deletion request arrives, you delete the single row in the PII Vault. The transactional table remains intact, maintaining financial history without storing user identifiers.

### 2. SQL Syntax (PII Hashing & Anonymization)
*   **Definition**: Writing SQL statements to hash emails and anonymize transaction logs for deletion requests:
    *   **Hashing emails**:
        ```sql
        SELECT 
            user_uuid,
            SHA256(email) AS hashed_email,
            amount_usd
        FROM raw_leads;
        ```
    *   **Anonymizing user profiles**:
        ```sql
        UPDATE crm_contacts
        SET 
            raw_name = 'ANONYMIZED_USER',
            raw_email = SHA256(raw_email),
            raw_phone = 'REDACTED'
        WHERE user_uuid = @target_uuid;
        ```

### 3. Query Optimization (Hashed Lookup Indexes)
*   **Definition**: Optimizing deletion lookup sweeps.
*   **GTM Application**: Sweeping massive database tables to find and delete matching emails is slow.
    *   **Indexes**: Build a B-Tree index on the hashed lookup key (`hashed_email`) to speed up deletion checks.
    *   **Delete Batching**: Group deletion requests and run them in batch updates during low-traffic windows to prevent database locks.
