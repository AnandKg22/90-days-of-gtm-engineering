# GTM Architecture - Day 002: Revenue Dashboard Telemetry Flow

This document details the telemetry architecture that feeds the Revenue Dashboard with real-time billing transaction states.

---

## 🔄 Billing to Analytics Data Flow

Below is the event-driven data flow that captures payment changes and aggregates them into the revenue metrics engine:

```mermaid
graph TD
    Stripe[Stripe Billing Gateway] -->|1. Webhook: charge.succeeded / customer.subscription.deleted| Gateway[API Gateway Webhook Receiver]
    Gateway -->|2. Enqueue Event| Queue[Redis Event Queue]
    Queue -->|3. Consume & Process| Worker[n8n Worker / Node Worker]
    
    subgraph Data Warehouse
        Worker -->|4. Insert/Update Transactions| DB[(PostgreSQL Replica DB)]
    end
    
    subgraph Analytics Dashboard
        DB -->|5. SQL Aggregations / CTEs| Engine[SaaS Metrics Engine]
        Engine -->|6. Render Metrics JSON| Frontend[Next.js Dashboard UI]
    end
```

---

## 📂 Data Schema Telemetry

The billing webhook pushes structured transaction logs. To calculate MRR, CAC, and Churn, we track subscription states:

*   `customer.subscription.created`: Adds new ARR, adds a customer, records their CAC (tied to their UTM/ad click history).
*   `customer.subscription.updated`: Captures plan changes (expansion/contraction MRR).
*   `customer.subscription.deleted`: Triggers a Churn event, marking the status as `Churned` and calculating customer lifetime span.
*   `invoice.payment_succeeded`: Confirms active status and gross revenue.
