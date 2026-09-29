# Agent Specification: Proposal Agent

Generates scoped service agreements, pricing structures, and contract terms automatically.

---

## ⚙️ Specifications

- **Default Tools**: `['calculate_pricing', 'generate_sow_doc']`
- **Input parameters**: `opportunity_id (str), requirements (list)`
- **Output type**: `ProposalDocument (Pydantic model)`

---

## 🛠️ Architecture

```
[Trigger / Input] ──> [Reasoning Loop] ──> [Tool Invocation] ──> [Pydantic Validation] ──> [Result Output]
```

---

## 📂 File Layout
- `agent.py` — Core logic class and execution pipeline.
- `README.md` — Architectural specifications.
