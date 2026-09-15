# Study Notes - Day 043: Agent & Workflow Orchestration

Today's studies focused on workflow orchestration architectures, Directed Acyclic Graph (DAG) compilation, parallel thread pools, retry strategies (exponential backoffs), task timeouts, and Saga-pattern compensation rollbacks.

---

## 1. Orchestration vs. Choreography

When coordinating multiple GTM systems or agents, there are two primary coordination patterns:

### 1. Orchestration (Centralized Control)
*   **Mechanism**: A central controller (the Orchestrator) coordinates all task steps, checks statuses, handles errors, and decides which task runs next.
*   **Pros**: Explicit dependency graph, single source of truth for workflow state, easier to debug and enforce compliance.
*   **GTM Use Case**: Running a lead processing pipeline (Ingest $\rightarrow$ Enrich $\rightarrow$ Score $\rightarrow$ Email $\rightarrow$ CRM Sync).

### 2. Choreography (Decentralized Event-Driven)
*   **Mechanism**: Individual nodes react to events independently. There is no central controller.
*   **Pros**: Highly decoupled, highly scalable.
*   **Cons**: Hard to trace the end-to-end path of a single lead; changes to workflow require updating multiple services.
*   **GTM Use Case**: A customer lifecycle where a new subscription triggers Slack alerts, email onboarding, and metric updates simultaneously.

---

## 2. DAGs & Parallel vs. Sequential Execution

A **Directed Acyclic Graph (DAG)** is a topological representation of tasks where:
*   Nodes represent individual tasks (e.g. "Score Lead").
*   Directed edges represent dependencies (e.g. "Score Lead" $\rightarrow$ "AI Copywriting" means scoring must finish first).
*   No cycles exist (Task A cannot depend on Task B if Task B depends on Task A).

### Parallel Execution (Concurrency)
Tasks that do not depend on each other can run simultaneously:
*   In our simulator, once **Ingest Lead** completes, both **Enrich Firmographics** and **Score Lead** are triggered in parallel using thread pools (`ThreadPoolExecutor`).
*   This cuts overall pipeline latency significantly compared to running every task sequentially.

---

## 3. Handling Pipeline Failures: Sag Pattern & Compensation

Distributed systems face frequent failures (network lag, API down, database lock). GTM engines must maintain consistency:

### 1. Forward Recovery (Retries)
*   If a task fails (e.g., API rate limit), retry using **Exponential Backoff**:
    $$\text{Wait Time} = \text{Base Wait} \times (\text{Backoff Factor})^{\text{Attempt}}$$
*   *Jitter*: Adding a small random variation to wait times to prevent a herd of retrying workers from overloading the target API simultaneously.

### 2. Backward Recovery (Saga Pattern / Compensation)
*   If a critical step fails and exhausts all retries (e.g. AI engine timeout), the system must roll back all previously completed database states.
*   **Saga Pattern**: For every task that commits changes to an external system, define a matching **Compensation Function** that rolls it back:
    *   *Task*: `Ingest Lead` $\rightarrow$ *Compensation*: `Delete lead from database`.
    *   *Task*: `CRM Sync` $\rightarrow$ *Compensation*: `Delete lead object from Salesforce`.
*   Rollbacks are run in **reverse chronological order** of completion.
