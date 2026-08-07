# Project Assignment - Day 023: Token Bucket Rate Limiter

This project requires developing a Python implementation of the Token Bucket Algorithm, designed to act as an inbound rate-limit governor at the API gateway layer. It dynamically calculates token refills based on elapsed timestamps and rejects spikes with status 429.

---

## 🎯 Requirements

Your Python application must:
1.  Create a `TokenBucketRateLimiter` class.
2.  Configure token settings:
    *   `capacity`: The maximum number of tokens allowed in the bucket (e.g. `5` tokens).
    *   `refill_rate`: The number of tokens added per second (e.g. `2` tokens/sec).
3.  Implement dynamic refill tracking:
    *   Rather than running background timer threads, calculate refills dynamically when requests arrive by comparing `current_time - last_request_time`.
4.  Implement request evaluations:
    *   `allow_request(client_id)`: Check if the client's bucket has at least 1 token.
    *   If yes, consume 1 token and return `True` (Simulated HTTP 200 OK).
    *   If no, return `False` (Simulated HTTP 429 Too Many Requests) and specify the time remaining before a token refills.
5.  Execute a loop simulation that:
    *   Fires a burst of 7 rapid requests.
    *   Waits 1.5 seconds.
    *   Fires another burst of 3 requests to show token refilling.

---

## 💻 Deliverable Code

A complete, working rate limiter script has been created and placed in [Code/rate_limiter.py](Code/rate_limiter.py). It models the Token Bucket class, runs the timestamp evaluations, and logs the execution trace.
