# Exercises - Day 033: LTV:CAC Efficiency Calculations

This document details the step-by-step mathematical calculations used to compute Customer Acquisition Cost (CAC), Lifetime Value (LTV), and Payback Periods.

---

## 🧮 GTM Efficiency Math Scenario

We analyze a SaaS campaign run during **Q1 2026** with the following metrics:

### 1. Inbound Campaign Metrics
*   **Total Sales & Marketing Spend**: **$50,000.00**
*   **Customers Acquired**: 50.
*   **Average Revenue Per User (ARPU)**: **$100.00/month** ($1,200.00/year).
*   **Gross Margin**: **80.0%** (Hosting & support costs account for 20%).
*   **Annual Churn Rate**: **10.0%** (average customer lifespan is 10 years).

---

## 📐 Step-by-Step Calculations

### 1. Calculate Customer Acquisition Cost (CAC)
$$\text{CAC} = \frac{\text{Sales \& Marketing Spend}}{\text{Customers Acquired}}$$
$$\text{CAC} = \frac{\$50,000.00}{50} = \mathbf{\$1,000.00}$$

### 2. Calculate Lifetime Value (LTV)
$$\text{LTV} = \frac{\text{ARPU (Annual)} \times \text{Gross Margin (\%) }}{\text{Annual Churn Rate}}$$
$$\text{LTV} = \frac{\$1,200.00 \times 0.80}{0.10} = \frac{\$960.00}{0.10} = \mathbf{\$9,600.00}$$

### 3. Calculate LTV:CAC Ratio
$$\text{LTV:CAC} = \frac{\text{LTV}}{\text{CAC}}$$
$$\text{LTV:CAC} = \frac{\$9,600.00}{\$1,000.00} = \mathbf{9.6\text{x}}$$

*   **Insight**: 9.6x LTV:CAC indicates an highly efficient funnel (above the 3.0x SaaS target benchmark).

### 4. Calculate CAC Payback Period (Months)
$$\text{Payback Period} = \frac{\text{CAC}}{\text{ARPU (Monthly)} \times \text{Gross Margin (\%) }}$$
$$\text{Payback Period} = \frac{\$1,000.00}{\$100.00 \times 0.80} = \frac{\$1,000.00}{\$80.00} = \mathbf{12.5\text{ Months}}$$

*   **Insight**: It takes 12.5 months of subscription fees for an acquired customer to break even and cover their marketing costs.
