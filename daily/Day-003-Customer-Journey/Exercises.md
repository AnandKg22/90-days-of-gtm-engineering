# Exercises - Day 003: CloudSentry Customer Journey Map

This document maps out the B2B SaaS customer journey for **CloudSentry**, an AI-powered cloud cost optimization and security compliance platform.

---

## 🗺️ CloudSentry Customer Lifecycle Funnel

The journey of a target account going from initial discovery to an expanded enterprise customer:

```
[ Visitor / Lead ] ──────(Enrichment & Fit)──────> [ Qualified SQL ]
                                                         │
                                               (Demo / Sandbox Trial)
                                                         ▼
[ Expanded Customer ] ◄───(Upgrade/Renewal)─── [ Active Customer ]
```

---

### Stage-by-Stage Journey Details

#### 1. Awareness (Discovery)
*   **Touchpoint**: A DevOps Engineer or VP of Engineering searches for "reduce AWS cost anomalies" or "SOC2 compliance requirements for cloud multi-tenant systems" and lands on a CloudSentry technical blog post or reads a recommendation on Hacker News.
*   **Data Captured**: Referral channel/keyword, IP-based company name lookup (e.g. via Clearbit/Koala), landing page URL, and page view count.

#### 2. Interest (Lead Capture)
*   **Touchpoint**: The visitor downloads the whitepaper "The Ultimate B2B SaaS Cloud Infrastructure Compliance Guide" or signs up for CloudSentry's monthly "DevOps Costs Digest" newsletter.
*   **Data Captured**: Name, work email address, company name, primary cloud hosting provider.
*   **System Action**: The contact is recorded in the CRM, tagged as a `Lead`, and entered into an automated email nurture track demonstrating CloudSentry's value.

#### 3. Consideration (Enrichment & Fit)
*   **Touchpoint**: The lead returns to the site, visits the `/pricing` page, and browses the `/features/security-audits` page.
*   **Data Captured**: Pricing page views, time spent on the features page, pricing calculator inputs.
*   **System Action**: An enrichment webhook (using Clearbit or Apollo) pulls company metadata. Because the company size is > 50 employees and uses AWS, the system triggers a Slack alert for the sales team and transitions the lead stage to **SQL (Sales Qualified Lead)**.

#### 4. Evaluation (Demo & Sandbox Trial)
*   **Touchpoint**: The SQL books a live product demonstration using the embedded Chili Piper scheduler or spins up a 14-day free trial workspace connected to a test AWS account.
*   **Data Captured**: Demo booking details, AWS IAM integration checklist completions, test scan triggers.
*   **System Action**: The opportunity is created in the CRM pipeline, and an Account Executive (AE) is assigned to manage the account. Stage changes to **Opportunity**.

#### 5. Purchase (Closed Won / Customer)
*   **Touchpoint**: The VP of Engineering signs the Enterprise Service Agreement, passes the security review, and pays the subscription fee via Stripe (or DocuSign for enterprise contracts).
*   **Data Captured**: Signed contract metadata, Stripe customer and transaction IDs, subscription tier.
*   **System Action**: The lifecycle stage in the CRM is updated to **Customer**. An automated provisioning webhook triggers, creating their dedicated tenant workspace and activating production API integrations.

#### 6. Onboarding (First Value / Activation)
*   **Touchpoint**: The customer connects their production cloud accounts (AWS/GCP/Azure), invites team members, and configures the Slack/PagerDuty notification channel to receive cost alerts.
*   **Data Captured**: Number of connected cloud accounts, number of active team seats, Slack integration status.
*   **Activation Event**: The system records the first "cost optimization scan" run, which identifies at least $1,000 in monthly potential savings (reaching the "Aha! moment").

#### 7. Adoption (Regular Usage)
*   **Touchpoint**: The DevOps team logs in multiple times per week to check dashboards, resolve security recommendations, and export weekly compliance reports.
*   **Data Captured**: Daily Active Users (DAU), recommendation resolution rate, number of reports generated.

#### 8. Expansion & Renewal (Growth)
*   **Touchpoint**: After 12 months, the customer expands their footprint by adding Google Cloud Platform (GCP) and Azure accounts to CloudSentry, or upgrading to the Premium Compliance module (enabling automated HIPAA and FedRAMP audits), renewing their annual contract.
*   **Data Captured**: Expansion deal size, new contract terms, renewed contract date.