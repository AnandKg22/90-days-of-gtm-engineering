# Study Notes - Day 022: GTM Integration Challenges & Recovery

Today's studies focused on API rate limits (HTTP 429), sync failure states, exponential backoff with jitter, schema conflicts, and Dead Letter Queue (DLQ) architectures.

---

## 1. System Integration Bottlenecks

Integrating multiple B2B SaaS APIs (Stripe, HubSpot, Outreach, Slack) introduces architectural points of failure:

*   **API Rate Limiting**: Platforms restrict the number of requests per second (e.g. HubSpot API limits requests to 100/10 seconds). Exceeding this returns an HTTP `429 Too Many Requests` code.
*   **Schema Mismatch**: A field name change in one tool causes sync scripts to fail payload validation.
*   **Custom Identifiers (ID Mapping)**: Connecting records when different tools use different primary keys (e.g., Stripe uses `cus_1234`, HubSpot uses `5543102`, and your app database uses UUIDs).

---

## 2. Deep-Dive: Integration Challenges Subtopics

To construct fault-tolerant GTM integrations, a GTM Engineer must master these three subtopics:

### 1. API Rate Limiting & Backoff (API Integration)
*   **Definition**: Handling API volume throttling securely.
*   **GTM Application**: You write wrappers around API call requests:
    *   **Exponential Backoff**: When a call receives a `429` status code, wait $2^x$ seconds before retrying (where $x$ is the retry count).
    *   **Jitter**: Adding a random float value to the wait time (e.g. waiting $4.12$ seconds instead of exactly $4.00$). This prevents multiple parallel scripts from retrying at the exact same millisecond, which overloads the destination server again.

### 2. Webhook Spikes & Ingestion Queues (Webhook Setup)
*   **Definition**: Buffering incoming webhook bursts to prevent server crashes.
*   **GTM Application**: When a marketing campaign goes viral, webhooks spike from 10/min to 1,000/sec. To prevent database timeouts:
    *   The webhook receiver writes the raw payload to a fast in-memory queue (like Redis).
    *   A background worker consumes from the queue at a throttled pace, keeping CRM API writes within safe limits.

### 3. Error Handling & Dead Letter Queues (Security & Errors)
*   **Definition**: Routing permanently failed requests to a separate storage bucket for manual auditing.
*   **GTM Application**:
    *   *System Error (500/503)*: Retried automatically up to 5 times.
    *   *Validation Error (400 Bad Request)*: Discarded from active runs immediately.
    *   **Dead Letter Queue (DLQ)**: If a request fails all 5 retry attempts, the payload is written to a DLQ database. A Slack notification alerts RevOps to inspect and manually re-run the transaction.
