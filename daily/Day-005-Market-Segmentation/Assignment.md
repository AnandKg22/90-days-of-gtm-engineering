# Project Assignment - Day 005: Market Segmentation Engine

This project requires developing a python analytics script that consumes raw lead lists and calculates the counts, valuation, and classification of TAM, SAM, and SOM target markets.

---

## 🎯 Requirements

Your Python segmentation engine must:
1.  Define a database of prospects containing names, locations, employee sizes, DGS approval status, and technographics.
2.  Evaluate each prospect against segment rules:
    *   **TAM (Total Addressable Market)**: Includes all accounts in the system.
    *   **SAM (Serviceable Addressable Market)**: Accounts located in India (`country == "IN"`) that are DGS-approved.
    *   **SOM (Serviceable Obtainable Market)**: Indian, DGS-approved accounts that also utilize target technology (e.g. `Moodle` or `Blackboard`) and are in South/West regions.
3.  Calculate the total Contract Values ($ value) for each tier.

---

## 💻 Deliverable Code

A complete, working metrics script has been developed and placed in [Code/segmentation_engine.py](Code/segmentation_engine.py). It runs these calculations on mock datasets and prints a tabular summary.