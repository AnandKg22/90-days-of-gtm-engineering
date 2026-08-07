# Reflection - Day 023: API Governance & Rate Limits

A personal log reflecting on the learning outcomes and concepts mastered on Day 23.

---

## 💡 Key Takeaways & Lessons Learned

1.  **Token Bucket balances bursts and limits**: Compared to Leaky Bucket (which delays all requests during a burst) or Fixed Window (which suffers from boundary doubling), Token Bucket is ideal for web traffic since it handles sudden bursts while capping long-term usage.
2.  **On-Demand Refills save server resources**: Running background threads to increment token counts across millions of users wastes CPU loops. Calculating refills dynamically when requests arrive (`elapsed_time * refill_rate`) is much more efficient.
3.  **HTTP Headers guide client behaviors**: Providing a `Retry-After` header tells API consumers exactly how long to wait before retrying. This reduces spam compared to generic error messages.

---

## 💻 Script Verification

I ran the `Code/rate_limiter.py` script to test the Token Bucket algorithm, dynamic refills, and wait calculations.
*   **Result**: 
    *   *Burst 1*: The first 5 requests succeeded instantly (decrementing tokens from 4.0 to 0.0). Requests 6 and 7 were rejected with HTTP 429 and calculated retry wait times.
    *   *Refill Interval*: Successfully waited 1.5 seconds, refilling the bucket.
    *   *Burst 2*: After the refill, 3 requests passed, and the 4th request was blocked with HTTP 429.
*   **Insight**: This proves the math of our Token Bucket limiter operates correctly, successfully shielding APIs from overloading spikes.

---

## 🎯 Plan for Tomorrow
Tomorrow is Day 24: **API Versioning**. I will focus on understanding API change control, URL vs Header versioning strategies, backward compatibility, and deprecation policies.
