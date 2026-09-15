# Day 043: GTM Workflow Orchestrator Prototype
import sys
import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Dict, Any, Tuple, Callable

# Ensure UTF-8 output formatting for terminal compatibility
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

class Task:
    def __init__(
        self,
        name: str,
        func: Callable[[Dict[str, Any]], Dict[str, Any]],
        dependencies: List[str] = None,
        timeout: float = 2.0,
        max_retries: int = 2,
        backoff_factor: float = 1.5,
        compensate_func: Callable[[Dict[str, Any]], None] = None
    ):
        self.name = name
        self.func = func
        self.dependencies = dependencies or []
        self.timeout = timeout
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor
        self.compensate_func = compensate_func
        self.status = "PENDING"  # PENDING, RUNNING, COMPLETED, FAILED
        self.error = None

class WorkflowOrchestrator:
    def __init__(self):
        self.tasks: Dict[str, Task] = {}
        self.context: Dict[str, Any] = {}

    def add_task(self, task: Task):
        self.tasks[task.name] = task

    def execute_workflow(self, initial_context: Dict[str, Any]) -> Tuple[str, Dict[str, Any]]:
        self.context = initial_context.copy()
        completed_tasks = set()
        failed_tasks = set()
        running_tasks = set()

        print("=" * 72)
        print("                 GTM WORKFLOW ORCHESTRATION START")
        print("=" * 72)
        print("DAG TASK DEPENDENCY LIST:")
        for name, task in self.tasks.items():
            deps = ", ".join(task.dependencies) if task.dependencies else "None"
            print(f"  - Task '{name:<18}' | Dependencies: [{deps}]")
        print("-" * 72)

        # Main orchestration loop
        with ThreadPoolExecutor(max_workers=4) as executor:
            while len(completed_tasks) + len(failed_tasks) < len(self.tasks):
                # 1. Identify tasks that are ready to run (dependencies satisfied)
                ready_tasks = []
                for name, task in self.tasks.items():
                    if task.status == "PENDING":
                        # Check if all dependencies are in completed_tasks
                        if all(dep in completed_tasks for dep in task.dependencies):
                            # If a dependency failed, we cannot run this task
                            if any(dep in failed_tasks for dep in task.dependencies):
                                print(f"[-] Task '{name}' BLOCKED because a dependency failed. Marking FAILED.")
                                task.status = "FAILED"
                                task.error = "Dependency Blocked"
                                failed_tasks.add(name)
                            else:
                                ready_tasks.append(task)

                # 2. Submit ready tasks to thread executor (Parallel execution)
                futures_map = {}
                for task in ready_tasks:
                    task.status = "RUNNING"
                    running_tasks.add(task.name)
                    print(f"[*] Task '{task.name}' STARTED (Running in thread)...")
                    # Submit task execution with retry logic
                    future = executor.submit(self._execute_with_retries, task)
                    futures_map[future] = task.name

                # 3. Wait for completed threads
                if futures_map:
                    for future in as_completed(futures_map):
                        task_name = futures_map[future]
                        running_tasks.remove(task_name)
                        try:
                            success, result_data = future.result()
                            task = self.tasks[task_name]
                            if success:
                                task.status = "COMPLETED"
                                completed_tasks.add(task_name)
                                self.context.update(result_data)
                                print(f"[+] Task '{task_name}' COMPLETED. Context updated.")
                            else:
                                task.status = "FAILED"
                                task.error = result_data.get("error", "Unknown error")
                                failed_tasks.add(task_name)
                                print(f"[!] Task '{task_name}' FAILED: {task.error}")
                        except Exception as e:
                            print(f"[!] Thread execution crashed for '{task_name}': {str(e)}")
                else:
                    # Avoid tight loop if we are waiting for active threads
                    if running_tasks:
                        time.sleep(0.1)
                    else:
                        break

        # 4. Check workflow status & Execute compensation logic on failure (Saga Pattern)
        if failed_tasks:
            print("\n[🚨 WORKFLOW FAILURE DETECTED] Triggering Compensation Rollbacks...")
            self._rollback(completed_tasks)
            return "FAILED", self.context
        else:
            print("\n[🎉 WORKFLOW SUCCESS] All tasks in dependency graph executed successfully.")
            return "SUCCESS", self.context

    def _execute_with_retries(self, task: Task) -> Tuple[bool, Dict[str, Any]]:
        """Handles execution, timeouts, and exponential backoff retry loops."""
        retries = 0
        wait_time = 0.5
        
        while retries <= task.max_retries:
            try:
                # Execute task within a timeout
                start_time = time.time()
                # Run function in the worker thread
                output = task.func(self.context)
                
                # Check for simulated timeout
                duration = time.time() - start_time
                if duration > task.timeout:
                    raise TimeoutError(f"Task execution exceeded timeout limit of {task.timeout}s.")
                
                return True, output
                
            except Exception as e:
                retries += 1
                err_msg = str(e)
                print(f"  [!] Task '{task.name}' attempt {retries} failed: {err_msg}")
                
                if retries <= task.max_retries:
                    print(f"  [~] Backing off. Waiting {wait_time}s before next retry...")
                    time.sleep(wait_time)
                    wait_time *= task.backoff_factor
                else:
                    return False, {"error": err_msg}

    def _rollback(self, completed_tasks: set):
        """Runs compensation tasks in reverse order to roll back changes."""
        # Reverse completed list to rollback most recent actions first
        ordered_rollback = [name for name in self.tasks.keys() if name in completed_tasks]
        ordered_rollback.reverse()
        
        for name in ordered_rollback:
            task = self.tasks[name]
            if task.compensate_func:
                print(f"[*] Running Compensation for '{name}'...")
                try:
                    task.compensate_func(self.context)
                    print(f"  [+] Rollback logic for '{name}' completed successfully.")
                except Exception as e:
                    print(f"  [ERROR] Compensation for '{name}' failed: {str(e)}")
            else:
                print(f"  [-] Task '{name}' has no compensation logic registered. Skipping.")


# --- MOCK GTM WORKFLOW FUNCTIONS ---

def ingest_lead_func(context: Dict[str, Any]) -> Dict[str, Any]:
    print("  -> [Ingesting] Processing lead info...")
    time.sleep(0.1)
    return {"lead_id": 401, "status": "Ingested"}

def enrich_firmographics_func(context: Dict[str, Any]) -> Dict[str, Any]:
    print("  -> [Enriching] Querying Clearbit API...")
    time.sleep(0.2)
    # Simulate network instability: 30% chance to fail first time
    if context.get("simulate_network_failure") and random.random() < 0.5:
        raise ConnectionError("Clearbit API connection refused (Simulated failure).")
    return {"tech_stack": "React, Salesforce", "employees": 450, "industry": "SaaS"}

def score_lead_func(context: Dict[str, Any]) -> Dict[str, Any]:
    print("  -> [Scoring] Evaluating fit score...")
    time.sleep(0.1)
    return {"fit_score": 85}

def ai_copywriting_func(context: Dict[str, Any]) -> Dict[str, Any]:
    print("  -> [AI Writing] Draft outreach email...")
    # Simulate timeout
    if context.get("simulate_ai_timeout"):
        time.sleep(1.2) # Exceeds 1.0s timeout
    else:
        time.sleep(0.2)
    return {"email_draft": "Subject: Level up sales at WayneCorp..."}

def crm_sync_func(context: Dict[str, Any]) -> Dict[str, Any]:
    print("  -> [CRM Syncing] Pushing to Salesforce...")
    time.sleep(0.2)
    if context.get("simulate_crm_crash"):
        raise RuntimeError("Salesforce database validation error (Simulated crash).")
    return {"salesforce_id": "sf_lead_99212"}


# --- COMPENSATION FUNCTIONS (ROLLBACK) ---

def rollback_ingest(context: Dict[str, Any]):
    print(f"  -> [ROLLBACK] Deleting Lead ID {context.get('lead_id')} from local database staging tables.")

def rollback_crm_sync(context: Dict[str, Any]):
    print(f"  -> [ROLLBACK] Deleting lead record {context.get('salesforce_id')} from Salesforce CRM database.")


if __name__ == "__main__":
    # Configure Workflow Tasks
    task_ingest = Task("Ingest Lead", ingest_lead_func, compensate_func=rollback_ingest)
    
    # Enrich depends on Ingest
    task_enrich = Task("Enrich Firmographics", enrich_firmographics_func, dependencies=["Ingest Lead"], max_retries=2)
    
    # Score depends on Ingest
    task_score = Task("Score Lead", score_lead_func, dependencies=["Ingest Lead"])
    
    # AI Copywriting depends on Enrich and Score (requires both tech stack and score)
    task_ai = Task("AI Copywriting", ai_copywriting_func, dependencies=["Enrich Firmographics", "Score Lead"], timeout=1.0)
    
    # CRM Sync depends on AI Copywriting
    task_crm = Task("CRM Sync", crm_sync_func, dependencies=["AI Copywriting"], compensate_func=rollback_crm_sync)

    # SCENARIO 1: SUCCESSFUL EXECUTION WITH NETWORK RETRY
    print("\n\n" + "#" * 72)
    print("### RUN SCENARIO 1: SUCCESSFUL WORKFLOW WITH MOCK NETWORK RETRIES")
    print("#" * 72)
    
    orchestrator1 = WorkflowOrchestrator()
    orchestrator1.add_task(task_ingest)
    orchestrator1.add_task(task_enrich)
    orchestrator1.add_task(task_score)
    orchestrator1.add_task(task_ai)
    orchestrator1.add_task(task_crm)
    
    # Enable network failure simulation to test retries
    status1, ctx1 = orchestrator1.execute_workflow({
        "company": "Wayne Enterprises", 
        "email": "bruce@waynecorp.com",
        "simulate_network_failure": True
    })
    print(f"\nFinal Workflow Result: {status1}")

    # SCENARIO 2: FAILURE EXECUTION WITH TIMEOUT & ROLLBACK (SAGA PATTERN)
    print("\n\n" + "#" * 72)
    print("### RUN SCENARIO 2: PIPELINE CRASH (TIMEOUT) & SAGA ROLLBACK")
    print("#" * 72)
    
    # Reset tasks status
    task_ingest.status = "PENDING"
    task_enrich.status = "PENDING"
    task_score.status = "PENDING"
    task_ai.status = "PENDING"
    task_crm.status = "PENDING"
    
    orchestrator2 = WorkflowOrchestrator()
    orchestrator2.add_task(task_ingest)
    orchestrator2.add_task(task_enrich)
    orchestrator2.add_task(task_score)
    orchestrator2.add_task(task_ai)
    orchestrator2.add_task(task_crm)
    
    # Trigger AI Copywriting timeout
    status2, ctx2 = orchestrator2.execute_workflow({
        "company": "Cyberdyne Systems", 
        "email": "sconnor@cyberdyne.co",
        "simulate_ai_timeout": True
    })
    print(f"\nFinal Workflow Result: {status2}")
