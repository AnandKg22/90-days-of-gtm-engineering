# Study Notes - Day 006: B2B Sales Fundamentals

Today's studies focused on sales pipelines, deal progression, CRM object lifecycle states, and mathematical forecasting models.

---

## 1. Sales Pipeline Object States

In B2B sales, a deal flows through several standard lifecycle definitions:

*   **Lead**: An individual contact who has shown initial interest but is not yet qualified (e.g. downloaded a whitepaper).
*   **Prospect**: A qualified lead whom sales is actively trying to engage (e.g. outreach emails sent).
*   **Opportunity (Deal)**: A qualified prospect who has agreed to a demo call. A financial value and target close date are assigned to the record.
*   **Closed Won**: The prospect signed the contract, paid the invoice, and is now a paying customer.
*   **Closed Lost**: The opportunity did not buy, and the sales cycle is closed. Reasons are captured for analysis (e.g., pricing, competitor, timing).

---

## 2. Deep-Dive: Sales Fundamentals Subtopics

To automate CRM pipelines, a GTM Engineer must master these three subtopics:

### 1. The Sales Funnel
*   **Definition**: A visual model showing the volumetric drop-off of leads as they move from top-of-funnel (awareness) to bottom-of-funnel (purchase).
*   **GTM Application**: We write queries to calculate **Conversion Rates** between stages (e.g., Lead-to-Meeting conversion, Meeting-to-Closed-Won conversion) to identify where deals are getting stuck.

### 2. Pipeline Stages
*   **Definition**: The specific, sequential steps a deal traverses in the CRM pipeline (e.g. *Discovery Scheduled*, *Proposal Sent*, *Contract Review*).
*   **GTM Application**: Each stage has an associated **Win Probability %** based on historical sales data. As a deal progresses, its probability of closing increases.

### 3. Revenue Forecasting (Weighted Pipeline)
*   **Definition**: Estimating future closed-won revenue based on active deals, close dates, and win probabilities.
*   **GTM Application**: The GTM Engineer builds dashboards that calculate the **Weighted Pipeline Value**. Rather than simply summing deal values, we multiply each deal value by its stage's win probability:
    $$Weighted \; Pipeline = \\sum (Deal \; Value \\times Stage \; Win \; Probability \\%)$$
    *Example: A $10,000 deal in "Proposal Sent" (60% win probability) is forecasted as $6,000 in expected revenue.*
