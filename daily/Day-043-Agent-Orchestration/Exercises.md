# Exercises - Day 043: Workflow Modeling & Sagas

This document details practical exercises on building Directed Acyclic Graphs (DAGs) and implementing Saga rollback logic.

---

## 📋 Exercise 1: Outbound Outreach DAG Graph

### Scenario:
You are designing an automated GTM campaign pipeline. A new contact is added, which triggers research, scoring, Slack alerts, email copywriting, email dispatch, and database sync.

### Dependency Graph Specification:
```
                [ Ingest Lead (A) ]
                        │
         ┌──────────────┴──────────────┐
         ▼                             ▼
  [ Tech Scrape (B) ]           [ Segment Score (C) ]
         │                             │
         └──────────────┬──────────────┘
                        ▼
            [ AI Email Writer (D) ]
                        │
         ┌──────────────┴──────────────┐
         ▼                             ▼
 [ Email Send (E) ]            [ CRM Push (F) ]
```

*   **Task A (Ingest)**: Depends on nothing.
*   **Task B (Scrape)**: Depends on A.
*   **Task C (Score)**: Depends on A.
*   **Task D (AI)**: Depends on B and C (needs tech stack and score to write custom email).
*   **Task E (Send)**: Depends on D (needs the email draft).
*   **Task F (CRM Sync)**: Depends on D.

---

## ⚙️ Exercise 2: Saga Rollback Transactions

When executing the above DAG, Task E (Email Send) fails due to SMTP gateway timeouts.
Determine:
1.  Which tasks need to trigger compensation rollbacks?
2.  In what order should they execute?

### Solution:
*   Only tasks that committed state changes *before* the failure need rollbacks. These are: **Task A (Ingest Lead)** and **Task F (CRM Push)** (assuming CRM Sync succeeded before Email Send crashed).
*   The rollbacks must execute in **reverse order of completion**:
    1.  `Compensate Task F`: Delete lead object from Salesforce CRM to avoid ghost profiles.
    2.  `Compensate Task A`: Soft-delete/flag the lead status as `Failed` in local tables.
*   Tasks B, C, and D are read-only calculations and do not need compensation.