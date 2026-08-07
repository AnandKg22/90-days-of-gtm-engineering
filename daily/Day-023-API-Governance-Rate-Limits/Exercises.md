# Exercises - Day 023: Rate Limiting Algorithms Blueprint

This document details the comparative blueprint of the four core rate-limiting algorithms utilized to govern API integrations.

---

## 📊 Rate Limiting Algorithms Comparison

| Algorithm | Core Operation | Pros | Cons | Ideal GTM Use Case |
| :--- | :--- | :--- | :--- | :--- |
| **Token Bucket** | Tokens accumulate in a bucket up to `capacity`. Each request consumes 1 token. Refills at a set `refill_rate` (tokens/sec). | Handles sudden bursts of traffic gracefully. | Can overwhelm downstream systems during large bursts. | **Public APIs / Stripe Integrations**: Supports fast page views while protecting the server. |
| **Leaky Bucket** | Requests enter a queue and leak out at a constant, fixed rate. Queue overflow rejects requests. | Produces a smooth, constant output flow. | Delays requests during bursts; requires queue memory. | **HubSpot CRM Syncs**: Ensures CRM writes remain flat and constant. |
| **Fixed Window** | Counts requests in fixed time windows (e.g. 100/minute). Resets count at window boundaries. | Extremely simple memory footprint; easy to implement. | Bursts at window boundaries can double the rate limit (e.g. 100 at 0:59, 100 at 1:00). | **Basic SaaS API Keys**: Restricting monthly search quotas. |
| **Sliding Log** | Logs timestamps of every request in memory (e.g. Redis Sorted Sets). Deletes logs older than 1 minute. | High accuracy; prevents window boundary bursts completely. | High memory consumption tracking millions of timestamps. | **Financial Transaction APIs**: High-security, low-volume pipelines. |
