# Day 011: Lead Source

## Objective
Understand acquisition channels (Organic, Paid, Referral, Outbound), configure browser UTM parameter cookie trackers, and construct attribution engines that distribute contract revenue among marketing touchpoints.

## Topics Covered
- Acquisition channels
- UTM Parameters
- First-Touch & Last-Touch Attribution

## Subtopics (Developed in Notes)
- UTM Campaign Tracking
- Conversion Source Capture
- Attribution Models (First-Touch vs. Last-Touch)

---

## 🛠️ Practical Exercise: UTM Query builder

In this exercise, we designed the sanitization parameters and URL generation models for VivaExams campaigns:
*   **Paid Search Ad**: `google/cpc/maritime_exam_prep` ──> `https://vivaexams.com/?utm_source=google&utm_medium=cpc&utm_campaign=maritime_exam_prep`
*   **Email Newsletter**: `newsletter/email/july_institutions` ──> `https://vivaexams.com/pricing?utm_source=newsletter&utm_medium=email&utm_campaign=july_institutions`
*   **Outbound Sequence**: `sales_outbound/cold_email/goa_academies` ──> `https://vivaexams.com/demo?utm_source=sales_outbound&utm_medium=cold_email&utm_campaign=goa_academies`

*View full builder input specifications in [Exercises.md](Exercises.md).*

---

## 🏫 Daily Project / Assignment: Lead Attribution Engine

We built an executable Python marketing attribution script in [Code/lead_attribution.py](Code/lead_attribution.py):
*   Models user touchpoint timelines containing timestamps and campaign sources.
*   Calculates **First-Touch Attribution** (attributing 100% of contract value to the initial traffic source that generated awareness).
*   Calculates **Last-Touch Attribution** (attributing 100% of contract value to the converting channel directly preceding the purchase).

*View project requirements in [Assignment.md](Assignment.md) and the system diagram in [Architecture.md](Architecture.md).*

---

## 📂 Expected Deliverables
*   📝 [Day 11 Study Notes](Notes.md) — Marketing channels, UTMs, and attribution models.
*   📝 [UTM URL Builder Spec](Exercises.md) — Parameter builders and URL strings.
*   📝 [Attribution Spec](Assignment.md) — Project requirements.
*   📊 [Attribution Cookie Diagram](Architecture.md) — Client-side cookie tracking flow.
*   💻 [Attribution Engine Script](Code/lead_attribution.py) — Executable touchpoint scoring program.

---

## 📝 Notes & Reflection
*   **Key Insight**: Capturing UTM parameters and saving them in local browser cookies ensures we preserve campaign attribution data even if a visitor takes multiple days to register.
*   **Study Log**: Read notes in [Notes.md](Notes.md).
*   **Daily Log**: Read reflections in [Reflection.md](Reflection.md).
