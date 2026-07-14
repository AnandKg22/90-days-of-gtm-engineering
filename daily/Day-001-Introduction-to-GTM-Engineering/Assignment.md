# Project Assignment - Day 001: VivaExams GTM Journey Design

This document details the Go-To-Market (GTM) customer journey specifically designed for **VivaExams** (a SaaS mock exam prep platform targeting maritime institutions and students).

---

## 🏫 VivaExams Platform Context

VivaExams sells mock exam prep tools in two modes:
1.  **B2C (Self-Serve)**: Direct sales to students buying practice mock tests.
2.  **B2B (Enterprise Sales)**: Bulk licenses sold to Maritime Colleges (e.g., IMSGOA, AMET, Tolani) for institutional mock exam delivery and auto-grading.

---

## 🗺️ The VivaExams GTM Journey Design

Here is the operational blueprint of the commercial funnel:

```
[Student/Dean on Site] ──> [Fills Form / Free Test] ──> [Enrichment & Domain Router]
                                                               │
                                         ┌─────────────────────┴─────────────────────┐
                                         ▼ (Student Domain)                          ▼ (College Admin Domain)
                              [B2C Self-Serve Flow]                        [B2B Enterprise Flow]
                                  - Email Onboarding                           - Slack Alert to Rep
                                  - Stripe Checkout ($49)                      - Book Demo (Meeting)
                                  - Self-provisioning                          - Proposal SOW ($5,000+)
```

---

### Stage-by-Stage Design Details

#### 1. Lead Generation (Visitor to Lead)
*   **The Hook**: A visitor lands on the VivaExams pricing page or blog and signs up for a "Free Marine Engineering Class IV Mock Exam Paper" (Lead Magnet).
*   **Intake Fields**: First Name, Last Name, Work/College Email, Institution Name, Role (Student vs. Professor/Dean).
*   **Database Record**: Created instantly in our product database and sent to HubSpot CRM via n8n webhook.

#### 2. Lead Qualification & Routing (Lead to MQL/SQL)
*   **Automated Enrichment Logic**:
    *   An n8n worker runs when a lead enters. It extracts the email domain (e.g. `tolani.edu`, `student@gmail.com`).
    *   If the domain is standard (Gmail/Yahoo) or role is student: Tag as **B2C Lead** and send to Self-Serve Onboarding.
    *   If the domain is associated with an educational institute or job title is Dean/Professor: Tag as **B2B Opportunity** and mark as SQL.
*   **Sales Routing (B2B)**:
    *   If B2B SQL, trigger an automated Slack notification to the Sales channel:
        > 🚨 **New B2B Lead for VivaExams**: Dean Rajat from AMET University just signed up. Domain: `ametuniv.edu.in`.
    *   Assign the lead to an Enterprise Account Executive (AE) using round-robin routing logic.

#### 3. Sales Demo & Negotiation (SQL to Opportunity)
*   **Demo Stage**: AE presents the B2B Institutional Dashboard (which allows professors to custom-build mock exams, auto-grade ship cadets, and check proctoring logs).
*   **Deal Creation**: Create a Deal in the "AMET 500 Cadets License" pipeline with value $7,500.

#### 4. Closing & Provisioning (Opportunity to Customer)
*   **Contract Sign-off**: AE sends a DocuSign agreement.
*   **Billing & Activation**:
    *   Customer pays via a Stripe invoice.
    *   Stripe webhook `invoice.payment_succeeded` fires.
    *   An API route calls our database to:
        1. Convert the org account to `active_subscription`.
        2. Provision 500 cadet seats.
        3. Email the Dean onboarding access.
    *   Update HubSpot Deal status to **Closed Won**.

#### 5. Success, Expansion & Renewal (Retention)
*   **Health Scoring**: Monitor user log-ins. If cadets mock-test usage drops by 50%, alert the Customer Success manager.
*   **Upsell Trigger**: If seat usage reaches 95% (e.g., 475/500 seats), trigger an automated in-app upsell notification asking to add 50 seats.
*   **Renewal**: Automate annual contract renewal notification 60 days before contract expiry.