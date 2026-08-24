# Exercises - Day 030: Cohort Retention Charts

This document details the Cohort Retention Grid Matrix and SaaS engagement formulas used to audit customer stickiness.

---

## 📊 Cohort Weekly Retention Matrix

This grid displays the percentage of acquired users who remain active in subsequent weeks:

| Cohort Signup Week | Total Users | Week 0 (Signup) | Week 1 | Week 2 | Week 3 | Retention Trend |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`2026-07-01`** | `100` | `100.0%` | `60.0%` | `45.0%` | `30.0%` | Strong onboarding; gradual drop. |
| **`2026-07-08`** | `150` | `100.0%` | `50.0%` | `30.0%` | `20.0%` | Sharp drop in Week 1; suggests onboarding friction. |

---

## ⚙️ SaaS Engagement Telemetry Formulas

To audit product stickiness, GTM dashboard widgets calculate these ratios:

### 1. Daily Active Users (DAU)
*   **Formula**: `COUNT(DISTINCT user_id) WHERE timestamp IN [last_24_hours]`
*   **Definition**: Number of unique users logging in during a single day.

### 2. Monthly Active Users (MAU)
*   **Formula**: `COUNT(DISTINCT user_id) WHERE timestamp IN [last_30_days]`
*   **Definition**: Number of unique active users in a 30-day window.

### 3. User Stickiness Ratio (%)
*   **Formula**: `(DAU / MAU) * 100`
*   **Definition**: The percentage of monthly active users who engage on a daily basis.
    *   *Example*: DAU = 20, MAU = 100. Stickiness = 20%. This means the average active user logs in 6 days a month. Stickiness > 20% is the target benchmark for healthy B2B SaaS.
