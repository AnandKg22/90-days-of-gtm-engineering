# Study Notes - Day 010: CRM Pipelines & Velocity Analytics

Today's studies focused on CRM pipelines, stage transition automations, tracking pipeline velocity (historical stage durations), and multi-currency exchange rate conversions.

---

## 1. CRM Pipeline Stage Transitions

In enterprise sales, deals move through sequential pipeline stages. Managing these transitions requires:

*   **Validation Rules**: Preventing reps from skipping stages (e.g. moving a deal directly from Discovery to Contract without sending a proposal).
*   **Transition Workflows**: Automated tasks that execute when a deal changes stages (e.g. alerting legal when a deal hits "Contract Review").
*   **Multi-currency Support**: Standardizing international deals (in INR, SGD, EUR) to a corporate base currency (USD) using daily exchange rate multipliers.

---

## 2. Deep-Dive: CRM Pipelines Subtopics

To implement and analyze pipeline velocity, a GTM Engineer must master these three subtopics:

### 1. Workflow Automation Triggers
*   **Definition**: Business rules executed when a deal enters or exits a pipeline stage.
*   **GTM Application**: You set up webhook listeners that catch stage transition events:
    *   *Exit Discovery*: Verify that a contact role is linked to the deal.
    *   *Enter Proposal*: Auto-generate a PDF proposal and email it to the client.
    *   *Enter Closed Won*: Trigger the Stripe billing script to provision account licenses.

### 2. Deal Stage History (Pipeline Velocity)
*   **Definition**: Auditing and calculating the duration (in days) that a deal spends in each stage.
*   **GTM Application**: Pipeline velocity is the key predictor of sales cycle length. You structure a `deal_stage_history` table in PostgreSQL:
    *   `deal_id`, `stage_name`, `entered_at`, `exited_at`, `duration_seconds`.
    *   Subtracting `exited_at - entered_at` calculates stage velocity.

### 3. Multi-currency Setup & Normalization
*   **Definition**: Normalizing international deal values in the CRM to a single corporate reporting currency.
*   **GTM Application**: You implement an exchange rates table in the database replica. When generating pipeline dashboards, values are multiplied by their conversion rate:
    $$Normalized \; Value \; (USD) = Local \; Currency \; Value \\times USD \; Exchange \; Rate$$
    *Example: An 830,000 INR deal at an exchange rate of 0.012 USD/INR is normalized to $9,960 USD.*
