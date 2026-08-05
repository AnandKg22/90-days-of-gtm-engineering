# Reflection - Day 022: Integration Challenges

A personal log reflecting on the learning outcomes and concepts mastered on Day 22.

---

## 💡 Key Takeaways & Lessons Learned

1.  **Jitter prevents retry collisions**: If a server goes down, and 100 client scripts wait exactly 2.0 seconds to retry, they will hit the server at the exact same millisecond, crashing it again. Adding random jitter (e.g. waiting 2.12 or 2.85 seconds) distributes retry loads.
2.  **Schema Mismatches must never be retried**: Retrying an HTTP 400 Bad Request is useless and wastes CPU resources. Since the schema format is incorrect, it will fail every time. Discard it immediately and alert engineering.
3.  **Dead Letter Queues protect transactions**: Rather than deleting failed transactions when retries fail, saving them to a DLQ table ensures zero data loss. Operations teams can fix the field mapping and re-process the event manually.

---

## 💻 Script Verification

I ran the `Code/error_handler.py` script to test the retry logic, immediate exclusions, and logging.
*   **Result**: 
    *   *Rate limits (429)*: Waited using exponential backoff (e.g. 2.54 seconds) and succeeded on the next try.
    *   *Validation Error (400)*: Instantly aborted retries, routed the record to the DLQ, and wrote the details to the error log file.
    *   *Server Error (500)*: Failed 3 times with increasing backoff delays, then timed out and successfully recorded the payload in `integration_failures.log`.
*   **Insight**: This validates the robust error handling strategy required to secure GTM integrations.

---

## 🎯 Plan for Tomorrow
Tomorrow is Day 23: **API Governance & Rate Limits**. I will focus on understanding API gateways, configuring API quotas, and designing client-side token bucket rate limiters.
