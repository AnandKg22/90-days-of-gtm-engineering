# GTM Architecture - Day 014: MongoDB Document Storage & Clickstreams

This document details the database architecture of our NoSQL GTM events database, illustrating clickstream ingest pipelines and document indexing plans.

---

## 🔄 NoSQL Clickstream Ingest Flow

The diagram below details the real-time event pipeline, showing how unstructured telemetry is captured and stored:

```mermaid
graph TD
    Client[Next.js Client Site] -->|1. user_activities: page views, clicks| Segment[Segment CDP Gateway]
    Segment -->|2. HTTP POST JSON Event Bundle| Receiver[Webhook API Receiver]
    
    subgraph MongoDB Event Store
        Receiver -->|3. Raw Ingest| LeadsCollection[(Leads Collection)]
        LeadsCollection -->|4. Index array elements| MultikeyIndex[(Multikey Index: touchpoints.url)]
    end
    
    subgraph Event Analytics
        Query[Nested Array Queries] -->|5. Fast lookup| MultikeyIndex
        MultikeyIndex -->|6. Render Traffic Reports| Dashboard[Analytics Dashboard]
    end
```

---

## ⚙️ Document Indexing Specifications

To search nesting arrays quickly as database records scale, we configure two NoSQL index models:

### 1. Compound Index (Multi-field search)
Optimizes queries filtering by both country and company size:
```javascript
db.leads.createIndex({ "country": 1, "employee_count": -1 });
```

### 2. Multikey Index (Nested Array search)
Optimizes search filters auditing user touchpoint URLs. Creating this index maps each object inside the `touchpoints` array individually:
```javascript
db.leads.createIndex({ "touchpoints.url": 1 });
```
This converts linear scans searching the nested array into B-Tree index scans, executing lookups in milliseconds.
