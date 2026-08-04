# Project Assignment - Day 018: Segment CDP Simulator

This project requires developing a Python Segment CDP Simulator that processes identity calls, tracks user actions, validates property parameters against a schema, and simulates routing data to down-stream destinations.

---

## 🎯 Requirements

Your Python simulation must:
1.  Create a `SegmentCDP` class to ingest event payloads.
2.  Implement an **Identity Resolution Graph**:
    *   `identify(anonymous_id, user_id, traits)`: Bind the browser's cookie `anonymous_id` to the database `user_id` in an in-memory graph.
3.  Implement a **Tracking Plan Validator**:
    *   `track(user_id, event_name, properties)`: Check if the event name is allowed, and verify that property fields have correct types. If validation fails, log a schema error and reject the event.
4.  Implement **Destination Routing (Multiplexing)**:
    *   Forward successfully validated events to mock destinations: `HubSpot CRM` (updates contacts) and `Google Analytics` (tracks web behavior).

---

## 💻 Deliverable Code

A complete, working simulator script has been created and placed in [Code/segment_simulator.py](Code/segment_simulator.py). It models the CDP, runs the identity resolution maps, validates telemetry schemas, and routes events.
