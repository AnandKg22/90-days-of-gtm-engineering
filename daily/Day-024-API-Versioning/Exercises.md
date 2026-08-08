# Exercises - Day 024: API Versioning Strategy

This document details the GTM API Versioning Strategy blueprint, outlining path routing and data schema translations.

---

## 📋 API Versioning Strategy Mappings

We compare the implementation patterns for version routing:

| Metric | URL Path Versioning | Header Versioning | Content Negotiation |
| :--- | :--- | :--- | :--- |
| **Example** | `POST /api/v1/prospects` | `X-API-Version: 2026-07-13` | `Accept: application/vnd.crm.v2+json` |
| **Routing Rule** | Evaluates string prefix in router path. | Evaluates custom headers dictionary. | Evaluates HTTP Accept headers parameter. |
| **URL Cleanliness**| Disrupts URLs (changes resource address). | Keeps resource URL address constant. | Keeps resource URL address constant. |
| **Browser Testing**| Simple to test in browser search bars. | Requires custom client request tools. | Requires custom client request tools. |

---

## ⚙️ Schema Transformations (v1 to v2)

Our GTM API exposes a `Prospect` endpoint. As our CRM models evolved, we transformed field names to enforce normalization:

*   **V1 Schema (Legacy)**: Expects a single `fullname` string and target `company` details.
*   **V2 Schema (Current)**: Expects separate `first_name` and `last_name` strings, and target `organization` details.

### Backward Compatibility Mapping Rule:
If a client submits a legacy `v1` payload to our versioned server:
1.  **Extract Name**: Read `fullname`, split by the first whitespace. Assign index `0` to `first_name` and index `1` to `last_name`.
2.  **Extract Org**: Read `company` and assign it to `organization`.
3.  **Forward to V2**: Inject warning headers and forward the normalized payload to our core V2 database engine.
