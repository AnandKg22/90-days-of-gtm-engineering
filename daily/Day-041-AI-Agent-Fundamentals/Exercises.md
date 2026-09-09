# Exercises - Day 041: Lead Research Agent Architecture

This document details practical exercises on designing AI agent architectures, defining tool interfaces, and planning reasoning loops.

---

## 📋 Exercise 1: Lead Research Agent Specification Design

### Scenario:
You are designing a **Lead Research Agent** to automate outbound market research. Draft the core specification blueprint.

### Specification Map:

1.  **Agent Persona & Role**:
    *   *Name*: GTM Recon Agent
    *   *Role*: Outbound Lead Enrichment & Intent Analyst.
    *   *System Instruction*: "You are an autonomous intelligence researcher. Gather company details, tech stacks, and buyer emails to formulate personalized pain-point pitches."
2.  **Tool Registry**:
    *   `search_web(query)`: Resolves general firmographic details.
    *   `fetch_pricing_page(domain)`: Scrapes target contract prices.
    *   `extract_contacts(domain)`: Scrapes decision-maker emails.
3.  **Short-term Memory Structure**:
    *   JSON array tracking current search history:
        ```json
        [
          {"step": 1, "thought": "Find tech stack", "action": "search_web", "observation": "Uses React, Next.js"}
        ]
        ```
4.  **Error Recovery & Fallback Rules**:
    *   If `extract_contacts` returns 0 contacts:
        *   *Thought*: "Direct scraping failed. I need to search LinkedIn structures."
        *   *Action*: Invoke `search_web` with parameter `[Company Name] LinkedIn Director of Sales`.

---

## ⚙️ Exercise 2: Human-in-the-Loop Integration Gate

### Goal:
Integrate a human approval step to prevent the agent from performing automated actions without verification.

### Design Task:
Insert a human approval gate before triggering the final synthesis. The agent should write its report to a file, trigger a Slack webhook asking for review, and wait.

```
[Agent research done] ──> [Write draft report] ──> [Send Slack approval link] ──> [WAIT] ──> [User clicks Approve] ──> [Dispatched to CRM]
```

### Flow Steps:
1.  **Generate Dossier**: Agent runs research loops.
2.  **Pause Loop**: Agent serializes its short-term memory state to a JSON file and pauses.
3.  **Human Audit**: A GTM manager opens the web console, edits the email draft, and clicks "Approve".
4.  **Resume**: The agent backend reads the approved text, completes the sync, and logs: `[HITL GATE APPROVED]`.