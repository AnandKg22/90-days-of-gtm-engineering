# Day 015: APIs & Webhooks

## Objective
Understand HTTP REST request methods, headers, and status codes, configure secure webhook receiver endpoints, and implement pre-shared token signature validation handlers.

## Topics Covered
- HTTP REST methods & Headers
- API Authorization methods
- Webhook receiver architectures
- Inbound JSON payload processing
- Webhook status codes

## Subtopics (Developed in Notes)
- API Integration Headers & Auth
- Webhook Setup & Response Handling
- Webhook Security (HMAC Signatures)

---

## 🛠️ Practical Exercise: Webhook Receiver Design

In this exercise, we designed a secure Stripe Webhook Receiver endpoint (`POST /v1/webhooks/stripe`):
*   **Security Header**: Read `Stripe-Signature` to capture timestamp `t` and signature hash `v1`.
*   **Hash Computation**: Compute HMAC-SHA256 of the raw body using webhook secret `whsec_viva_exams_99812`.
*   **Response SLA**: Return status `200 OK` (body: `{"received": true}`) instantly to prevent sender timeouts and retries, handling database writes in the background.

*View complete specifications and security checks in [Exercises.md](Exercises.md).*

---

## 🏫 Daily Project / Assignment: Webhook Receiver Server

We built an executable Python HTTP server in [Code/webhook_server.py](Code/webhook_server.py):
*   Exposes a webhook POST receiver endpoint on `http://localhost:8080/webhook`.
*   Verifies incoming HTTP headers, matching the `X-Webhook-Secret` token.
*   Returns `401 Unauthorized` if validation fails, and `200 OK` with JSON logs upon successful ingestion.
*   Includes an internal unit-test execution mode (`--test`) to test handler pathways without binding ports or hanging the terminal.

*View project requirements in [Assignment.md](Assignment.md) and the system diagram in [Architecture.md](Architecture.md).*

---

## 📂 Expected Deliverables
*   📝 [Day 15 Study Notes](Notes.md) — Webhook setup, response handling, and HMAC.
*   📝 [Receiver Spec Sheet](Exercises.md) — Endpoint specifications and security flows.
*   📝 [Webhook Server Spec](Assignment.md) — Project requirements.
*   📊 [Webhook Sequence Flow](Architecture.md) — Event sequence diagram.
*   💻 [Webhook Receiver Server](Code/webhook_server.py) — Executable HTTP server script.

---

## 📝 Notes & Reflection
*   **Key Insight**: Always return `200 OK` first and process data in background tasks to prevent gateway timeout loops and duplicate event delivery.
*   **Study Log**: Read notes in [Notes.md](Notes.md).
*   **Daily Log**: Read reflections in [Reflection.md](Reflection.md).
