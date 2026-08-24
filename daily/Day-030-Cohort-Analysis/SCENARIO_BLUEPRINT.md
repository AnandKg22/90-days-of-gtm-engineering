# 📐 Day 030 Scenario Blueprint: Cohort Analysis
## 7-Stage Technical Architecture & Reference Implementation

> **Author**: Anand Kumar | [akstack.com](https://akstack.com) | [GitHub](https://github.com/AnandKg22) | [LinkedIn](https://www.linkedin.com/in/anandkg22/)  
> **Curriculum Phase**: Phase 2: APIs, Workflow Automation & Ingestion Pipelines  
> **Core Outcome**: Practically Skilled (Able to design cohort retention reporting pipelines, write SQL pivot queries, calculate DAU/WAU/MAU stickiness metrics, and optimize high-volume activity log databases)  
> **Architecture Pattern**: Event-Driven Revenue Engineering / Resilient GTM Pipeline  

---

## 🎯 1. Enterprise Case Scenario & Problem Definition

### 1.1 Enterprise Context
* **Company Profile**: Series-B B2B SaaS ($15M–$30M ARR, 50-person commercial org, ACV $25k–$50k).
* **Operational Challenge**: If commercial operations experience manual friction, unvalidated data syncs, or slow response times in **Cohort Analysis**, then high-intent customer velocity drops significantly across the revenue funnel.

### 1.2 Domain Overview
A B2B SaaS startup can acquire thousands of new users weekly, but if those users do not return to use the product, the business will fail due to churn. In revenue operations, **Cohort Analysis** is the primary method used to measure user retention and product-market fit.

Rather than looking at generic user growth (which hides product issues), cohort analysis groups acquired users into buckets based on a shared time window (e.g. signup week) and tracks their engagement over subsequent intervals. GTM dashboard widgets audit user engagement using metrics like **Daily Active Users (DAU)**, **Weekly Active Users (WAU)**, and **Monthly Active Users (MAU)**. They also track the **User Stickiness Ratio** ($DAU/MAU$), aiming for a $>20\%$ benchmark. To compile these cohort grids from high-volume database tables, you write multi-step SQL Common Table Expressions (CTEs) that calculate elapsed date deltas and pivot the output into retention grids.

---

### 1.3 Quantifiable Engineering Objectives
* [x] **Latency**: Reduce end-to-end processing latency for **Cohort Analysis** to `< 1,200 ms`.
* [x] **Reliability**: Ensure 100% data consistency across CRM, Database, and Event queues.
* [x] **Cost Optimization**: Maintain operational compute & token unit economics at `< $0.035 / transaction`.

---

## 🔍 2. Technical Feasibility, Concepts & Protocol Research

### 2.1 Key Architectural Concepts
*   **Cohort**: A group of users who share a common characteristic or event within a specific time window (most commonly, the date of signup).
*   **Cohort Analysis**: The study of behavioral changes in cohorts over time, focusing on user retention and churn trends.
*   **Daily Active Users (DAU)**: The number of unique users who perform an action in a GTM application within a 24-hour window.
*   **Monthly Active Users (MAU)**: The number of unique users active within a rolling 30-day window.
*   **User Stickiness Ratio**: The percentage of monthly active users who engage on a daily basis, calculated as:
    $$\text{Stickiness} = \left( \frac{\text{DAU}}{\text{MAU}} \right) \times 100$$
*   **Acquisition Cohort**: Grouping users based on the date of their first transaction or signup.
*   **Behavioral Cohort**: Grouping users based on specific actions they perform (e.g., users who complete at least 3 exams in their first week).
*   **Retention Grid**: A matrix displaying the proportion of acquired cohort users who return to the product in subsequent weeks or months.

---

---

## 📐 3. System Architecture & Schemas

### 3.1 Architectural Flow Diagram
```mermaid
graph TD
    Logs[(Raw Activity Logs Table)] -->|1. SELECT user_id, MIN(event_date)| Cohort_Start[Cohort Acquisition Date view]
    
    Cohort_Start -->|2. Join with raw logs| Join[Joined Log Table]
    
    Join -->|3. Calculate day difference| Days[Elapsed Day Delta]
    
    Days -->|4. Divide by 7| Weeks[Weekly Interval Buckets: W0, W1, W2, W3]
    
    Weeks -->|5. Pivot & COUNT(DISTINCT user_id)| Grid[Cohort Weekly Retention Grid]
```

### 3.2 Technical Reference & Specifications
Detailed schema mappings and configuration constraints for Cohort Analysis.

---

## 💻 4. Reference Implementation & Sandbox Code

```python
class CohortAnalyzer:
    def __init__(self, logs: List[dict]):
        self.logs = logs
        
    def analyze_retention(self) -> dict:
        # 1. Identify first activity (signup) date for each user
        user_signups = {}
        for log in self.logs:
            uid = log["user_id"]
            date_val = datetime.strptime(log["event_date"], "%Y-%m-%d")
            if uid not in user_signups or date_val < user_signups[uid]:
                user_signups[uid] = date_val
                
        # 2. Group cohorts by signup week
        cohorts = {"2026-07-01": [], "2026-07-08": []}
        for uid, signup_date in user_signups.items():
            if signup_date.strftime("%Y-%m-%d") <= "2026-07-07":
                cohorts["2026-07-01"].append(uid)
            else:
                cohorts["2026-07-08"].append(uid)
                
        # 3. Calculate weekly activity deltas
        retention_grid = {
            "2026-07-01": {0: set(), 1: set(), 2: set(), 3: set()},
            "2026-07-08": {0: set(), 1: set(), 2: set(), 3: set()}
        }
        for log in self.logs:
            uid = log["user_id"]
            event_date = datetime.strptime(log["event_date"], "%Y-%m-%d")
            signup_date = user_signups[uid]
            
            delta_days = (event_date - signup_date).days
            week_idx = delta_days // 7
            
            for cohort_start, uids in cohorts.items():
                if uid in uids and week_idx in retention_grid[cohort_start]:
                    retention_grid[cohort_start][week_idx].add(uid)
                    break
                    
        return {c: {"size": len(cohorts[c]), "retention": {w: len(uids) for w, uids in weeks.items()}} 
                for c, weeks in retention_grid.items()}
```

---

## ⚡ 5. Automation Blueprint & Event Wiring

* **Ingestion Trigger**: Public webhook listener with cryptographic signature verification.
* **Routing Logic**: Idempotent processing gate backed by Redis cache.
* **Downstream Sinks**: Real-time upsert to PostgreSQL / Supabase, bi-directional CRM synchronization, and automated notification bus.

---

## 📊 6. Telemetry, KPI & Unit Economics

$$\text{Unit Economics} = \text{Compute} + \text{External API Calls} + \text{Storage} \approx \mathbf{\$0.0025\ /\ event}$$

* **P95 Latency SLA**: `< 1,200 ms`
* **Error Rate Target**: `< 0.05%`
* **Commercial ROI**: Eliminates an estimated 15–20 hours of manual operational drag per week.

---

## 🛡️ 7. Edge Cases, Guardrails & Resilience Strategy

1. **API Rate Limiting (429)**: Exponential backoff with random jitter ($2^n \times 100\text{ms}$) and Dead-Letter Queue (DLQ) buffering.
2. **Payload Integrity & Schema Drift**: Strict Pydantic type validation with automatic rejection of malformed inputs.
3. **Downstream Outages**: Asynchronous retry worker ensuring zero dropped transactions during system maintenance.
