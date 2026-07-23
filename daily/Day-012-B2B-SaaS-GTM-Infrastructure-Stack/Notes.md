# Study Notes - Day 012: B2B SaaS GTM Infrastructure Stack

Today's studies focused on B2B SaaS architecture, multi-system integrations, data contracts, and orchestrating API pipelines (Stripe, Apollo, HubSpot, Outreach, Slack, Postgres).

---

## 1. The GTM Infrastructure Stack

An enterprise GTM stack integrates specialized tools to form a closed-loop revenue engine:

```
[ Stripe Billing ] ──(Payment)──> [ n8n Orchestrator ] ──(Enrich)──> [ Apollo API ]
                                         │
                                   (Sync Records)
                                         ▼
[ Slack Alerts ] ◄──(Notify)─── [ HubSpot CRM ] ───(Outbound)───> [ Outreach Sequences ]
                                         │
                                   (Analytics)
                                         ▼
                              [ PostgreSQL pgvector ]
```

*   **Stripe**: The billing gateway that captures purchases, trial starts, and upgrades.
*   **n8n / Workato**: The integration broker that runs workflows and routes data.
*   **Apollo / Clearbit**: Enrichment APIs that fetch employee size, location, and technographics.
*   **HubSpot / Salesforce**: The single source of truth for sales pipelines.
*   **Outreach / Salesloft**: The email sales sequence automation tool.
*   **Slack**: Real-time sales channel notifications and buyer alerts.
*   **Postgres (pgvector)**: Local replica database for SQL reporting and AI lead routing.

---

## 2. Deep-Dive: GTM Stack Subtopics

To construct an enterprise GTM infrastructure stack, a GTM Engineer must master these three subtopics:

### 1. API Documentation Auditing
*   **Definition**: Reading developer documentation to identify endpoints, authentication models (OAuth2 vs Bearer Token), rate limits, and payload schemas.
*   **GTM Application**: You audit API documentation to design data sync rules. For example, HubSpot limits batch company updates to 100 records per call, requiring you to write batching queues.

### 2. API Integration Patterns
*   **Definition**: Structuring REST requests, handling status codes, retries, and rate limits.
*   **GTM Application**: You write robust integration scripts:
    *   *Retry with Exponential Backoff*: Handles temporary network dropouts or rate-limiting (`429 Too Many Requests`).
    *   *Idempotency Keys*: Prevents duplicate billing charges if an API call runs twice.

### 3. Multi-system Schema Configurations (Data Contracts)
*   **Definition**: Designing JSON data contracts that represent records as they sync between tools.
*   **GTM Application**: You build a central schema registry mapping:
    *   `Stripe: customer.email` ──> `HubSpot: email` ──> `Outreach: prospect.email_address` ──> `Postgres: contacts.email`.
    *   Any field format changes (like converting phone numbers to E.164 standard) are handled by the orchestrator.
