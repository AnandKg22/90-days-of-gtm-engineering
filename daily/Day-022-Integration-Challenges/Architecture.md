# GTM Architecture - Day 022: API Retry & DLQ Architecture

This document details the retry flow chart and Dead Letter Queue (DLQ) layout configured to prevent data loss in integration pipelines.

---

## 🔄 API Retry & Dead Letter Queue (DLQ) Process

The flowchart below details how inbound transactions are filtered, retried, and logged:

```mermaid
graph TD
    Start[Inbound API Request] --> Send{Send Payload}
    Send -->|HTTP 200| Success[Success: Complete Run]
    
    Send -->|HTTP 400| Skip{Bad Request: Schema Mismatch?}
    Skip -->|Yes| DLQ[Save to Dead Letter Queue PostgreSQL]
    DLQ --> Slack[Send Critical Slack Alert]
    
    Send -->|HTTP 429 / 503| RetryCheck{Retry Attempt < 3?}
    RetryCheck -->|No: Max Retries Exceeded| DLQ
    
    RetryCheck -->|Yes: Retriable| Wait[Compute Exponential Backoff + Jitter]
    Wait -->|Delay Wait Time| Send
```

---

## ⚙️ Log Payload Format

When transactions fail permanently, they are logged to a JSON file format inside `integration_failures.log` for automatic alerting:

```json
{
  "timestamp": "2026-07-13 15:37:25",
  "level": "ERROR",
  "details": {
    "endpoint": "/outreach/prospect/add",
    "status_code": 400,
    "error": "Bad Request: Custom field 'job_role' does not exist in schema",
    "payload": {
      "email": "captain@imsgoa.org",
      "job_role": "Deck Officer"
    }
  }
}
```
