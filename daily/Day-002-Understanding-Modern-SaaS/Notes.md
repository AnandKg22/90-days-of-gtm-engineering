# Study Notes - Day 002: Understanding Modern SaaS

Today's studies focused on SaaS business mechanics, billing structures, and the mathematical formulas governing subscription unit economics.

---

## 1. SaaS Subscription Models & Billing

SaaS revenue relies on predictability. As a GTM Engineer, you will configure billing systems to handle:

### Monthly Billing (Contractual flexibility)
*   **Customer Experience**: Pays every 30 days. High flexibility to upgrade, downgrade, or cancel.
*   **Financial Impact**: Drives high MRR but exposes the business to higher churn rates.

### Annual Billing (Cash flow optimization)
*   **Customer Experience**: Pays for 12 months upfront, usually receiving a discount (e.g. 20% off).
*   **Financial Impact**: Lowers churn risk, provides instant cash flow for customer acquisition reinvestment, but requires deferred revenue accounting (recognizing $1/12$ of the contract value each month).

---

## 2. Gross vs. Net Revenue & Expansion

*   **Gross Revenue**: The total amount of money billed to customers before any deductions, discounts, or processing fees.
*   **Net Revenue**: Gross revenue minus discounts, refunds, chargebacks, and transaction fees.
*   **Expansion Revenue**: Additional revenue generated from existing customers. This is the holy grail of SaaS because the CAC to acquire this revenue is near $0. Driven by:
    *   **Seat Expansion**: Adding more users.
    *   **Feature Upgrades**: Upgrading from Basic to Enterprise.
    *   **Usage Overages**: Charging for data volume or API calls.

---

## 3. Core SaaS Financial Formulas

A GTM Engineer must program these formulas into analytics dashboards:

### 1. Monthly & Annual Recurring Revenue
*   **MRR (Monthly Recurring Revenue)**:
    $$MRR = \\sum (Active \\; Subscriptions \\times Monthly \\; Fees)$$
*   **ARR (Annual Recurring Revenue)**:
    $$ARR = MRR \\times 12$$

### 2. Churn Rate (Revenue & Logo)
*   **Logo Churn Rate**: The percentage of customers who cancel their account.
    $$Logo \\; Churn \\; \\% = \\frac{Cancellations \\; in \\; Period}{Total \\; Customers \\; at \\; Start \\; of \\; Period} \\times 100$$
*   **Net Revenue Churn Rate**: The percentage of revenue lost after accounting for expansion.
    $$Net \\; Revenue \\; Churn \\; \\% = \\frac{Churned \\; MRR - Expansion \\; MRR}{Starting \\; MRR} \\times 100$$
    *Note: If Net Churn is negative (e.g., -5%), it means Expansion exceeded lost revenue. This is called **Negative Churn**.*

### 3. Customer Acquisition Cost & Lifetime Value
*   **CAC (Customer Acquisition Cost)**:
    $$CAC = \\frac{Total \\; Sales \\; \\& \\; Marketing \\; Costs}{New \\; Customers \\; Acquired}$$
*   **LTV (Lifetime Value)**:
    $$LTV = \\frac{Average \\; Revenue \\; Per \\; Account \\; (ARPU) \\times Gross \\; Margin \\%}{Logo \\; Churn \\; Rate}$$

### 4. Payback Period
*   **CAC Payback Period (Months)**:
    $$Payback \; Period = \frac{CAC}{ARPU \times Gross \; Margin \%}$$

---

## 4. Deep-Dive: SaaS Subtopics

To master modern SaaS economics, a GTM Engineer must implement database schemas and logic supporting these five billing subtopics:

### 1. Monthly Billing
*   **Definition**: A subscription schedule where customers are charged automatically every 30 days.
*   **GTM Application**: High churn risk but lower friction to acquire. The billing engine must handle failed monthly card charges (dunning cycles) and automate trial-to-paid conversion schedules.

### 2. Annual Billing
*   **Definition**: A contract schedule where the user pays for a full year upfront, usually receiving a discount (e.g., 10%–20%).
*   **GTM Application**: Greatly increases cash flow (upfront cash to reinvest in CAC) and reduces churn. The GTM database must track both *deferred revenue* (liability on books) and *recognized revenue* ($1/12$ of contract value released each month).

### 3. Gross Revenue
*   **Definition**: The total, raw invoiced value billed to customers before accounting for any operational expenses, merchant fees, or refunds.
*   **GTM Application**: The starting metric for sales funnel conversions. Used to analyze top-line sales growth.

### 4. Net Revenue
*   **Definition**: The actual cash retained by the business after subtracting merchant processing fees (e.g. Stripe's 2.9% + $0.30), refunds, chargebacks, and coupon discounts.
*   **GTM Application**: Net revenue determines the actual margin available to fund operations and customer acquisition.
    $$Net \; Revenue = Gross \; Revenue - Refunds - Discounts - Processing \; Fees$$

### 5. Expansion Revenue
*   **Definition**: Recurring revenue generated from existing customer accounts through account upgrades, add-on features, seat increases, or usage overages.
*   **GTM Application**: The key to achieving **Net Negative Churn**. When expansion revenue exceeds the revenue lost from churned customers, the business grows naturally even without acquiring new logos.
