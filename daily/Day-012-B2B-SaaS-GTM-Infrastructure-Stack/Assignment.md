# Project Assignment - Day 012: GTM Stack Orchestrator

This project requires developing a Python integration prototype that acts as a central orchestrator (simulating n8n/Workato) to execute our multi-system GTM blueprint.

---

## 🎯 Requirements

Your Python orchestrator must:
1.  Ingest a Stripe Checkout Completed webhook payload.
2.  Orchestrate a sequential multi-system integration flow:
    *   **Apollo Enrichment API**: Query a mock enrichment API to fetch company size and technographic stack details using the billing domain.
    *   **HubSpot CRM Sync**: Post enriched properties to a mock HubSpot API.
    *   **Outreach Engagement Sync**: Add the contact email to a mock onboarding email sequence.
    *   **Slack Alerts webhook**: Format and output a Markdown notification message.
    *   **PostgreSQL Log**: Record the transaction to a mock database audit list.
3.  Print a chronological log trace showing details and responses for each system call.

---

## 💻 Deliverable Code

A complete, working simulation script has been created and placed in [Code/stack_orchestrator.py](Code/stack_orchestrator.py). It models the full stack flow, executes the steps sequentially, and prints the audit logs.
