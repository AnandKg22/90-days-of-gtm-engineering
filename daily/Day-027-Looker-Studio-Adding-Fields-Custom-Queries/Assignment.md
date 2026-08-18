# Project Assignment - Day 027: Calculated Fields & Custom SQL Engine

This project requires developing a Python Looker Studio calculated fields engine. It parses string concatenation formulas (`CONCAT`), type casts (`CAST`), and conditional segments (`CASE`), and compares frontend browser calculation speeds against warehouse pre-compiled queries.

---

## 🎯 Requirements

Your Python application must:
1.  Define a mock dataset containing:
    *   `first_name`, `last_name`, `email`, `employees`, `seats_string`.
2.  Implement a **Calculated Field Parser**:
    *   `concat_name(first, last)`: Simulates `CONCAT` to merge name strings.
    *   `case_tier(employees)`: Simulates `CASE` (employees > 50 ──> "Enterprise", else ──> "SME").
    *   `cast_seats(seats_str)`: Simulates `CAST` to convert string keys to numbers.
3.  Implement a **Performance Optimizer Audit**:
    *   Compare the rendering time of calculating formulas in a row-by-row frontend execution loop versus loading pre-compiled custom SQL tables.
    *   Log performance recommendations based on the execution times.

---

## 💻 Deliverable Code

A complete, working calculated fields engine script has been created and placed in [Code/calculated_fields_engine.py](Code/calculated_fields_engine.py). It models the dataset, executes the formulas, and compares execution times.
