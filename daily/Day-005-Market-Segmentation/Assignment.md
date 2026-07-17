# Project Assignment - Day 005: Market Segmentation Engine

This project requires developing a Python analytics script that consumes raw lead lists of schools and coaching centers and calculates the counts, valuation, and classification of TAM, SAM, and SOM target markets.

---

## 🎯 Requirements

Your Python segmentation engine must:
1.  Define a database of school/coaching prospects containing names, locations (country and region), student sizes, board affiliation status (whether they are affiliated with CBSE/ICSE or state boards), and technographics (learning software in use).
2.  Evaluate each prospect against segment rules:
    *   **TAM (Total Addressable Market)**: Includes all accounts in the database.
    *   **SAM (Serviceable Addressable Market)**: Accounts located in India (`country == "IN"`) that are board-affiliated (`is_board_affiliated == True`).
    *   **SOM (Serviceable Obtainable Market)**: Indian, board-affiliated accounts that also utilize target technology (e.g., `Moodle` or `Canvas`) and are in our active sales regions (`North` or `South`).
3.  Calculate the total Contract Values ($ value) for each tier based on a standard Annual Contract Value (ACV) of $1,200.

---

## 💻 Deliverable Code

A complete, working metrics script has been developed and placed in [segmentation_engine.py](file:///D:/Books/90Days-GTM-Engineer/gtm-portfolio-public/daily/Day-005-Market-Segmentation/Code/segmentation_engine.py). It runs these calculations on mock school datasets and prints a tabular summary.