# Day 018: Customer Data Platforms (CDP) / Segment

## Objective
Understand Customer Data Platforms (CDP) architectures, configure identity resolution graphs (anonymous-to-identified mapping), design JSON tracking plan schemas, and multiplex client-side telemetry to CRM and marketing destinations.

## Topics Covered
- CDP architectures
- Identify, Track, Group, and Page calls
- Multiplexing to downstream destinations
- Identity resolution models

## Subtopics (Developed in Notes)
- Identity Resolution (Identity Graph Database Design)
- Segment API Call Standards
- Event Schema Configuration (Tracking Plans)

---

## 🛠️ Practical Exercise: GTM Event Tracking Plan

In this exercise, we designed a standardized Segment Tracking Plan for VivaExams events:
*   **Identify**: Binds anonymous cookie IDs to verified User IDs, mapping email and name traits.
*   **Group**: Binds the contact to a B2B HubSpot Company record.
*   **Exam Completed**: Logs cadet mock exam completions, requiring `exam_id` (string), `score` (number), and `pass_status` (boolean).
*   **Subscription Upgraded**: Logs plan upgrades, requiring `plan_tier` (string), `seats_added` (integer), and `amount` (number).

*View complete tracking plan grids and JSON schema validators in [Exercises.md](Exercises.md).*

---

## 🏫 Daily Project / Assignment: Segment CDP Simulator

We built an executable Python event router simulator in [Code/segment_simulator.py](Code/segment_simulator.py):
*   Implements an in-memory identity graph linking anonymous IDs to User IDs.
*   Implements a **Tracking Plan Validator** that checks incoming event properties against expected types (e.g. rejecting string-based quantities when integers are required).
*   Multiplexes validated events to simulated target destinations: HubSpot CRM and Google Analytics.

*View project requirements in [Assignment.md](Assignment.md) and the connection diagram in [Architecture.md](Architecture.md).*

---

## 📂 Expected Deliverables
*   📝 [Day 18 Study Notes](Notes.md) — CDPs, identity resolution graphs, and tracking schemas.
*   📝 [Event Tracking Plan](Exercises.md) — Event schemas and property validation contracts.
*   📝 [CDP Simulator Spec](Assignment.md) — Project requirements.
*   📊 [Event Routing Diagram](Architecture.md) — Segment ingestion and multiplexing flow.
*   💻 [CDP Event Simulator](Code/segment_simulator.py) — Executable tracking plan validation engine.

---

## 📝 Notes & Reflection
*   **Key Insight**: Implementing tracking schema validation at the ingestion layer (CDP) prevents bad data from corrupting downstream database tables and analytical reports.
*   **Study Log**: Read notes in [Notes.md](Notes.md).
*   **Daily Log**: Read reflections in [Reflection.md](Reflection.md).
