# Reflection - Day 038: Security & Access Control

A personal log reflecting on the learning outcomes and concepts mastered on Day 38.

---

## 💡 Key Takeaways & Lessons Learned

1.  **Decouple security logic from code**: Hardcoding role permissions (e.g. `if user.role == 'Admin'`) makes application updates complex. Decoupling permissions into a normalized database structure allows administrators to adjust access scopes dynamically.
2.  **Enforce Least Privilege with OAuth scope intersection**: When clients request tokens, checking the intersection between requested scopes and their role's permissions ensures they are only granted the minimal necessary access.
3.  **Cache permissions in memory**: Joining multiple relational tables (Users, Roles, Permissions) on every API request introduces performance lag. Caching active tokens and permissions in Redis resolves this bottleneck.

---

## 💻 Script Verification

I ran the `Code/access_control.py` script to test OAuth token issuance, scope stripping, and gateway checks.
*   **Result**: 
    *   *Admin Token*: Granted all requested scopes and successfully accessed `billing:write`.
    *   *Sales Token*: Requested `contacts:read` and `billing:write`. The compiler stripped `billing:write`, issuing a token with only `contacts:read`. The Gateway successfully blocked his access to `billing:write`.
    *   *Marketing Token*: Requested write access. The compiler stripped it, and the Gateway successfully blocked the unauthorized call.
*   **Insight**: This proves that gateway checks successfully prevent unauthorized API queries.

---

## 🎯 Plan for Tomorrow
Tomorrow is Day 39: **Looker Studio (Security & Sharing)**. I will focus on Looker-specific sharing controls, viewer credentials, row-level security (RLS), and email-based data filters to restrict dashboard views.
