# Exercises - Day 022: GTM Error Handling Strategy

This document details the GTM Stack Error Handling Strategy designed to protect pipeline transactions from API timeouts, schema changes, and rate limits.

---

## 📋 Integration Error Handling Matrix

This matrix defines the recovery actions executed when integrations encounter failures:

| Failure Scenario | Detection Method | Immediate Action | Secondary Action (SLA) |
| :--- | :--- | :--- | :--- |
| **API Throttling** (HTTP 429) | Inbound status code `= 429` | Wait using **Exponential Backoff + Jitter** and retry. | If 5 retries fail, route payload to **DLQ** and alert engineering. |
| **CRM Connection Timeout** (HTTP 504) | Connection timeout exception | Wait 5 seconds and retry. | If timeout persists after 3 tries, log warning and add to Redis queue for later execution. |
| **Invalid Schema Payload** (HTTP 400) | Inbound status code `= 400` | Skip retries immediately (prevents repeating bad requests). | Dump payload to **DLQ** file; send high-priority alert to RevOps Slack channel. |
| **CRM Destination Down** (HTTP 503 / 500) | Inbound status code `>= 500` | Hold queue execution; trigger n8n error workflow. | Alert system operations; schedule sync retry in 15-minute intervals. |

---

## ⚙️ Dead Letter Queue (DLQ) Schema Configuration

When a payload fails permanently, it is logged to a PostgreSQL `dead_letter_queue` table for manual auditing:

```sql
CREATE TABLE dead_letter_queue (
    id SERIAL PRIMARY KEY,
    failed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    target_system VARCHAR(100) NOT NULL, -- e.g. "HubSpot"
    error_code INT,
    error_message TEXT,
    payload_json JSONB NOT NULL,
    status VARCHAR(50) DEFAULT 'Pending Review' -- Pending, Resolved, Ignored
);
```
