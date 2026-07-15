# GTM Architecture - Day 003: Journey Tracking State Engine

This document details the telemetry tracking architecture that powers the lifecycle state transitions of the Journey Mapping Board.

---

## 🔄 Client-Side Telemetry Flow

The diagram below shows how raw clicks and signups are captured, validated, and used to update the contact's pipeline stage:

```mermaid
graph TD
    Client[Next.js Client Application] -->|1. user_activity: clicks/views| Segment[Segment CDP Gateway]
    Segment -->|2. Webhook Event Bundle| Router[n8n Event Router]
    
    subgraph Data Warehousing
        Router -->|3. Log Event| DB[(PostgreSQL Events DB)]
    end
    
    subgraph Lifecycle State Machine
        DB -->|4. Read Event Log| Tracker[Journey Tracker Engine]
        Tracker -->|5. Compute Stage Change| CRM[HubSpot Contacts API]
        Tracker -->|6. Trigger Slack Alert if High Intent| Slack[Slack Intent Alerts]
    end
```

---

## 📂 Webhook Event Payloads

### 1. Page View Event (Visitor State)
Captured when a user lands on key pages:
```json
{
  "user_id": "usr_9921",
  "event_name": "page_view",
  "properties": {
    "url": "/pricing",
    "referrer": "google.com"
  }
}
```

### 2. Form Signup Event (Lead State)
Fired when the user signs up for a trial account:
```json
{
  "user_id": "usr_9921",
  "event_name": "form_signup",
  "properties": {
    "email": "alex.dev@acmecorp.com",
    "company": "Acme Corp"
  }
}
```
