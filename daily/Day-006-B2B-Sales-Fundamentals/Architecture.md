# GTM Architecture - Day 006: Sales Pipeline & Forecasting

This document details the sales pipeline architecture and data flows that update deal statuses and calculate revenue projections.

---

## 🔄 Sales Stage Updates & Forecast Data Flow

The diagram below details how deal movements in the CRM trigger database syncs and recalculate weighted pipeline valuations:

```mermaid
graph TD
    Rep[Sales Rep / AE] -->|1. Moves Deal Stage| CRM[HubSpot / Salesforce UI]
    CRM -->|2. Webhook: deal.stage_change| Gateway[API Webhook Receiver]
    Gateway -->|3. Log Stage History| Queue[Redis Task Queue]
    Queue -->|4. Update Database| DB[(PostgreSQL Replica DB)]
    
    subgraph Forecasting Engine
        DB -->|5. SQL Queries with Stage Probability| Engine[Metrics Forecast Engine]
        Engine -->|6. Render Pipeline Stats| UI[Executive Dashboard / Slack Digest]
    end
```

---

## 📂 Webhook Event Payload

When an AE moves a deal's stage in HubSpot, it fires a webhook payload:

```json
{
  "event": "deal.stage_change",
  "deal_id": "d_001",
  "properties": {
    "deal_name": "Tolani Maritime Academy",
    "amount": 10000.00,
    "old_stage": "Discovery",
    "new_stage": "Proposal",
    "last_updated": "2026-07-13T15:16:00Z"
  }
}
```

This payload is consumed by the Webhook Receiver and updates the active stage in our Postgres database replica. The analytics dashboard then runs the weighted sum queries to update forecast statistics.
