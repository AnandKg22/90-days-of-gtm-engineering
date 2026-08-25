# Exercises - Day 031: Subscription MRR Waterfall Calculations

This document details the step-by-step mathematical calculations used to compile Monthly Recurring Revenue (MRR) waterfalls.

---

## 📋 MRR Waterfall Math Equations

*   **Net New MRR**:
    $$\text{Net New MRR} = \text{New MRR} + \text{Expansion MRR} - \text{Contraction MRR} - \text{Churned MRR}$$
*   **Ending MRR**:
    $$\text{Ending MRR} = \text{Starting MRR} + \text{Net New MRR}$$
*   **Annual Recurring Revenue (ARR) Run Rate**:
    $$\text{ARR} = \text{Ending MRR} \times 12$$

---

## 🧮 Step-by-Step Monthly Financial Scenario

### 1. Starting Metrics
*   **Starting Month MRR**: **$10,000.00**

### 2. Subscription Movements during the Month
*   **Customer A**: Upgrades license count from $500.00/mo to $800.00/mo.
    *   *Classification*: **Expansion MRR** = **+$300.00**
*   **Customer B**: Cancels subscription entirely (old contract value: $400.00/mo).
    *   *Classification*: **Churned MRR** = **-$400.00**
*   **Customer C**: Signs up for new cadet licenses worth $1,200.00/mo.
    *   *Classification*: **New MRR** = **+$1,200.00**
*   **Customer D**: Downgrades support package from $600.00/mo to $400.00/mo.
    *   *Classification*: **Contraction MRR** = **-$200.00**

### 3. Net New MRR Evaluation
$$\text{Net New MRR} = \$1,200.00 + \$300.00 - \$200.00 - \$400.00 = \mathbf{+\$900.00}$$

### 4. Ending Month Metrics
*   **Ending Month MRR**: $\$10,000.00 + \$900.00 = \mathbf{\$10,900.00}$
*   **ARR Run Rate**: $\$10,900.00 \times 12 = \mathbf{\$130,800.00}$
