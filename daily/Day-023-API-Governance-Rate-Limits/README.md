# Day 023: API Governance & Rate Limits

## Objective
Understand API Governance requirements, evaluate the trade-offs of rate-limiting algorithms (Token Bucket, Leaky Bucket, Fixed Window, and Sliding Log), and implement a Token Bucket rate-limit governor at the API gateway layer to block client spikes and issue Retry-After headers.

## Topics Covered
- API Governance models
- Rate limiting algorithms
- Token Bucket implementation
- HTTP 429 Retry-After headers
- API Gateway security rules

## Subtopics (Developed in Notes)
- Client-Side API Throttling (API Integration)
- Inbound Webhook Rate Governors (Webhook Setup)
- API Gateway Security (Security & Governance)

---

## 🛠️ Practical Exercise: Rate Limiting Algorithms Blueprint

In this exercise, we compared the four core API rate-limiting algorithms:
*   **Token Bucket**: Allows sudden traffic bursts while enforcing long-term rate limits. Ideal for public web APIs.
*   **Leaky Bucket**: Leaks requests at a constant, flat rate. Ideal for database-heavy CRM syncs.
*   **Fixed Window**: Simple resets at time boundaries, but suffers from double-quota spikes at window splits.
*   **Sliding Log**: Precise timestamp tracking, but high memory footprint.

*View the complete comparative matrix and database schemas in [Exercises.md](Exercises.md).*

---

## 🏫 Daily Project / Assignment: Token Bucket Rate Limiter

We built an executable Python rate limiter in [Code/rate_limiter.py](Code/rate_limiter.py):
*   Implements the **Token Bucket Algorithm** with a capacity of 5 tokens and a refill rate of 2 tokens per second.
*   Enforces **On-Demand Refills** (calculating token increases dynamically when requests arrive by comparing time deltas, saving CPU cycles).
*   Returns `True` (HTTP 200) for approved requests, and `False` (HTTP 429) with calculated retry-after durations for blocked requests.
*   Includes a burst simulation testing requests before and after token refilling.

*View project requirements in [Assignment.md](Assignment.md) and the logical flowchart in [Architecture.md](Architecture.md).*

---

## 📂 Expected Deliverables
*   📝 [Day 23 Study Notes](Notes.md) — API governance, rate algorithms, and client throttling.
*   📝 [Rate Algorithms Blueprint](Exercises.md) — Comparative matrix of throttling designs.
*   📝 [Rate Limiter Spec](Assignment.md) — Project requirements.
*   📊 [Throttling Flowchart](Architecture.md) — Visual gateway rate-limit logic tree.
*   💻 [Token Bucket Limiter](Code/rate_limiter.py) — Executable rate-governor script.

---

## 📝 Notes & Reflection
*   **Key Insight**: Utilizing on-demand timestamp checks (`elapsed * refill_rate`) to calculate token refilling replaces resource-intensive timer loops, allowing the limiter to scale to millions of requests.
*   **Study Log**: Read notes in [Notes.md](Notes.md).
*   **Daily Log**: Read reflections in [Reflection.md](Reflection.md).
