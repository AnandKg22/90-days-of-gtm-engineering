# Day 005: Market Segmentation & Positioning

## Objective
Analyze Total Addressable Market (TAM), Serviceable Addressable Market (SAM), and Serviceable Obtainable Market (SOM), and segment prospects using firmographic, geographic, and technographic criteria.

## Topics Covered
- TAM, SAM, and SOM definitions
- Market Segmentation vectors
- Positioning strategies

## Subtopics (Developed in Notes)
- Industry Niche (e.g., K-12 Private Schools vs. Test-Prep Coaching Centers)
- Student / Employee Count (Scale of the institute)
- Revenue / Institutional Budget
- Country / Geography (Regulatory and curriculum boards)
- Technology / Technographics (LMS portals like Moodle or Canvas)
- Intent / Behavioral (Active interest in AI-grading features)

---

## 🛠️ Practical Exercise: Segmenting Coaching & Tutoring Institutes

In this exercise, we calculated the revenue potentials for **SmartStudy Classrooms** (a B2B SaaS platform sold to schools and tuition centers to auto-generate worksheets and grade tests with AI) across three market layers:
1.  **TAM (Global)**: ~10,000,000 private K-12 schools and coaching institutes globally, valued at **$20,000,000,000 / year** ($2,000 ACV).
2.  **SAM (India)**: ~200,000 private schools and coaching institutes in India, valued at **$300,000,000 / year** ($1,500 ACV).
3.  **SOM (Target)**: ~1,000 test-prep coaching centers in metropolitan hubs (Kota, Delhi, Hyderabad, Bengaluru) specializing in JEE/NEET/Boards using digital systems, valued at **$1,200,000 / year** ($1,200 ACV).

*View complete segment descriptions in [Exercises.md](file:///D:/Books/90Days-GTM-Engineer/gtm-portfolio-public/daily/Day-005-Market-Segmentation/Exercises.md).*

---

## 🏫 Daily Project / Assignment: Market Segmentation Engine

We built an executable Python analytics calculator in [segmentation_engine.py](file:///D:/Books/90Days-GTM-Engineer/gtm-portfolio-public/daily/Day-005-Market-Segmentation/Code/segmentation_engine.py):
*   Processes raw lists of educational coaching accounts containing student counts, locations, board affiliation status, and technographics.
*   Partitions the database into TAM, SAM, and SOM segments.
*   Calculates the total ACV (Annual Contract Value) potential for each tier to prioritize go-to-market resources.

*View project requirements in [Assignment.md](file:///D:/Books/90Days-GTM-Engineer/gtm-portfolio-public/daily/Day-005-Market-Segmentation/Assignment.md) and the system diagram in [Architecture.md](file:///D:/Books/90Days-GTM-Engineer/gtm-portfolio-public/daily/Day-005-Market-Segmentation/Architecture.md).*

---

## 📂 Expected Deliverables
*   📝 [Day 5 Study Notes](file:///D:/Books/90Days-GTM-Engineer/gtm-portfolio-public/daily/Day-005-Market-Segmentation/Notes.md) — Market definitions and deep-dive subtopics guides.
*   📝 [TAM/SAM/SOM Models](file:///D:/Books/90Days-GTM-Engineer/gtm-portfolio-public/daily/Day-005-Market-Segmentation/Exercises.md) — Valuation math and target classifications.
*   📝 [Segmentation Spec](file:///D:/Books/90Days-GTM-Engineer/gtm-portfolio-public/daily/Day-005-Market-Segmentation/Assignment.md) — Project requirements.
*   📊 [Segmentation Diagram](file:///D:/Books/90Days-GTM-Engineer/gtm-portfolio-public/daily/Day-005-Market-Segmentation/Architecture.md) — Account filtration and SQL database routing.
*   💻 [Segmentation Script](file:///D:/Books/90Days-GTM-Engineer/gtm-portfolio-public/daily/Day-005-Market-Segmentation/Code/segmentation_engine.py) — Executable market analysis calculator.

---

## 📝 Notes & Reflection
*   **Key Insight**: Segmenting a database by technology fit (e.g., searching for schools that already use Moodle or Canvas) isolates high-probability accounts. It is much easier to sell an AI plug-in to a school that is already digital than to a school that relies entirely on paper.
*   **Study Log**: Read notes in [Notes.md](file:///D:/Books/90Days-GTM-Engineer/gtm-portfolio-public/daily/Day-005-Market-Segmentation/Notes.md).
*   **Daily Log**: Read reflections in [Reflection.md](file:///D:/Books/90Days-GTM-Engineer/gtm-portfolio-public/daily/Day-005-Market-Segmentation/Reflection.md).
