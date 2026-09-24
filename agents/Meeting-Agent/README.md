# Agent Specification: Meeting Agent

Compiles customer profiles, open deal sizes, and technographics into AE briefs before sales calls.

---

## ⚙️ Specifications

- **Default Tools**: `['get_deal_history', 'get_meeting_notes', 'generate_brief']`
- **Input parameters**: `lead_id (str)`
- **Output type**: `MeetingPrepBrief (Pydantic model)`

---

## 🛠️ Architecture

```
[Trigger / Input] ──> [Reasoning Loop] ──> [Tool Invocation] ──> [Pydantic Validation] ──> [Result Output]
```

---

## 📂 File Layout
- `agent.py` — Core logic class and execution pipeline.
- `README.md` — Architectural specifications.
