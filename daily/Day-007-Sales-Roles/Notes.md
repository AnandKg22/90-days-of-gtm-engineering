# Study Notes - Day 007: Commercial Sales Roles & Hand-offs

Today's studies focused on commercial roles (SDR, BDR, AE, SE, CS, RevOps, GTM), their responsibilities, key performance indicators (KPIs), and hand-off mechanics.

---

## 1. Commercial Sales Roles

A B2B SaaS company splits the sales process into specialized roles:

*   **SDR (Sales Development Rep)**: Focuses on qualifying inbound leads (leads who filled out forms on our website).
*   **BDR (Business Development Rep)**: Focuses on cold outbound prospecting (finding target companies on LinkedIn and emailing them).
*   **AE (Account Executive)**: Owns the quota. Runs demo meetings, handles pricing negotiations, and signs contracts.
*   **Sales Engineer / Solutions Architect**: Technical expert who supports the AE during complex enterprise sales, building custom product prototypes.
*   **Customer Success Manager (CSM)**: Owns onboarding, product adoption, retention, and expansion upsells after the contract is signed.
*   **RevOps (Revenue Operations)**: Operates the commercial software tools and ensures sales processes run smoothly.
*   **GTM Engineer**: Writes the code, builds the APIs, integrates custom scripts, and manages database replicas that power RevOps and sales teams.

---

## 2. Deep-Dive: Sales Roles Subtopics

As a GTM Engineer, you must build workflows supporting the actions, metrics, and hand-offs of these roles:

### 1. Daily Activities & System Ownership
*   **SDR/BDR**: System ownership is Apollo/LinkedIn Sales Navigator (sourcing) and Outreach/Salesloft (email sequencing).
*   **AE**: System ownership is HubSpot/Salesforce Deals and calendar apps.
*   **CSM**: System ownership is Gainsight/ChurnZero and Zendesk (support).
*   **RevOps/GTM**: System ownership is n8n, Stripe APIs, Postgres DBs, and CRM settings.

### 2. Key Performance Indicators (KPIs)
*   **SDR/BDR**: Meetings booked, SQL conversion rate %.
*   **AE**: New Net ARR closed, Win rate %, Sales cycle length.
*   **CSM**: Net Revenue Retention (NRR), Logo Churn %, Onboarding Time.
*   **RevOps/GTM**: Lead-to-assign time, API system uptime, data sync accuracy %, pipeline velocity.

### 3. Customer Hand-off Workflows
*   **The Problem**: If data is lost during a transition (e.g. an AE doesn't tell a CSM what the customer's goals are), the customer experience suffers, increasing churn.
*   **GTM Automation Solution**:
    *   *SDR -> AE*: When an SDR books a Calendly, the system automatically creates a HubSpot meeting, matches the company domain to the assigned AE, and pushes qualification notes to the calendar invite.
    *   *AE -> CSM*: When a deal changes to "Closed Won," the system triggers an onboarding kickoff task, clones the deal properties to the CS workspace, and schedules a Slack notification for the CSM.
