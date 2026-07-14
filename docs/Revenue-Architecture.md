# Revenue Systems Architecture & Event Flows

This document details the blueprint for an enterprise-grade commercial tech stack, showing how data syncs securely across marketing, CRM, product usage, databases, and billing.

---

## 1. Systems Architecture Blueprint

```
                      ┌──────────────────────┐
                      │    WEB APP PORTAL    │
                      │ (React/Next.js UI)   │
                      └──────────┬───────────┘
                                 │ HTTP API
                                 ▼
                      ┌──────────────────────┐
                      │   PRODUCT DATABASE   │
                      │ (PostgreSQL/Supabase)│
                      └──────────┬───────────┘
                                 │
                 ┌───────────────┴───────────────┐
                 │                               │
                 ▼ Webhook                       ▼ segment.track()
      ┌────────────────────┐          ┌────────────────────┐
      │   n8n WORKFLOWS    │          │  CUSTOMER DATA DB  │
      │ (Orchestrator Engine)│        │   (pgvector/CDP)   │
      └──────────┬─────────┬┘          └────────────────────┘
                 │         │
      ┌──────────▼─┐     ┌─▼──────────┐
      │ HUBSPOT API│     │ STRIPE API │
      │   (CRM)    │     │ (Billing)  │
      └────────────┘     └────────────┘
```

### Data Flow Execution Sequence
1.  **Lead Capture**: User submits a signup form on the portal. Webhook fires to `n8n`.
2.  **Data Enrichment**: `n8n` calls Clearbit/Clay API to enrich the lead's firmographics.
3.  **Record Creation**: `n8n` inserts/updates Contacts & Companies in HubSpot CRM.
4.  **Routing & Notifications**: Lead is routed to a sales rep, and a Slack alert is sent.
5.  **Product Usage Events**: As user interacts with the app, telemetry captures actions and updates Customer Data DB.
6.  **Billing Event**: User upgrades. Stripe API triggers webhook, modifying plan type in Database & updating HubSpot Deal status to 'Closed Won'.

---

## 2. Event-Driven Messaging & Queues

When processing thousands of webhook events (e.g. tracking click streams or HubSpot updates), direct HTTP requests can time out or hit API rate limits. We use queues for **asynchronous processing**:

```
[Webhook Request] ──> [Express Gateway] ──> [Redis/RabbitMQ Queue] ──> [Worker Pool] ──> [DB/CRM]
```

### Why Use a Message Queue?
*   **Fault Tolerance**: If HubSpot API goes down, events remain in the queue and retry automatically.
*   **Rate Limiting**: Worker threads can throttle API requests to ensure we don't exceed HubSpot's 100 requests/second limit.
*   **Responsiveness**: The webhook receiver returns an immediate `200 OK` to the sender, moving processing to background tasks.
