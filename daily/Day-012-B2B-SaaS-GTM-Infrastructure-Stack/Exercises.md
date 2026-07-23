# Exercises - Day 012: GTM Stack Integration Blueprint

This document contains the multi-system Integration Blueprint mapping the commercial B2B SaaS data contracts.

---

## 📋 Multi-System Integration Blueprint Matrix

This matrix guides how data is routed, transformed, and updated across the GTM stack upon a Stripe payment transaction:

| Step | Source System | Target System | Action / API Endpoint | Auth Method | Payload Fields Mapped |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | **Stripe Checkout** | **n8n Orchestrator** | HTTP POST webhook receiver `/webhooks/stripe/payment` | API Key Header | `customer_email`, `quantity`, `amount_total` |
| **2** | **n8n Orchestrator** | **Apollo API** | POST `https://api.apollo.io/v1/people/match` | Bearer Token | Match: `email` ──> Return: `company_name`, `employee_count`, `tech_stack` |
| **3** | **n8n Orchestrator** | **HubSpot CRM** | POST `/crm/v3/objects/companies` | OAuth 2.0 | `name` ──> `name`<br>`employee_count` ──> `cadet_seats_purchased`<br>`tech_stack` ──> `sponsoring_shipping_lines` |
| **4** | **n8n Orchestrator** | **Outreach** | POST `/v2/prospects` | OAuth 2.0 | Create Prospect: `email` ──> Trigger outreach onboarding sequence ID `seq_1190` |
| **5** | **n8n Orchestrator** | **Slack API** | POST `/services/hooks/incoming-webhook` | Webhook URL | Format markdown block: `🏆 *New Deal Closed Won!*` |
| **6** | **n8n Orchestrator** | **PostgreSQL DB** | INSERT INTO `sales_analytics` | Database SSL Credentials | `hubspot_id`, `company_name`, `mrr_usd`, `synced_at` |
