# GTM Architecture - Day 001: VivaExams Go-To-Market Stack

This document details the system integrations and data flow architecture designed for the VivaExams GTM engine.

---

## 🗺️ GTM Systems Architecture

Below is a sequence architecture showing how data traverses the product portal, webhook routing engine, HubSpot CRM, and Stripe billing:

```mermaid
graph TD
    User[Student / College Admin] -->|1. Sign Up / Free Test| WebApp[VivaExams Next.js Web App]
    WebApp -->|2. Event Webhook: /api/lead| Router[n8n Automation Engine]
    
    subgraph Enrichment & Routing
        Router -->|3. Query Domain| Scraper[Enrichment Scraper]
        Scraper -->|4. Firmographic Info| Router
    end
    
    subgraph CRM & Notifications
        Router -->|5. Sync Contacts/Deals| HubSpot[HubSpot CRM]
        Router -->|6. Alert B2B SQL| Slack[Slack Sales Alerts Channel]
    end
    
    subgraph Billing & Provisioning
        HubSpot -->|7. Send Invoice / Quote| Stripe[Stripe Billing Gateway]
        Stripe -->|8. Webhook: Payment Success| WebApp
        WebApp -->|9. Provision Seats| DB[(PostgreSQL Product DB)]
    end
```

---

## 🔄 Core Data Flow Steps

1.  **Lead Intake**: The user submits their email on the Next.js portal. The portal sends a JSON payload to our n8n webhook intake endpoint.
2.  **Enrichment Step**: The n8n engine extracts the email domain. If it is an institutional domain (e.g., `.edu`), it scrapes web metadata or calls our internal scraper to extract the institution name and enrollment statistics.
3.  **CRM Synchronization**: n8n formats the payload into a standard HubSpot CRM contact object. It creates or updates the Contact and Company records.
4.  **B2B Routing Alert**: If the contact is identified as a B2B college admin, n8n pushes a formatted message to Slack with a HubSpot profile link, assigning the lead to an Account Executive.
5.  **Billing & Provisioning Loop**: When a deal closes, Stripe handles billing. Stripe sends an event notification back to our API gateway upon payment success, which triggers database SQL scripts to provision license seats inside the PostgreSQL application database.
