# Study Notes - Day 023: API Governance & Rate Limiting

Today's studies focused on API governance structures, rate-limiting algorithms (Token Bucket, Leaky Bucket, Fixed Window, Sliding Log), client-side throttling governors, and API gateway security protections.

---

## 1. Why API Governance?

When building microservices and GTM integrations, API endpoints must be protected from resource depletion:

*   **Denial of Service (DoS)**: A bug in a front-end script running in a loop can send 10,000 requests per second, crashing the backend database.
*   **Cost Control**: Third-party APIs (like OpenAI or enrichments) charge per call. Governance limits how many requests a user or client token can run.
*   **Fairness**: Ensuring one customer does not consume all API server threads, leaving other customers experiencing slow load times.

---

## 2. Deep-Dive: API Governance & Rate Limits Subtopics

To construct secure, robust GTM services, a GTM Engineer must master these three rate-limiting subtopics:

### 1. Client-Side API Throttling (API Integration)
*   **Definition**: Building outbound rate-limit governors into integration scripts to keep requests within target provider quotas (e.g. Stripe's limit of 100 requests/sec).
*   **GTM Application**: You configure a queue runner that tracks outbound request speed, forcing a delay (e.g. sleep 10ms) between calls when approaching the limit.

### 2. Inbound Webhook Rate Governors (Webhook Setup)
*   **Definition**: Implementing ingress rate limiters on public webhook endpoint paths (`POST /webhook/stripe`) to reject request spikes or queue them safely.
*   **GTM Application**: If Stripe sends 500 webhooks in 1 second, the receiver gateway accepts the connections, writes them to Redis, but enforces a rate-limiting policy (e.g. process 10 events/sec) to protect the CRM from crash-locking.

### 3. API Gateway Security (Security & Governance)
*   **Definition**: Implementing rate limiters at the gateway level (e.g., Kong, AWS API Gateway) using token or bucket algorithms to block malicious requests before they reach application servers.
*   **GTM Application**: You configure IP-based and API-key-based rate-limit rules. If a client exceeds the threshold, the gateway instantly returns `429 Too Many Requests` with a `Retry-After: 5` header, bypassing the application stack entirely.
