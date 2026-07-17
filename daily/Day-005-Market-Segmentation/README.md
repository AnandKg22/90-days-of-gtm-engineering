# Day 005: Market Segmentation & Positioning

## Objective
Analyze Total Addressable Market (TAM), Serviceable Addressable Market (SAM), and Serviceable Obtainable Market (SOM), and segment prospects using firmographic, geographic, and technographic criteria.

## Topics Covered
- TAM, SAM, and SOM definitions
- Market Segmentation vectors
- Positioning strategies

## Subtopics (Developed in Notes)
- Industry Niche
- Employee Count
- Revenue
- Country (Geography)
- Technology (Technographics)
- Intent (Behavioral)

---

## 🛠️ Practical Exercise: Segmenting Marine Institutes

In this exercise, we calculated the revenue potentials for VivaExams across three market layers:
1.  **TAM (Global)**: ~4,500 maritime education centers worldwide, valued at **$45,000,000 / year** ($10k ACV).
2.  **SAM (India)**: ~160 DGS-approved maritime academies in India, valued at **$1,280,000 / year** ($8k ACV).
3.  **SOM (Target)**: ~50 private maritime academies in West/South India running Moodle, valued at **$400,000 / year** ($8k ACV).

*View complete segment descriptions in [Exercises.md](Exercises.md).*

---

## 🏫 Daily Project / Assignment: Market Segmentation Engine

We built an executable Python analytics calculator in [Code/segmentation_engine.py](Code/segmentation_engine.py):
*   Processes raw lists of maritime accounts containing geolocations, student counts, and technographics.
*   Partitions the database into TAM, SAM, and SOM segments.
*   Calculates the total ACV (Annual Contract Value) potential for each tier to prioritize go-to-market resources.

*View project requirements in [Assignment.md](Assignment.md) and the system diagram in [Architecture.md](Architecture.md).*

---

## 📂 Expected Deliverables
*   📝 [Day 5 Study Notes](Notes.md) — Market definitions and deep-dive subtopics guides.
*   📝 [TAM/SAM/SOM Models](Exercises.md) — Valuation math and target classifications.
*   📝 [Segmentation Spec](Assignment.md) — Project requirements.
*   📊 [Segmentation Diagram](Architecture.md) — Account filtration and SQL database routing.
*   💻 [Segmentation Script](Code/segmentation_engine.py) — Executable market analysis calculator.

---

## 📝 Notes & Reflection
*   **Key Insight**: Segmenting a database by technology fit (e.g. searching for Moodle users) isolates high-probability accounts, reducing sales friction and lowering CAC.
*   **Study Log**: Read notes in [Notes.md](Notes.md).
*   **Daily Log**: Read reflections in [Reflection.md](Reflection.md).
