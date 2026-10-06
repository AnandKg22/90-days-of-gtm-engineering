# Agent Specification: Knowledge Agent

Integrates with pgvector RAG databases to retrieve internal product and compliance context.

---

## ⚙️ Specifications

- **Default Tools**: `['query_vector_db', 'get_citation_references']`
- **Input parameters**: `query (str)`
- **Output type**: `RAGContextAnswer (Pydantic model)`

---

## 🛠️ Architecture

```
[Trigger / Input] ──> [Reasoning Loop] ──> [Tool Invocation] ──> [Pydantic Validation] ──> [Result Output]
```

---

## 📂 File Layout
- `agent.py` — Core logic class and execution pipeline.
- `README.md` — Architectural specifications.
