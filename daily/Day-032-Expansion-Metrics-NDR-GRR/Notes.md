# Study Notes - Day 032: Expansion Metrics (NDR & GRR)

Today's studies focused on Net Dollar Retention (NDR), Gross Dollar Retention (GRR), cohort revenue tracking database designs, SQL queries for cohort revenue metrics, and performance optimizations.

---

## 1. NDR vs. GRR in B2B SaaS

Once a customer is acquired, GTM teams focus on **expansion** (upsells, cross-sells) and **retention**. We track two key metrics to audit contract changes over a specific cohort window (typically 12 months):

### 1. Net Dollar Retention (NDR)
NDR measures how much your cohort revenue grew or shrank, **including** expansion, contraction, and churn.
*   **Formula**:
    $$\text{NDR (\%)} = \frac{\text{Starting MRR} + \text{Expansion MRR} - \text{Contraction MRR} - \text{Churned MRR}}{\text{Starting MRR}} \times 100$$
*   **Significance**: NDR > 100% means expansion from remaining customers outpaces churn. This is "Net Negative Churn," the holy grail of SaaS growth.

### 2. Gross Dollar Retention (GRR)
GRR measures the stability of cohort revenue, **excluding** expansion (capping growth at 100.0%). It shows the baseline health of your product.
*   **Formula**:
    $$\text{GRR (\%)} = \frac{\text{Starting MRR} - \text{Contraction MRR} - \text{Churned MRR}}{\text{Starting MRR}} \times 100$$
*   **Significance**: GRR cannot exceed 100.0%. A high GRR (>85%) indicates a stable customer base that rarely cancels.

---

## 2. Deep-Dive: Expansion Metrics Subtopics

To implement automated retention dashboards, a GTM Engineer must master these three subtopics:

### 1. Database Design (Cohort Revenue Tables)
*   **Definition**: Designing database tables that record customer contract snapshots at fixed intervals:
    *   **Customer Cohorts**: Grouping companies by their initial purchase date (`company_key`, `cohort_group_date`, `initial_mrr`).
    *   **Monthly Contract Snapshots**: Tracking monthly recurring revenue per customer (`company_key`, `snapshot_month`, `mrr_amount`).
*   **GTM Application**: Snapshot designs allow you to retrieve a company's MRR for "Month 0" and compare it to "Month 12" to calculate retention rates.

### 2. SQL Syntax (NDR & GRR Queries)
*   **Definition**: Writing SQL queries that isolate a starting cohort and compute revenue at the start and end of a 12-month window:
    ```sql
    WITH cohort_starting AS (
        SELECT company_key, mrr_amount AS start_mrr
        FROM contract_snapshots
        WHERE snapshot_month = '2025-01-01'
    ),
    cohort_ending AS (
        SELECT company_key, mrr_amount AS end_mrr
        FROM contract_snapshots
        WHERE snapshot_month = '2026-01-01'
    )
    ```
    Joining these CTEs allows you to calculate cohort revenue changes and compute ratios.

### 3. Query Optimization (Cohort Pre-Aggregation)
*   **Definition**: Optimizing slow cohort queries.
*   **GTM Application**: Running recursive self-joins across millions of snapshot rows to compute NDR takes minutes. To optimize:
    *   **Index snap timestamps**: Build B-Tree indexes on `(company_key, snapshot_month)`.
    *   **Materialize views**: Write daily cron scripts that pre-calculate the starting and ending revenue metrics for active cohorts and write them to a `cohort_retention_summary` table.
