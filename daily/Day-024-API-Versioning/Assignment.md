# Project Assignment - Day 024: Versioned API Router

This project requires developing a Python Versioned API Router simulator. It parses incoming paths and HTTP headers, routes payloads to version-specific controllers, dynamically translates legacy fields for backward compatibility, and injects HTTP deprecation/sunset warnings.

---

## 🎯 Requirements

Your Python application must:
1.  Define a request router class that accepts simulated client requests (path, headers, JSON body).
2.  Implement **Version Resolution**:
    *   Parse the path to check for version codes (e.g. `/v1/prospect` or `/v2/prospect`).
    *   If no path code is found, parse the custom header `X-API-Version: 2026-07-13` to resolve the version.
3.  Implement **Backward Compatibility Normalization**:
    *   If the request is marked `v1`, parse the legacy payload (`fullname`, `company`), split/map the variables, and construct a standardized `v2` payload (`first_name`, `last_name`, `organization`) to forward to the database.
4.  Implement **Deprecation Alerts**:
    *   If a request queries the legacy `v1` version, inject these metadata response headers:
        *   `Deprecation: true`
        *   `Sunset: Mon, 13 Jul 2026 10:00:00 GMT`
5.  Execute mock request test cases validating path routing, header resolution, payload normalization, and deprecation warnings.

---

## 💻 Deliverable Code

A complete, working API router script has been created and placed in [Code/versioned_router.py](Code/versioned_router.py). It models the routes, executes mapping logic, and prints the transaction logs.
