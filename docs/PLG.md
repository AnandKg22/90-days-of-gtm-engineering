# Product-Led Growth (PLG) & Telemetry

Product-Led Growth shifts customer acquisition costs to the product. Rather than relying solely on sales calls, the product drives onboarding, activation, and expansion revenue.

---

## 1. PLG vs. Sales-Led GTM

| Dimension | Sales-Led Growth | Product-Led Growth |
| :--- | :--- | :--- |
| **User Entry** | Books demo with sales rep | Signs up for free trial instantly |
| **Value Realization** | Learns value from slide deck | Experiences "Aha!" moment in product |
| **Sales Trigger** | Inbound form download | Product activation signals (PQLs) |
| **Expansion** | Annual contract negotiations | Self-service stripe upgrades |

---

## 2. Product-Qualified Leads (PQLs)

A Product-Qualified Lead is a user who has signed up, used the product, reached a specific threshold of core actions, and is highly likely to convert to a paid subscription.

*   **Aha! Moment**: The moment a user experiences your product's value (e.g., Slack: Team sends 2,000 messages; Dropbox: User uploads 1 file on 2 separate devices).

### PQL Evaluation Schema

```
[User Signup] ──> [Event Telemetry: segment.track()] ──> [Internal Database]
                                                             │
                                                 Query threshold: sends > 10 calls
                                                             │
                                                             ▼
                                                [Flag PQL & Sync to HubSpot]
```

---

## 3. Product Event Telemetry Schema (CDP Tracking)

Using standard event schemas (Segment/Amplitude format) to capture product telemetry:

```javascript
// Example segment event triggered in React app
analytics.track("Document Created", {
  userId: "user_9812",
  companyId: "comp_2112",
  planType: "Free Trial",
  documentType: "Proposal",
  pages_count: 5
});
```

### Postgres Analytics Event Schema

```sql
CREATE TABLE product_events (
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(100) NOT NULL,
    company_id VARCHAR(100),
    event_name VARCHAR(100) NOT NULL,
    properties JSONB, -- store dynamic payload elements
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Trigger query to identify active PQL users
SELECT DISTINCT company_id
FROM product_events
WHERE event_name = 'Document Created'
GROUP BY company_id
HAVING COUNT(id) >= 5; -- Inferred PQL activation threshold
```
