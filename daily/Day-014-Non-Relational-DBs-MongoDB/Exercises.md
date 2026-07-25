# Exercises - Day 014: MongoDB Document Schema Design

This document details the MongoDB collection structures and aggregation pipelines designed for our NoSQL GTM event database.

---

## 📂 MongoDB `leads` Document Schema (JSON)

Below is the document blueprint designed to store dynamic lead properties and nested activity timelines:

```json
{
  "_id": {"$oid": "64b0f9c2d1b849208a77a911"},
  "email": "dean@imsgoa.org",
  "company_name": "IMSGOA Maritime College",
  "employee_count": 85,
  "country": "IN",
  "touchpoints": [
    {
      "timestamp": {"$date": "2026-07-01T10:00:00Z"},
      "source": "google",
      "medium": "cpc",
      "url": "/features"
    },
    {
      "timestamp": {"$date": "2026-07-05T14:30:00Z"},
      "source": "newsletter",
      "medium": "email",
      "url": "/pricing"
    }
  ],
  "integrations_metadata": {
    "stripe_customer_id": "cus_stripe_8820",
    "stripe_status": "Active",
    "apollo_enriched_at": {"$date": "2026-07-02T08:00:00Z"},
    "custom_fields": {
      "proctoring_approved": true,
      "sponsors": ["SYNERGY", "FLEET"]
    }
  }
}
```

---

## 🔍 MongoDB Document Query Examples

### 1. Find leads who viewed the `/pricing` page
Filters documents by matching values inside the nested `touchpoints` array:
```javascript
db.leads.find(
  { "touchpoints.url": "/pricing" },
  { "email": 1, "company_name": 1, "_id": 0 }
);
```

### 2. Aggregation Pipeline: Count total leads grouped by Traffic Source
Unwinds the nested `touchpoints` array to count and sort traffic channels:
```javascript
db.leads.aggregate([
  // Step 1: Deconstruct the touchpoints array
  { $unwind: "$touchpoints" },
  // Step 2: Group by source and count
  {
    $group: {
      _id: "$touchpoints.source",
      total_leads: { $sum: 1 }
    }
  },
  // Step 3: Sort by count descending
  { $sort: { total_leads: -1 } }
]);
```
