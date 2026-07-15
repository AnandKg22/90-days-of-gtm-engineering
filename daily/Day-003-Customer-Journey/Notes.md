# Study Notes - Day 003: Customer Journey

Today's studies focused on mapping user progression across the complete lifecycle and analyzing touchpoints, buyer intent, and B2B committee decision-making.

---

## 1. The 8 Stages of the Customer Lifecycle

The SaaS customer lifecycle progresses through eight distinct milestones:

1.  **Awareness**: The user discovers the product (via ads, blogs, social media, or organic search).
2.  **Interest**: The user shows active engagement (signs up for a newsletter, downloads a whitepaper).
3.  **Consideration**: The user compares solutions (visits pricing page, reads competitive reviews).
4.  **Evaluation**: The user signs up for a free trial or requests a sandbox demo.
5.  **Purchase**: The user signs the agreement and pays the initial subscription invoice.
6.  **Onboarding**: The customer sets up their workspace and completes the initial configurations.
7.  **Adoption**: The customer uses the product daily, integrating it into their core operations.
8.  **Expansion**: The customer buys upgrades, seats, or add-ons, increasing customer lifetime value.

---

## 2. Deep-Dive: Customer Journey Subtopics

As a GTM Engineer, you must track, log, and analyze customer behaviors. The core subtopics are detailed below:

### 1. Customer Touchpoints
*   **Definition**: Any interaction or contact point between the prospect and the company (e.g. ad click, blog post read, lead magnet download, sales email reply, demo call, support ticket).
*   **GTM Application**: Touchpoints must be logged to a central database to build **Attribution Models** (First-Touch, Last-Touch, U-Shaped). This tells marketing which touchpoints actually generate revenue.

### 2. Buyer Intent
*   **Definition**: Behavior signals that indicate a prospect's readiness to buy (e.g., visiting the `/pricing` page 3 times, viewing a comparison sheet, researching security compliance documents, or searching for your company on G2/Capterra).
*   **GTM Application**: We write scraping scripts or hook into intent providers (like Bombora or Koala) to capture these signals. If a company domain shows high intent, our router automatically alerts the sales rep to do outbound outreach.

### 3. Decision Making (B2B Committee Dynamics)
*   **Definition**: Unlike B2C, B2B purchasing decisions are made by a group (usually 6–10 stakeholders) called the **Buying Committee**.
*   **GTM Application**: You must design the CRM database to link and categorize committee members:
    *   **The Champion**: The end-user who loves the product and pushes it internally.
    *   **The Economic Buyer**: The executive (CFO/VP) who signs the check.
    *   **The Technical Blocker**: The IT/Security director who audits compliance (SOC2/SSO).
    *   **The Influencer**: Department managers whose teams will use the tool.
