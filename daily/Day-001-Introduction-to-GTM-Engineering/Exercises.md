# Exercises - Day 001: Customer Journey Mapping

This document contains the completed practical exercise mapping the complete customer journey.

---

## 🏃 B2B SaaS Customer Acquisition Journey

Below is the step-by-step lifecycle of a lead, detailing the target state, systems involved, and data captured at each transition point:

```
[ Visitor ] ─────────(Sign-up / Lead Gen)──────────> [ Lead ]
                                                          │
                                                    (Enrich & Score)
                                                          ▼
[ Meeting ] ◄────────(Book Demo / Calendly)───────── [ Qualified Lead ]
     │
(Sales Demo)
     ▼
[ Opportunity ] ─────(Quote / SOW signed)──────────> [ Customer ]
                                                          │
                                                    (Cross-sell / Upsell)
                                                          ▼
[ Renewal ] ◄────────(Annual Billing Contract)────── [ Expansion ]
```

---

### 1. Visitor (TOFU - Awareness)
*   **Definition**: A unique browser session landing on the marketing website.
*   **Data Captured**: IP address (leads to firmographic reverse lookup), traffic source (UTM parameters), page paths visited.
*   **Systems**: Google Analytics, Segment, Clearbit Reveal (IP lookup).

### 2. Lead (TOFU - Intake)
*   **Transition Trigger**: Visitor fills out a lead capture form (e.g. downloads an ebook or registers for a webinar).
*   **Data Captured**: Email, first name, last name, company domain, job role.
*   **Systems**: HubSpot Marketing Hub, Webhook Intake Server.

### 3. Qualified Lead (MQL/SQL - Evaluation)
*   **Transition Trigger**: Lead profile is enriched and passes scoring thresholds.
    *   *MQL (Marketing Qualified)*: Downloaded multiple guides, visited pricing page (tracked in CRM).
    *   *SQL (Sales Qualified)*: Passes firmographic ICP criteria (matched by the Lead Scoring Engine).
*   **Data Captured**: Company size, tech stack, funding, buyer intent score.
*   **Systems**: CRM (HubSpot/Salesforce), Apollo/Clearbit enrichment APIs.

### 4. Meeting (MOFU - Sales Engagement)
*   **Transition Trigger**: Lead books a product demonstration call (e.g., via Calendly or HubSpot Meetings link).
*   **Data Captured**: Meeting date/time, customer pain points stated, meeting notes.
*   **Systems**: Calendly, Google Calendar, HubSpot Contacts, Zoom/Gong.io call recording.

### 5. Opportunity (BOFU - Deal Negotiation)
*   **Transition Trigger**: Sales representative qualifies the meeting and creates a Deal record in the sales pipeline.
*   **Data Captured**: Estimated deal size ($ value), close date, pipeline stage (e.g., Proposal Sent), competitor names.
*   **Systems**: Salesforce Sales Cloud / HubSpot Deals.

### 6. Customer (BOFU - Won Revenue)
*   **Transition Trigger**: Deal stage changes to "Closed Won". Customer signs the contract, and billing account is created.
*   **Data Captured**: Contract Start/End date, payment details, subscription plan tier.
*   **Systems**: DocuSign, Stripe Billing, Product PostgreSQL Database.

### 7. Expansion (CS - Value Expansion)
*   **Transition Trigger**: Customer hits usage limits or wants additional modules, buying upgrades.
*   **Data Captured**: Expanded MRR delta, add-on purchase details.
*   **Systems**: Stripe Billing, HubSpot Deals (Upsell pipeline).

### 8. Renewal (CS - Retention)
*   **Transition Trigger**: Customer signs an annual renewal contract, or subscription auto-renews.
*   **Data Captured**: Contract renewal date, new billing terms.
*   **Systems**: Stripe, CRM, DocuSign.