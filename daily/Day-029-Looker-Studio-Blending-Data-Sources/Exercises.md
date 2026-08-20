# Exercises - Day 029: Looker Data Blending Blueprints

This document details the data source blending configurations designed to merge CRM records with billing transactions inside the Looker Studio canvas.

---

## 🎨 Looker Data Blending Panel Blueprint

To evaluate customer conversion rates, we construct a data blend joining HubSpot and Stripe sources:

```
┌─────────────────────────────────┐           ┌─────────────────────────────────┐
│     Table 1: HubSpot Contacts   │           │     Table 2: Stripe Payments    │
│  (Dimensions: email, source)   │           │ (Dimensions: customer_email)    │
│                                 │           │ (Metrics: amount_paid)          │
└────────────────┬────────────────┘           └────────────────┬────────────────┘
                 │                                             │
                 │              Left Outer Join                │
                 └──────────────► [ JOIN KEY ] ◄───────────────┘
                     email <==> customer_email
```

### Blend Configuration Table:
*   **Data Source 1 (Left Table)**: `HubSpot CRM Contacts`
    *   *Dimensions*: `email`, `lead_source`, `employees`
*   **Data Source 2 (Right Table)**: `Stripe Billing Charges`
    *   *Dimensions*: `customer_email`, `plan_tier`
    *   *Metrics*: `amount`
*   **Join Operator**: **Left Outer Join**
*   **Join Key Mappings**: `email` (HubSpot) <==> `customer_email` (Stripe)

---

## 💡 Left Outer Join vs. Inner Join in GTM

*   **Left Outer Join (Correct)**: Retains all prospects from the HubSpot table, even if they have not completed a Stripe checkout. Non-paying leads show `amount = NULL`. This is necessary to calculate **Lead-to-Customer conversion rates** (e.g. 100 total leads, 10 paid leads = 10% conversion).
*   **Inner Join (Incorrect)**: Abruptly drops any lead record without a matching Stripe checkout. The combined table only shows paying customers, making it impossible to calculate conversion rates or analyze non-converting lead channels.
