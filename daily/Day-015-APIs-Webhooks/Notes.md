# Study Notes - Day 015: APIs & Webhooks

Today's studies focused on REST APIs, HTTP methods, authorization headers, status codes, webhook payload structures, and HMAC security validation.

---

## 1. REST APIs vs. Webhooks

In B2B GTM systems, software applications communicate in two ways:

*   **REST API (Polling/Pull)**: Your server makes an outbound HTTP request to retrieve data from a system (e.g. GET `/crm/v3/objects/contacts`). This is pull-based.
*   **Webhooks (Push)**: The external system makes an inbound HTTP POST request to your server when an event occurs (e.g. Stripe posts a payload to `/webhooks/stripe` when a payment succeeds). This is push-based and real-time.

---

## 2. Deep-Dive: APIs & Webhooks Subtopics

To construct secure integration servers, a GTM Engineer must master these three subtopics:

### 1. API Integration Headers & Auth
*   **Definition**: Formatting HTTP request headers to authenticate and negotiate content:
    *   `Content-Type: application/json`: Tells the server the payload is JSON.
    *   `Authorization: Bearer <token>`: Authenticates requests using a static API key or OAuth2 token.
    *   `Authorization: Basic <base64_credentials>`: Authenticates requests using username/password keys (like Stripe API keys).
*   **GTM Application**: You configure integrations to inject these headers into outbound API request buffers.

### 2. Webhook Setup & Response Handling
*   **Definition**: Setting up a listener endpoint to consume JSON event payloads.
*   **GTM Application**: Webhook receivers must execute two steps:
    1.  **Fast Acknowledgement**: The receiver must instantly return a `200 OK` status code to the sender. If your server runs heavy database queries before replying, the sender (e.g., Stripe) will timeout, assume your server is down, and retry the request, causing duplicated operations.
    2.  **Async Processing**: Enqueue the payload (e.g., into Redis) to run database updates in the background after returning the `200 OK`.

### 3. Webhook Security (HMAC Signatures)
*   **Definition**: Verifying that the webhook payload was sent by the trusted platform, not a malicious third party.
*   **GTM Application**:
    *   The sender calculates a hash signature of the raw body using a pre-shared secret key and attaches it to the header (e.g., `Stripe-Signature` or `X-Hubspot-Signature`).
    *   Your server reads the signature header, computes its own HMAC hash of the raw request body using the shared secret, and compares the values.
    *   If they match, the payload is authentic. If not, the request is rejected with a `401 Unauthorized` code.
