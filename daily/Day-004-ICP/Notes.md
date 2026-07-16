# Study Notes - Day 004: Ideal Customer Profile (ICP)

Today's studies focused on defining and implementing Ideal Customer Profiles (ICP), Buyer Personas, and User Personas to build high-performance lead filters.

---

## 1. ICP, Buyer Persona, and User Persona

Commercial targeting operates at three distinct levels:

```
[ IDEAL CUSTOMER PROFILE (ICP) ] ──> Organization Level (e.g., Maritime Colleges)
              │
              ▼
[ BUYER PERSONAS ] ───────────────> Decision Maker Level (e.g., Dean, CFO)
              │
              ▼
[ USER PERSONAS ] ────────────────> End User Level (e.g., Cadets, Instructors)
```

1.  **Ideal Customer Profile (ICP)**: Focuses on the **company** (firmographics). It describes the characteristics of organizations that get the highest value from your product and represent the highest LTV (e.g. Company Size: 100–500, Industry: B2B FinTech).
2.  **Buyer Persona**: Focuses on the **decision-makers** who sign the contract (e.g. Dean of Admissions, CFO). They care about business ROI, pricing, contract terms, and compliance.
3.  **User Persona**: Focuses on the **end-users** who use the software daily (e.g. Cadets, Maritime Instructors). They care about UI/UX, ease of use, grading accuracy, and workflow speed.

---

## 2. Deep-Dive: ICP Subtopics

To automate lead scoring, a GTM Engineer must program criteria based on these six subtopics:

### 1. Industry
*   **Definition**: The business sector the company operates in (e.g., Maritime Shipping, FinTech, Cybersecurity).
*   **GTM Application**: We normalize raw industry data (which can be messy) into standardized tags in our database to ensure proper routing rules.

### 2. Company Size
*   **Definition**: The scale of the company, measured by employee count (e.g., 50–200 employees) or branch count.
*   **GTM Application**: Size dictates the sales tier. Small companies go to automated B2C checkouts, while mid-market/enterprise companies go to sales reps.

### 3. Revenue
*   **Definition**: The Annual Recurring Revenue (ARR) of the target company.
*   **GTM Application**: Used to qualify purchasing power. Companies below a certain revenue threshold are disqualified from high-touch enterprise sales.

### 4. Technology (Technographics)
*   **Definition**: The software stack and developer tools used by the target company (e.g. uses Salesforce, Stripe, Next.js).
*   **GTM Application**: We write scraping algorithms to look for specific JavaScript SDKs on homepages or query job postings to find target tech stacks.

### 5. Pain Points
*   **Definition**: The operational problems the target company is struggling to solve (e.g., slow mock exam grading, high drop-out rates, manual lead entry errors).
*   **GTM Application**: Leads are segmented by pain points so that AI SDR agents draft emails speaking directly to those issues.

### 6. Buying Signals
*   **Definition**: Trigger events showing high intent or growth (e.g. hiring new instructors, raising a Series A funding round, or opening a new training branch).
*   **GTM Application**: Web scraping tools monitor news feeds and job boards. When a signal is detected, the lead score is bumped, and an automated outreach sequence begins.
