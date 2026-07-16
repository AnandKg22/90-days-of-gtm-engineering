# Day 004: Ideal Customer Profile (ICP)

## Objective
Define and structure Ideal Customer Profiles (ICP) at the organization level, and distinguish them from Buyer and User Personas to build high-performance programmatic lead qualification filters.

## Topics Covered
- Ideal Customer Profile (ICP)
- Buyer Persona
- User Persona

## Subtopics (Developed in Notes)
- Industry
- Company Size
- Revenue
- Technology (Technographics)
- Pain Points
- Buying Signals

---

## 🛠️ Practical Exercise: ICP Profiles

In this exercise, we designed detailed B2B target profiles for our three commercial entities:
1.  **VivaExams B2B ICP**: Focuses on Maritime Academies (50–300 employees) using legacy LMS portals (Moodle) suffering from manual exam grading overhead.
2.  **IMSGOA Sponsorship ICP**: Targets global commercial shipping managers (Singapore/Dubai) with 15+ vessels needing sponsored cadets to mitigate crew training gaps.
3.  **Marine Colleges ICP**: Targets coastal Indian training institutions requiring compliance tracking with DGS (Director General of Shipping) standards.

*View complete profiles in [Exercises.md](Exercises.md).*

---

## 🏫 Daily Project / Assignment: ICP Validator Engine

We built an executable Python lead validation script in [Code/icp_validator.py](Code/icp_validator.py):
*   Evaluates incoming leads on a 100-point scale across **Industry** (35 pts), **Company Size** (25 pts), **Technographics** (20 pts), and **Geography** (20 pts).
*   Sorts prospects into **High Fit**, **Medium Fit**, or **Low Fit** tiers to prioritize automated sales queues.
*   Enforces boundary conditions (e.g. flagging `Tolani Maritime Academy` as High Fit and sorting out-of-spec software startups as Low Fit).

*View project requirements in [Assignment.md](Assignment.md) and the system diagram in [Architecture.md](Architecture.md).*

---

## 📂 Expected Deliverables
*   📝 [Day 4 Study Notes](Notes.md) — Profiles definitions and deep-dive subtopics guides.
*   📝 [ICP Target Models](Exercises.md) — Detailed specifications for our three organizations.
*   📝 [ICP Validator Specs](Assignment.md) — Project scoring requirements.
*   📊 [Lead Routing Diagram](Architecture.md) — Webhook-to-CRM API sequence.
*   💻 [ICP Validator Script](Code/icp_validator.py) — Executable lead scoring program.

---

## 📝 Notes & Reflection
*   **Key Insight**: Implementing automated technographic checks (e.g. checking if a college page contains Moodle tags) cuts sales onboarding time and increases pipeline conversion.
*   **Study Log**: Read notes in [Notes.md](Notes.md).
*   **Daily Log**: Read reflections in [Reflection.md](Reflection.md).

---

## 👤 Author & Connect

Developed by **Anand Kumar** — Go-To-Market Architect & Revenue Engineer.
*   **Website**: [akstack.com](https://akstack.com)
*   **GitHub**: [github.com/AnandKg22](https://github.com/AnandKg22)
*   **LinkedIn**: [linkedin.com/in/anandkg22](https://www.linkedin.com/in/anandkg22/)
