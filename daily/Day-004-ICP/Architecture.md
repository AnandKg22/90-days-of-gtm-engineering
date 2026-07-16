# GTM Architecture - Day 004: ICP Lead Qualification Flow

This document details the systems design blueprint mapping automated lead intake, third-party firmographic enrichment, and programmatic ICP validation.

---

## 🔄 Lead Scoring & CRM Sync Pipeline

The sequence diagram below details how lead records are captured, validated, and categorized:

```mermaid
graph TD
    User[Web Lead / Lead Form] -->|1. Fills Form| WebApp[Next.js Portal / API]
    WebApp -->|2. HTTP POST Event| Router[n8n Automation Engine]
    
    subgraph Data Enrichment
        Router -->|3. Get Company Details| Apollo[Apollo / Clearbit APIs]
        Apollo -->|4. Size, Location, Tech Stack| Router
    end
    
    subgraph Qualification Engine
        Router -->|5. Run Score Evaluation| Validator[ICP Validator Service]
        Validator -->|6. Fit Score & Tier Category| Router
    end
    
    subgraph Destination CRM
        Router -->|7a. Sync High Fit & Create Deal| CRM[HubSpot / Salesforce]
        Router -->|7b. Trigger Slack Alert to Rep| Slack[Sales Alerts Channel]
        Router -->|7c. Sync Low/Medium to Drip| Email[Email Marketing Engine]
    end
```

---

## ⚙️ Pipeline System Rules

1.  **Form Submission**: Submits basic email (e.g. `dean@tolani.edu`).
2.  **Enrichment Lookup**: Resolves the email domain to retrieve company details:
    *   Name: `Tolani Maritime Academy`
    *   Employees: `120`
    *   Country: `IN`
    *   Technologies: `["Moodle", "Stripe"]`
3.  **ICP Scoring**: The `ICPValidator` runs, outputting a score of `90/100` (`High Fit`).
4.  **Routing Split**:
    *   *High Fit leads* immediately spawn a HubSpot Contact & Company, link them, create a Deal in the Enterprise Pipeline, and alert sales.
    *   *Medium & Low Fit leads* are placed into low-touch email drip sequences to nurture them.
