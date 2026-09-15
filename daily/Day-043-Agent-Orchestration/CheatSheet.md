# Cheat Sheet - Agent Orchestration

This cheat sheet compiles orchestration terminology, thread management scripts, and rollback patterns for GTM systems.

---

## 1. Key Terminology

*   **Directed Acyclic Graph (DAG)**: A structural network representation of tasks and dependencies containing no circular loops.
*   **Saga Pattern**: A design pattern for managing distributed transactions by executing a series of local transactions, with compensation rollbacks triggered on failures.
*   **Exponential Backoff**: A retry strategy where the delay between attempts increases exponentially (e.g. 1s $\rightarrow$ 2s $\rightarrow$ 4s).
*   **Jitter**: Random noise added to retry delays to prevent concurrent connection spikes (herd effect).
*   **Concurreny vs Parallelism**: Concurrency is handling multiple tasks at once; Parallelism is executing multiple tasks simultaneously (using multiple CPU cores/threads).

---

## 2. Exponential Backoff Formula

$$\text{Delay}_n = \text{Base Delay} \times \text{Multiplier}^n \pm \text{Random Jitter}$$

*Example (Base=1.0, Multiplier=2.0)*:
*   Attempt 1: $1.0 \times 2^0 = 1.0\text{s}$
*   Attempt 2: $1.0 \times 2^1 = 2.0\text{s}$
*   Attempt 3: $1.0 \times 2^2 = 4.0\text{s}$

---

## 3. Parallel Execution Template (Python Threads)

Submit multiple independent tasks in parallel:
```python
from concurrent.futures import ThreadPoolExecutor, as_completed

tasks_to_run = [
    {"name": "Enrichment", "func": run_enrich},
    {"name": "Lead Scoring", "func": run_scoring}
]

context = {"lead_email": "bruce@waynecorp.com"}

with ThreadPoolExecutor(max_workers=2) as executor:
    # Submit tasks in parallel
    futures = {
        executor.submit(t["func"], context): t["name"] 
        for t in tasks_to_run
    }
    
    # Process outputs as they finish
    for future in as_completed(futures):
        task_name = futures[future]
        result = future.result()
        print(f"Task {task_name} finished with output: {result}")
```

---

## 4. Saga Compensation Runner Template

If a workflow fails, run rollback functions in reverse execution order:
```python
completed_tasks = ["Ingest Lead", "Enrichment", "CRM Sync"]
compensate_map = {
    "Ingest Lead": rollback_ingestion,
    "CRM Sync": rollback_crm_sync
}

# Reverse order rollback
for name in reversed(completed_tasks):
    rollback_func = compensate_map.get(name)
    if rollback_func:
        print(f"Rolling back: {name}")
        rollback_func(context)
```
