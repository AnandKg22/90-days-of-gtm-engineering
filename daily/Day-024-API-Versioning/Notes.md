# Study Notes - Day 024: API Versioning & Deprecation

Today's studies focused on API versioning strategies (URL path, Custom headers, Accept content negotiation), backward compatibility mappings, and HTTP deprecation policies (Sunset/Deprecation headers).

---

## 1. Why API Versioning?

SaaS systems evolve. Over time, you need to change data structures, rename fields, or drop fields entirely. Without versioning:
*   Updating your API will crash downstream scripts running in production.
*   **API Versioning** allows legacy applications to query old endpoints safely, while new integrations use updated data structures.

---

## 2. Deep-Dive: API Versioning Subtopics

To maintain high-availability GTM pipelines, a GTM Engineer must master these three versioning subtopics:

### 1. Versioning Models (API Integration)
*   **Definition**: Methods for defining the requested version in HTTP calls:
    *   **URL Path Versioning**: Version is hardcoded in the path (e.g., `GET /v1/leads`). Simple to route and audit, but changes URLs.
    *   **Custom Header Versioning**: Version is sent in a custom header (e.g. `X-API-Version: 2026-07-13`). Keeps URLs clean; allows Stripe-style granular versioning.
    *   **Accept Header Versioning**: Version is defined in the media type content header (e.g. `Accept: application/vnd.vivaexams.v2+json`). Most REST-compliant, but complex to parse.

### 2. Multi-Version Webhook Routing (Webhook Setup)
*   **Definition**: Webhook listener architectures that accept and normalize multiple payload layouts based on the version header sent by the provider.
*   **GTM Application**: Stripe webhooks include a `Stripe-Version` header. Your receiver must read this header and run version-specific parser classes to normalize fields before writing them to the CRM.

### 3. Deprecation & Sunset Policies (Security & Governance)
*   **Definition**: Standardizing how legacy endpoints are decommissioned without breaking customer code.
*   **GTM Application**: You inject specific HTTP headers in responses for deprecated routes:
    *   `Deprecation: true`: Signals the route is deprecated.
    *   `Sunset: Mon, 13 Jul 2026 10:00:00 GMT`: Defines the date the endpoint will be turned off.
    *   Central monitoring parses logs for these warning headers to alert teams to update integrations.
