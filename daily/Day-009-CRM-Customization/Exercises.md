# Exercises - Day 009: CRM Custom Property Definitions

This document details the custom CRM property configurations (HubSpot API schema compatible) designed for B2B VivaExams accounts.

---

## ⚙️ Custom Properties Schema Specifications

To track maritime academy metrics, we define five custom properties on the Company object:

### 1. Cadet Seats Purchased
*   **API Name**: `cadet_seats_purchased`
*   **Field Type**: `number`
*   **Description**: The total number of active exam prep licenses purchased by the institution.
*   **Validation**: Integer, minimum value = `0`.

### 2. Mock Exam Pass Rate %
*   **API Name**: `exam_pass_rate_percent`
*   **Field Type**: `number`
*   **Description**: The average score of all cadets in mock exams, used to identify schools needing customer success intervention.
*   **Validation**: Float, range `0.0` to `100.0`.

### 3. Sponsoring Shipping Lines
*   **API Name**: `sponsoring_shipping_lines`
*   **Field Type**: `enumeration` (Multi-select Checkbox)
*   **Description**: Sponsoring companies who hire cadets from this academy.
*   **Options**:
    *   `SYNERGY` (Synergy Marine Group)
    *   `FLEET` (Fleet Management Ltd)
    *   `MAERSK` (Maersk Line)
    *   `ANGLO_EASTERN` (Anglo-Eastern Group)
    *   `CHEVRON` (Chevron Shipping)

### 4. Proctoring Compliance Approved
*   **API Name**: `proctoring_compliance_approved`
*   **Field Type**: `boolean` (Checkbox)
*   **Description**: Indicates whether the college's local computer room meets webcam anti-cheating guidelines.

### 5. Onboarding Kickoff Date
*   **API Name**: `onboarding_kickoff_date`
*   **Field Type**: `date`
*   **Description**: The calendar day the CSM conducted the initial system walkthrough.
*   **Validation**: YYYY-MM-DD.
