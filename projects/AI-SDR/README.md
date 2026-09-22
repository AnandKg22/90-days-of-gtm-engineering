# Day 045: AI SDR Agent

## Objective
Build an automated **AI SDR Agent (v2)** that qualifies leads based on intent scores, generates structured 4-touch outbound sequences (Email, LinkedIn, Follow-up, Break-up), schedules delivery offset dates, and synchronizes status logs to CRMs.

## Topics Covered
- Lead Qualification: Threshold check gates
- Outbound Sequencing: Touchpoint frameworks
- Personalized Copywriting: Ingesting firmographics and pain points
- Dynamic Task Scheduling (Datetime offset modeling)
- CRM updates: Syncing sequence stages and logging actions

## Subtopics (Developed in Notes)
- Multichannel Campaigns (Email + LinkedIn)
- Outbound Scheduling Algorithms
- Lead Stage State Transitions in CRMs
- Dynamic Personalization Variable mappings
- Outreach metrics tracking (open, reply rates)

---

## 🛠️ Practical Exercise: Multichannel Sequencing

In this exercise, we designed a 4-touch outbound sequence for B2B SaaS target buyers:
*   **Touch 1 (Day 1 - Cold Email)**: Hooking the buyer using their tech stack and operational pain points.
*   **Touch 2 (Day 4 - LinkedIn Connect)**: Conversational request validating their industry growth.
*   **Touch 3 (Day 8 - Follow-up Email)**: Case study social proof showing value outcomes.
*   **Touch 4 (Day 15 - Break-up Email)**: Soft closing invitation giving them permission to close the file.

*View complete email scripts and schedule offsets in [Exercises.md](Exercises.md).*

---

## 🏫 Daily Project / Assignment: AI SDR v2 Engine

We completed two primary deliverables:
1.  **AI SDR v2 Generator**: An executable Python campaign scheduler in [Code/ai_sdr_v2.py](Code/ai_sdr_v2.py) that qualifies leads, compiles outreach copy, schedules offset times, and simulates CRM status changes.
2.  **SDR Sequence Blueprints**: Outbound state charts and schemas detailed in [Assignment.md](Assignment.md) and [Architecture.md](Architecture.md).

---

## 📂 Expected Deliverables
*   📝 [Day 45 Study Notes](Notes.md) — Campaign topologies, state machines, and scheduling math.
*   📝 [Sequence Design Spec](Exercises.md) — Multichannel scripts and schedule intervals.
*   📝 [Project Assignment Spec](Assignment.md) — Technical requirements for the SDR v2 engine.
*   📊 [SDR Campaign Flow](Architecture.md) — Mermaid sequence diagram mapping out outreach touchpoints.
*   💻 [AI SDR v2 Engine](Code/ai_sdr_v2.py) — Executable Python campaign sequence compiler.
*   📋 [SDR Cheat Sheet](CheatSheet.md) — Key terms, touchpoint guides, and scheduling code blocks.
*   🤖 [SDR Copywriting Prompts](Prompts.md) — Prompts for compiling cold emails and LinkedIn hooks.
*   🔗 [SDR Resources](Resources.md) — Links to outbound deliverability, Lemlist, and Apollo.io APIs.
*   📝 [Daily Reflection](Reflection.md) — Learnings, sequence verifications, and preview of Day 46.

---

## 📝 Notes & Reflection
*   **Key Insight**: An SDR agent cannot rely on single blast messages. Successful outbound requires multichannel coordination (Email + LinkedIn) and structured follow-up scheduling mapped directly to lead timelines.
*   **Study Log**: Read notes in [Notes.md](Notes.md).
*   **Daily Log**: Read reflections in [Reflection.md](Reflection.md).

---

## 👤 Author & Connect

Developed by **Anand Kumar** — Go-To-Market Architect & Revenue Engineer.
*   **Website**: [akstack.com](https://akstack.com)
*   **GitHub**: [github.com/AnandKg22](https://github.com/AnandKg22)
*   **LinkedIn**: [linkedin.com/in/anandkg22](https://www.linkedin.com/in/anandkg22/)
