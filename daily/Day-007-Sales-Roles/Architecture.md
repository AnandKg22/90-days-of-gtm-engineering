# GTM Architecture - Day 007: Sales Org Structure & Tools Ownership

This document details the sales organization structure, roles, and software tool boundaries within the commercial stack.

---

## 🛠️ Sales Org Structure & Tool Hierarchy

Below is the commercial organization tree, mapping each team member to their primary software tools and databases:

```mermaid
graph TD
    CRO[Chief Revenue Officer / VP of Sales] --> RevOps[RevOps / GTM Engineering]
    CRO --> Sales[Sales Team]
    CRO --> CS[Customer Success Team]
    
    subgraph System Ownership
        RevOps -->|Config & Code| Tools[n8n, Stripe APIs, Postgres DB, CRM Admin]
        Sales -->|Outreach & Demos| ToolsSales[HubSpot Deals, LinkedIn Sales Nav, Calendly]
        CS -->|Retention & Support| ToolsCS[Gainsight, ChurnZero, Zendesk]
    end
```

---

## 📂 Ownership Matrices

| Role | Core Mission | Primary CRM Objects | Primary Software Stack |
| :--- | :--- | :--- | :--- |
| **SDR/BDR** | Qualify Leads | Contacts, Activities | Apollo.io, LinkedIn Sales Navigator, HubSpot (Inbox) |
| **AE** | Close Deals | Contacts, Companies, Deals | HubSpot (Deals Board), Calendly, Zoom |
| **CSM** | Retain Customers | Contacts, Companies, CS tickets | Gainsight, Zendesk, Product Admin Panel |
| **RevOps/GTM** | Build Infrastructure | All Objects + Database Replica | n8n Workflows, Stripe Billing, Postgres, Docker, pgvector |
