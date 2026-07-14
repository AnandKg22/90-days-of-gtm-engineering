# Day 001: Introduction to GTM Engineering

## Objective
Understand what GTM Engineering actually is.

## Topics Covered
- What is Go-To-Market?
- Product vs GTM
- Why startups hire GTM Engineers
- Revenue as an engineering problem
- Traditional engineering vs GTM engineering

## Subtopics
- Customer acquisition
- Customer activation
- Customer retention
- Expansion revenue
- Revenue flywheel

---

## 🛠️ Practical Exercise: B2B Customer Journey

In this exercise, we map the chronological lifecycle of a customer, identifying key commercial systems and transition triggers:

1.  **Visitor**: Anonymous session on the site. Tracked via [Segment](https://segment.com) and IP enrichment.
2.  **Lead**: Visitor fills out a signup form. Data is pushed to HubSpot CRM.
3.  **Qualified Lead (SQL)**: Profile is enriched via Apollo API and passes the scoring threshold.
4.  **Meeting**: SQL books a demo call using a Calendly scheduling link.
5.  **Opportunity**: Sales AE qualifies the call and creates a HubSpot Deal.
6.  **Customer**: Opportunity is marked "Closed Won" after Stripe invoice payment confirmation.
7.  **Expansion**: CS monitors limits, triggering auto-upsells for extra seats via Stripe billing.
8.  **Renewal**: Agreement is renewed annually using automated DocuSign webhooks.

*View complete documentation in [Exercises.md](Exercises.md).*

---

## 🏫 Daily Project / Assignment: VivaExams GTM Design

We designed a GTM data pipeline for the **VivaExams** mock-exam prep platform:
*   **B2C Self-Serve**: Focuses on direct checkout. When a student purchases a mock test, Stripe triggers a webhook to provision the user instantly.
*   **B2B Enterprise**: Targets maritime colleges. College admin leads are identified by their email domains (e.g. `.edu.in`), triggering high-value sales alerts in Slack and assigning leads to Account Executives via round-robin routing.

*View the full specification in [Assignment.md](Assignment.md) and the system diagram in [Architecture.md](Architecture.md).*

---

## 📂 Expected Deliverables
*   📝 [Day 1 Study Notes](Notes.md) — Comprehensive details on GTM Engineering fundamentals.
*   📝 [Customer Journey Mapping](Exercises.md) — Transition triggers and system states.
*   📝 [VivaExams GTM Specification](Assignment.md) — B2B and B2C operational designs.
*   📊 [GTM Stack Diagram](Architecture.md) — Visual flow chart mapping webhooks, HubSpot, and databases.

---

## 📝 Notes & Reflection
*   **Key Insight**: Revenue operations is a software pipeline. By automating integrations between billing, databases, and CRMs, we reduce manual sales load and scale cash flow.
*   **Study Log**: Read more in [Notes.md](Notes.md).
*   **Daily Log**: Read reflections in [Reflection.md](Reflection.md).
