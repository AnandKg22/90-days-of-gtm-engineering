# Exercises - Day 016: n8n Workflow Blueprint

This document details the visual node sequence configuration designed inside the n8n orchestrator dashboard.

---

## 🗺️ n8n Visual Workflow Node Sequence

The diagram below details how data flows sequentially from the webhook trigger through JavaScript parsing, enrichment APIs, conditional filters, CRM inserts, and Slack alerts:

```
                  ┌──────────────────────┐
                  │ 1. Webhook Trigger   │
                  │ (POST /stripe-hook)  │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │ 2. JavaScript Code   │
                  │ (Parse Email Domain) │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │ 3. HTTP Request Node │
                  │  (Query Apollo.io)   │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │    4. IF Filter      │
                  │ (Employees > 50?)    │
                  └──────┬────────────┬──┘
                         │            │
                  (True) │            │ (False)
                         ▼            ▼
        ┌───────────────────┐      ┌───────────────────┐
        │5. HubSpot Company │      │7. ActiveCampaign  │
        │   (Upsert Deal)   │      │(Nurture Sequence) │
        └────────┬──────────┘      └───────────────────┘
                 │
                 ▼
        ┌───────────────────┐
        │6. Slack Channel   │
        │   (Alert Rep)     │
        └───────────────────┘
```

---

## ⚙️ Detailed Node Parameters

### 1. Webhook Trigger Node
*   **Method**: `POST`
*   **Path**: `stripe-payment`
*   **Response Mode**: `On Received` (returns `200 OK` instantly to Stripe).

### 2. Code Node (JavaScript)
Extracts the email domain and normalizes the input:
```javascript
// Extract domain from billing email
const item = items[0].json;
const email = item.customer_email;
item.domain = email.split('@')[1];
return [{ json: item }];
```

### 3. HTTP Request Node (Apollo)
*   **Method**: `POST`
*   **URL**: `https://api.apollo.io/v1/people/match`
*   **Headers**: `X-Api-Key: ******`
*   **Body**: `{"email": "{{ $json.customer_email }}"}`

### 4. IF Node
*   **Conditions**: Number `{{ $json.organization.estimated_num_employees }}` is greater than `50`.

### 5. HubSpot Company Node (True Branch)
*   **Resource**: `Company`, **Operation**: `Create or Update`.
*   **Mapped Properties**: Name: `{{ $json.organization.name }}`, Target Seats: `{{ $json.quantity }}`.

### 6. Slack Node (True Branch)
*   **Text**: `🏆 *New Deal Closed Won!* Company: {{ $json.organization.name }} | Seats: {{ $json.quantity }}`
