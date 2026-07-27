# Project Assignment - Day 015: Webhook Receiver Server

This project requires developing an executable Python HTTP server that exposes a webhook endpoint, validates pre-shared authorization secrets, parses event payloads, and returns correct HTTP responses.

---

## 🎯 Requirements

Your Python HTTP server must:
1.  Initialize a lightweight HTTP server listening on `http://localhost:8080/webhook`.
2.  Listen for inbound `POST` requests.
3.  Audit security headers:
    *   Read the header `X-Webhook-Secret`.
    *   Validate the secret value against a pre-shared local secret (`vivaexams_secret_token_1120`).
    *   If the secret is missing or incorrect, return status `401 Unauthorized`.
4.  If authorized, read the JSON body payload containing `event_name` and `data` and log them to the console.
5.  Return status code `200 OK` with header `Content-Type: application/json` and response body:
    ```json
    { "status": "event_processed" }
    ```

---

## 💻 Deliverable Code

A complete, working HTTP server script has been created and placed in [Code/webhook_server.py](Code/webhook_server.py). It implements the base request handler, runs authorization checks, and starts a server listening on port 8080.
