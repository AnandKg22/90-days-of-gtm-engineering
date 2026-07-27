# Exercises - Day 015: Webhook Receiver Blueprint

This document details the functional blueprint and payload validation rules designed for a secure Stripe Webhook Receiver endpoint.

---

## 🛠️ Webhook Receiver Specifications

To ingest billing updates securely and prevent timeout bottlenecks, the receiver is configured with the following parameters:

*   **Endpoint Routing**: `POST /v1/webhooks/stripe`
*   **Security Header**: `Stripe-Signature` (contains timestamp `t` and hash signature `v1`).
*   **Response SLA**: Returns `200 OK` within 2 seconds.

---

## 🔒 Verification & Ingest Sequence

Below is the step-by-step logic executed by the server when a webhook request is received:

1.  **Extract Raw Body**: Read the raw, unparsed request body as bytes.
2.  **Fetch Header**: Extract the `Stripe-Signature` header.
3.  **Compute HMAC**:
    *   Retrieve the pre-shared webhook signing secret (`whsec_viva_exams_99812`).
    *   Compute the HMAC-SHA256 hash using the raw request body bytes and the secret.
4.  **Compare Signatures**:
    *   Compare the calculated hash with the `v1` signature from the header.
    *   If signatures match, proceed. If they do not, return `401 Unauthorized` and drop the request.
5.  **Enqueue for Background Job**:
    *   Fires a task to a background task queue (e.g. Redis).
    *   The background worker parses the JSON to extract:
        *   `event.type`: `checkout.session.completed`
        *   `data.object.customer_email`: `dean@imsgoa.org`
6.  **Return Success Response**: Return HTTP status `200 OK` with JSON body:
    ```json
    { "received": true }
    ```
