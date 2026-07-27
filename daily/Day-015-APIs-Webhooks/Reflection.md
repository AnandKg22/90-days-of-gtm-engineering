# Reflection - Day 015: APIs & Webhooks

A personal log reflecting on the learning outcomes and concepts mastered on Day 15.

---

## 💡 Key Takeaways & Lessons Learned

1.  **Fast Webhook Acknowledgement is Mandatory**: If a webhook receiver runs heavy database reads or writes synchronously before returning a response, the calling gateway will timeout and retry the event. Instantly returning `200 OK` and running the database logic asynchronously is the only way to scale.
2.  **Signature Validation protects resources**: Webhook endpoints are public URLs. Anyone can send mock POST requests to `/webhook` attempting to trigger mock purchases. Enforcing header signature checks (HMAC hashes) is mandatory to prevent unauthorized data injections.
3.  **Basic Auth vs. Bearer Tokens**: Understanding header formatting (e.g. Base64 encoding credentials for Basic Auth vs pasting Bearer tokens) simplifies troubleshooting API integration errors.

---

## 💻 Script Verification

I ran the `Code/webhook_server.py` script with the `--test` flag to verify the request handler logic.
*   **Result**: 
    *   *Test 1 (Valid Secret)*: Successfully returns `200 OK`, outputs the `[INBOUND WEBHOOK RECEIVED]` log, and parses the payload.
    *   *Test 2 (Invalid Secret)*: Successfully detects the invalid key and rejects the request with `401 Unauthorized`.
*   **Insight**: The test suite validates our server logic without needing an external HTTP request client or port bindings.

---

## 🎯 Plan for Tomorrow
Tomorrow is Day 16: **Integration Tools (n8n)**. I will focus on understanding n8n workflow nodes, creating trigger nodes, configuring HTTP request nodes, and building automated data sync workflows.
