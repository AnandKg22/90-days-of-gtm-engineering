# Exercises - Day 035: Attribution Model Revenue Allocations

This document details the revenue distributions across marketing channels under different attribution models.

---

## 📋 Customer Touchpoint History Scenario

We analyze a customer journey that concluded with a **$10,000.00** conversion:
*   **Touchpoint 1 (Day 1)**: `Google Ads` (First touch).
*   **Touchpoint 2 (Day 5)**: `Email Newsletter` (Middle touch).
*   **Touchpoint 3 (Day 10)**: `LinkedIn Ads` (Last touch/Conversion event).

---

## 📊 Revenue Allocation Matrix ($10,000.00 Deal)

This grid compares how credit is distributed across marketing channels:

| Attribution Model | Google Ads (Touch 1) | Email Newsletter (Touch 2) | LinkedIn Ads (Touch 3) | Model Allocation Logic |
| :--- | :--- | :--- | :--- | :--- |
| **`First Touch`** | **`$10,000.00`** (100%) | `$0.00` (0%) | `$0.00` (0%) | 100% of credit goes to the initial click. |
| **`Last Touch`** | `$0.00` (0%) | `$0.00` (0%) | **`$10,000.00`** (100%) | 100% of credit goes to the closing click. |
| **`Linear`** | **`$3,333.33`** (33.3%) | **`$3,333.33`** (33.3%) | **`$3,333.33`** (33.3%) | Revenue is split equally among all touchpoints. |
| **`U-Shaped`** | **`$4,000.00`** (40%) | **`$2,000.00`** (20%) | **`$4,000.00`** (40%) | 40% to first, 40% to last, 20% to middle. |

---

## ⚙️ Model Insights

*   **First Touch Bias**: Over-values discovery channels, underestimating the impact of SDR nurturing and late-stage retargeting campaigns.
*   **Last Touch Bias**: Over-values high-intent closing channels (e.g. direct traffic, branded search), while ignoring early-stage discovery campaigns.
*   **U-Shaped Balance**: Standard B2B default because it gives high credit to the introduction and closing touchpoints while rewarding nurturing channels in the middle.
