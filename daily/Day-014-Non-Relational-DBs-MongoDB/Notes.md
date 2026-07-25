# Study Notes - Day 014: Non-Relational Databases (MongoDB)

Today's studies focused on non-relational document databases (NoSQL/MongoDB), JSON/BSON storage, denormalization, document queries, and document store indexing.

---

## 1. MongoDB in GTM Engineering

While SQL databases are ideal for relational records (like invoices linked to companies), they struggle with highly dynamic, unstructured data (like clickstream events, user settings, or nested webhooks). GTM Engineers use document databases like MongoDB to:

*   **Store Schema-less Data**: Webhook payloads from marketing tools change frequently. MongoDB stores them as raw JSON documents without requiring DDL alterations.
*   **Embed Nested Arrays**: Storing all of a user's page views or touchpoints inside a single `touchpoints` array embedded directly in the lead document, avoiding expensive SQL joins.
*   **Handle High Writes**: NoSQL databases scale horizontally, allowing them to ingest millions of user activity clicks per second.

---

## 2. Deep-Dive: NoSQL Databases Subtopics

To manage document store pipelines, a GTM Engineer must master these three NoSQL subtopics:

### 1. NoSQL Database Design (Denormalization)
*   **Definition**: Embedding related data directly inside a single document rather than splitting it across tables (normalization).
    *   *Embedded Model*: A company document contains an array of contact objects. This allows you to fetch the company and all its contacts in a single query.
    *   *Referenced Model*: Storing contact IDs inside the company document, similar to SQL foreign keys.
*   **GTM Application**: You denormalize user clickstream events by embedding them as a nested list within the lead profile:
    ```json
    {
      "email": "dean@imsgoa.org",
      "touchpoints": [
        {"timestamp": "2026-07-01", "source": "google"},
        {"timestamp": "2026-07-05", "source": "newsletter"}
      ]
    }
    ```

### 2. NoSQL Query Syntax (Filters & Projections)
*   **Definition**: Writing filters to query JSON documents and projections to specify which fields to return.
*   **GTM Application**: You write queries to filter prospects based on nested values:
    *   *Filter*: Find leads where `touchpoints.source` equals `"google"`.
    *   *Projection*: Return only the `email` and `company_name` fields, excluding the large events history array.

### 3. Document Query Optimization (Compound Indexes)
*   **Definition**: Speeding up document queries using single-field, compound, or multikey (indexing array fields) indexes.
*   **GTM Application**:
    *   **Compound Indexes**: If you frequently query by both industry and company size, you create a compound index: `{ industry: 1, employee_count: -1 }`.
    *   **Multikey Indexes**: Created on nested array fields (e.g. `touchpoints.source`) to index each entry in the array separately, keeping search operations fast as history arrays grow.
