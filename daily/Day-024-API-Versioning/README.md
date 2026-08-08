# Day 024: API Versioning

## Objective
Understand API versioning and deprecation models, compare URL path vs. header versioning techniques, implement backward compatibility translation layers to normalize legacy fields, and inject standard HTTP `Deprecation` and `Sunset` headers.

## Topics Covered
- API versioning models
- URL path vs. Custom headers versioning
- Backward compatibility mappings
- HTTP Deprecation & Sunset headers
- Versioned webhook ingestion

## Subtopics (Developed in Notes)
- Versioning Models (API Integration)
- Multi-Version Webhook Routing (Webhook Setup)
- Deprecation & Sunset Policies (Security & Governance)

---

## 🛠️ Practical Exercise: Versioning Strategy & Schema Translation

In this exercise, we designed a GTM API versioning strategy and mapping pipeline:
*   **Version Comparison**: Audited path, header, and Accept-header versioning approaches.
*   **Schema Translation (v1 to v2)**: Set rules to dynamically translate legacy v1 requests (keys: `fullname`, `company`) to current v2 structures (keys: `first_name`, `last_name`, `organization`) by splitting string whitespace.

*View complete schema normalization contracts in [Exercises.md](Exercises.md).*

---

## 🏫 Daily Project / Assignment: Versioned API Router

We built an executable Python API router in [Code/versioned_router.py](Code/versioned_router.py):
*   Parses incoming paths for version tags (`/v1/` vs `/v2/`) and falls back to custom headers (`X-API-Version`).
*   Implements **Backward Compatibility Normalization** (parsing and converting legacy v1 payload parameters before writing them to the consolidated database).
*   Injects standard HTTP headers (`Deprecation: true`, `Sunset: Mon, 13 Jul 2026 10:00:00 GMT`) in responses when legacy v1 routes are queried.

*View project requirements in [Assignment.md](Assignment.md) and the versioning flowchart in [Architecture.md](Architecture.md).*

---

## 📂 Expected Deliverables
*   📝 [Day 24 Study Notes](Notes.md) — URL versioning, header versioning, and sunsetting.
*   📝 [Versioning Strategy](Exercises.md) — Target schemas and v1-to-v2 mapping rules.
*   📝 [Versioned Router Spec](Assignment.md) — Project requirements.
*   📊 [Router Process Diagram](Architecture.md) — Version resolution flowchart.
*   💻 [Versioned Router Script](Code/versioned_router.py) — Executable routing and translation engine.

---

## 📝 Notes & Reflection
*   **Key Insight**: Implementing backward-compatible mapping layers in routers allows companies to update internal databases without breaking client integrations running in production.
*   **Study Log**: Read notes in [Notes.md](Notes.md).
*   **Daily Log**: Read reflections in [Reflection.md](Reflection.md).
