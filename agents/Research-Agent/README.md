# Agent Specification: Research Agent

Scrapes website text, checks technographics, and crawls search engines for corporate enrichment.

---

## ⚙️ Specifications

- **Default Tools**: `['scrape_url', 'web_search', 'get_technographics']`
- **Input parameters**: `domain (str)`
- **Output type**: `CompanyEnrichmentResult (Pydantic model)`

---

## 🛠️ Architecture

```
[Trigger / Input] ──> [Reasoning Loop] ──> [Tool Invocation] ──> [Pydantic Validation] ──> [Result Output]
```

---

## 📂 File Layout
- `agent.py` — Core logic class and execution pipeline.
- `README.md` — Architectural specifications.
