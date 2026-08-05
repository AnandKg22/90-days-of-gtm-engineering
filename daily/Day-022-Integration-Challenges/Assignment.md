# Project Assignment - Day 022: Error Ingestion & Retry Client

This project requires developing a Python client wrapper script that simulates API queries. It implements exponential backoff with random jitter, detects and skips retries on invalid payloads, writes permanent errors to a local log file, and simulates Dead Letter Queue routing.

---

## 🎯 Requirements

Your Python application must:
1.  Define a mock API client that takes requests and randomly returns:
    *   `200 OK` (Success).
    *   `429 Too Many Requests` (Rate Limited).
    *   `503 Service Unavailable` (Temporary Server Error).
    *   `400 Bad Request` (Invalid Schema Payload).
2.  Implement an **Exponential Backoff with Jitter** retry decorator or loop:
    *   If a request encounters a `429` or `503`, calculate wait time $T = 2^{\text{retry}} + \text{random\_jitter}$.
    *   Print wait times to the console and retry the request up to a max of 3 attempts.
3.  Implement **Immediate Rejection**:
    *   If a request encounters a `400` validation error, do NOT retry. Immediately route the payload to the Dead Letter Queue.
4.  Write permanent failures (records failing after 3 attempts or receiving a `400` error) to a local log file named `integration_failures.log` using Python's `logging` library.

---

## 💻 Deliverable Code

A complete, working integration wrapper script has been created and placed in [Code/error_handler.py](Code/error_handler.py). It models the API behaviors, runs retries, writes error logs, and simulates Slack alerts.
