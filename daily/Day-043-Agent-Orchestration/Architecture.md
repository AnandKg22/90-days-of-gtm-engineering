# GTM Architecture - Day 043: Workflow Orchestrator

This document details the scheduling engine, concurrency models, and rollback logic supporting GTM workflow orchestration.

---

## 🔄 Concurrency & DAG Execution Pipeline

The diagram below details the pipeline, showing how independent tasks are executed in parallel while dependent nodes wait for completion:

```mermaid
graph TD
    Start[Trigger: Ingest Lead] -->|1. Run Ingestion| A[Task 1: Ingest Lead]
    A -->|2. Ingest Done| Scheduler{DAG Scheduler}
    
    subgraph Parallel Worker Threads
        Scheduler -->|3. Start Thread| B[Task 2: Enrich Firmographics]
        Scheduler -->|3. Start Thread| C[Task 3: Score Lead]
    end
    
    B -->|4. Complete| WaitGate{Wait for Both}
    C -->|4. Complete| WaitGate
    
    WaitGate -->|5. Both Done| D[Task 4: AI Copywriting]
    D -->|6. Copy Done| E[Task 5: CRM Sync]
    E -->|7. Sync Done| Finish[Workflow Success]
```

---

## 🔄 Saga Rollback Pipeline (Backward Recovery)

The diagram below outlines the sequence triggered when a task fails (e.g. AI Copywriting exceeds its 1.0s timeout limit) and exhausts all retries:

```mermaid
graph TD
    AI[Task 4: AI Copywriting] -->|Attempt 3 Timeout| Fail[MARK FAILED]
    Fail -->|1. Abort Downstream| Block[Mark CRM Sync BLOCKED]
    Block -->|2. Trigger rollback| Saga[Saga Rollback Engine]
    
    subgraph Reverse Chronological Compensation
        Saga -->|3. Compensate Task 3| Skip1[Skip Score Lead: Read-Only]
        Skip1 -->|4. Compensate Task 2| Skip2[Skip Enrich: Read-Only]
        Skip2 -->|5. Compensate Task 1| Rollback1[Compensate Ingest Lead: Delete local DB staging]
    end
    
    Rollback1 -->|6. Complete| Complete[System Reset: Fail Logged]
```

---

## ⚙️ Orchestration Core Components

1.  **DAG Scheduler**: Analyzes task metadata and dependencies to build a topological execution order. Identifies sibling nodes that can run concurrently.
2.  **Worker Thread Pool**: Utilizes Python's `ThreadPoolExecutor` to manage asynchronous worker threads, running task functions concurrently.
3.  **Context Registry**: A shared data dictionary (`self.context`) that aggregates task outputs. Downstream tasks read variables (e.g., `tech_stack` or `fit_score`) produced by upstream tasks.
4.  **Saga Rollback Engine**: An error interceptor that pauses threads upon execution failures, cancels downstream scheduling, and traverses completed tasks backward to call compensation handlers.
