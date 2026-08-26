# Exercises - Day 032: NDR & GRR Cohort Calculations

This document details the mathematical calculations used to compute Net Dollar Retention (NDR) and Gross Dollar Retention (GRR) across a 12-month cohort window.

---

## 🧮 Cohort Retention Math Scenario

We analyze a customer cohort acquired in **January 2025** and evaluate their contract changes in **January 2026**:

### 1. Cohort Parameters
*   **Starting Cohort Size**: 10 companies.
*   **Starting Cohort MRR (Jan 2025)**: **$50,000.00**

### 2. Cohort Revenue Movements (by Jan 2026)
*   **Expansion MRR (Upgrades)**: **+$10,000.00** (3 companies purchased more cadet seats).
*   **Contraction MRR (Downgrades)**: **-$4,000.00** (2 companies reduced support tiers).
*   **Churned MRR (Cancellations)**: **-$5,000.00** (1 company cancelled their subscription).
*   **Flat MRR**: 4 companies kept their contracts unchanged.

---

## 📐 Step-by-Step Calculations

### 1. Calculate Net Dollar Retention (NDR)
$$\text{NDR} = \frac{\text{Starting MRR} + \text{Expansion} - \text{Contraction} - \text{Churn}}{\text{Starting MRR}} \times 100$$
$$\text{NDR} = \frac{\$50,000.00 + \$10,000.00 - \$4,000.00 - \$5,000.00}{\$50,000.00} \times 100$$
$$\text{NDR} = \frac{\$51,000.00}{\$50,000.00} \times 100 = \mathbf{102.0\%}$$

*   **Insight**: NDR > 100% indicates Net Negative Churn. The customer base grew without acquiring new accounts.

### 2. Calculate Gross Dollar Retention (GRR)
$$\text{GRR} = \frac{\text{Starting MRR} - \text{Contraction} - \text{Churn}}{\text{Starting MRR}} \times 100$$
$$\text{GRR} = \frac{\$50,000.00 - \$4,000.00 - \$5,000.00}{\$50,000.00} \times 100$$
$$\text{GRR} = \frac{\$41,000.00}{\$50,000.00} \times 100 = \mathbf{82.0\%}$$

*   **Insight**: GRR cannot exceed 100%. A GRR of 82.0% means we retain 82.0% of our baseline revenue before factoring in upsells.
