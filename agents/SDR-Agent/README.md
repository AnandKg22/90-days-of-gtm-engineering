# Agent Specification: SDR Agent

Runs lead scoring metrics and drafts personalized AIDA email copy for prospects.

---

## ⚙️ Specifications

- **Default Tools**: `['score_lead', 'fetch_prospect_bio', 'write_outreach']`
- **Input parameters**: `contact_id (str), company_id (str)`
- **Output type**: `OutreachCampaign (Pydantic model)`

---

## 🛠️ Architecture

```
[Trigger / Input] ──> [Reasoning Loop] ──> [Tool Invocation] ──> [Pydantic Validation] ──> [Result Output]
```

---

## 📂 File Layout
- `agent.py` — Core logic class and execution pipeline.
- `README.md` — Architectural specifications.
