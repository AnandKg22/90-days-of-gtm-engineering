# Study Notes - Day 029: Looker Studio Data Blending & SQL Joins

Today's studies focused on Looker Studio Data Blending, mapping join keys, relational SQL join types (Left Outer, Inner, Full Outer), and the performance limitations of client-side blending.

---

## 1. What is Looker Studio Data Blending?

**Data Blending** allows you to join multiple disparate data sources (like matching Stripe billing transactions to Google Analytics session logs or HubSpot contact records) directly inside the Looker Studio interface. 

*   Each data blend can join up to 5 tables.
*   Every joined table must share at least one common **Join Key** (e.g. `email` or `company_domain`).

---

## 2. Deep-Dive: Looker Blending Subtopics

To construct integrated sales reporting engines, a GTM Engineer must master these three blending subtopics:

### 1. Dashboard Design (The Blending Canvas)
*   **Definition**: Configuring joins visually inside Looker's Blending Panel:
    *   **Join Keys**: Mapped columns that identify matching records (e.g. HubSpot `email` ──> Stripe `customer_email`).
    *   **Dimensions**: Grouping fields pulled from both tables (e.g., Lead Source from HubSpot, Plan Tier from Stripe).
    *   **Metrics**: Quantitative values aggregated from both tables (e.g. sum of Stripe charges).

### 2. SQL Syntax (Relational Join Operators)
*   **Definition**: Coding explicit SQL joins to combine database tables on disk:
    *   **Left Outer Join (Default Looker Blend)**: Returns all records from the left table, and matching records from the right. If no match exists, right columns return `NULL`. Critical in GTM to preserve all leads, even if they have not made a payment.
    *   **Inner Join**: Returns rows ONLY when there is a match in both tables. Leads without payments are dropped.
    *   **Full Outer Join**: Returns all records when there is a match in either left or right tables.
    *   **Right Outer Join**: Returns all records from the right table, and matching records from the left.

### 3. Query Optimization (The Cost of Client-Side Blending)
*   **Definition**: Managing browser performance and database scan costs.
*   **GTM Application**:
    *   *How Blending Works*: Looker does not run a single SQL join query in the warehouse. Instead, it queries each database source separately, loads all rows into the browser's JavaScript memory, and runs the join client-side.
    *   *The Performance Cost*: If both tables are large (e.g., 50,000 leads and 100,000 events), client-side data blending will freeze the user's browser.
    *   *The Best Practice*: Avoid Looker Blending. Perform joins at the database tier using dbt models or SQL joins, exposing a single pre-joined table to Looker.
