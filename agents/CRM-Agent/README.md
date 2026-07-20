# Agent Specification: CRM Agent

Synchronizes entities and object properties between internal systems and HubSpot/Salesforce.

---

## ⚙️ Specifications

- **Default Tools**: `['sync_hubspot_record', 'query_salesforce_soql']`
- **Input parameters**: `object_type (str), crm_id (str), data (dict)`
- **Output type**: `CRMSyncStatus (Pydantic model)`

---

## 🛠️ Architecture

```
[Trigger / Input] ──> [Reasoning Loop] ──> [Tool Invocation] ──> [Pydantic Validation] ──> [Result Output]
```

---

## 📂 File Layout
- `agent.py` — Core logic class and execution pipeline.
- `README.md` — Architectural specifications.
