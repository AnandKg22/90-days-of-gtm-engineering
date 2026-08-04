# GTM Architecture - Day 018: Customer Data Platform (Segment)

This document details the CDP architecture, demonstrating identity resolution mappings and multiplexing endpoints.

---

## 🔄 Segment Event Routing & Identity Resolution

The diagram below details the path of telemetry events from browser actions, through identity graphs, to multiple integrations:

```mermaid
graph TD
    Client[Next.js Website Client] -->|1. HTTP POST: Track/Identify calls| Segment[Segment CDP Ingestion]
    
    subgraph Identity Resolution Graph
        Segment -->|2. Check cookies| ID_Graph[(Identity DB: anonymous_id <==> user_id)]
    end
    
    subgraph Tracking Plan Validation
        Segment -->|3. Check schema validation| Check{Is Valid JSON?}
        Check -->|No: Log Error| Discard[Rejected Events Queue]
        Check -->|Yes: Multiplex payload| Router[Destinations Router]
    end
    
    subgraph Downstream Destinations
        Router -->|4a. Track Events| GA4[Google Analytics 4]
        Router -->|4b. Upsert Contacts & Companies| HubSpot[HubSpot CRM]
        Router -->|4c. Write Events History| Postgres[(PostgreSQL Warehouse)]
    end
```

---

## ⚙️ Segment API Payload Specifications

### 1. Identify Call (Identity Mapping)
Establishes the link between sessions and traits:
```json
{
  "userId": "usr_9901",
  "anonymousId": "anon_session_881023",
  "type": "identify",
  "traits": {
    "email": "captain@imsgoa.org",
    "name": "Vikram Singh"
  }
}
```

### 2. Group Call (Account Mapping)
Links the identified user to their B2B Company ID:
```json
{
  "userId": "usr_9901",
  "groupId": "org_imsgoa",
  "type": "group",
  "traits": {
    "name": "IMSGOA Maritime College",
    "employees": 85
  }
}
```
