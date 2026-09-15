# Project Assignment - Day 043: Workflow Orchestrator

This project requires developing a Python GTM Workflow Orchestrator. It acts as the central execution engine coordinating multi-node campaigns based on task dependencies.

---

## 🎯 Requirements

Your Orchestrator must:
1.  **Define DAG Dependency Resolution**:
    *   Accept task nodes with named dependencies.
    *   Map out ready tasks on every loop iteration.
2.  **Concurrency / Parallel Processing**:
    *   Execute independent sibling nodes concurrently in parallel threads (e.g. running firmographics scraper and lead scorer simultaneously).
3.  **Task Timeout Thresholds**:
    *   Support custom timeout limits (seconds) per node. If a task exceeds this limit (e.g., a lagging LLM call), abort the thread and mark it failed.
4.  **Exponential Backoff Retries**:
    *   Attempt retries on transient connection errors, implementing exponential delays between attempts (e.g., wait 0.5s, then 0.75s, etc.).
5.  **Saga Pattern Rollback Engine**:
    *   If a node exhausts all retries and fails, block all downstream tasks.
    *   Iterate backward through all completed tasks and execute registered compensation functions to undo committed database/API states.

---

## 💻 Deliverable Code

A complete, working workflow orchestrator prototype script has been created and is available in [Code/workflow_orchestrator.py](Code/workflow_orchestrator.py). It runs both success scenarios (with retries) and failure scenarios (triggering Sagas rollbacks).