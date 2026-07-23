# Exercises - Day 011: UTM Builder Specification

This document details the functional specifications and generation models for the UTM Campaign URL Builder.

---

## 🛠️ UTM Builder Input Sanitization Rules

To prevent broken links or reporting errors in CRM dashboards, a GTM UTM builder applies these formatting steps:

1.  **Force Lowercase**: Converts all parameter inputs to lowercase (`Google` ──> `google`).
2.  **Replace Spaces**: Converts spaces to underscores or URL encoding `%20` (`july newsletter` ──> `july_newsletter`).
3.  **Strip Query Symbols**: Removes duplicate `?` or `&` characters from input blocks.

---

## 📋 Campaign URL Reference Mappings

Below are target URL configurations for VivaExams promo campaigns:

### 1. Paid Search (Google Ads CPC)
*   *Base URL*: `https://vivaexams.com`
*   *Parameters*: Source: `google`, Medium: `cpc`, Campaign: `maritime_exam_prep`
*   *Output URL*:
    ```
    https://vivaexams.com/?utm_source=google&utm_medium=cpc&utm_campaign=maritime_exam_prep
    ```

### 2. Email Newsletter Campaign
*   *Base URL*: `https://vivaexams.com/pricing`
*   *Parameters*: Source: `newsletter`, Medium: `email`, Campaign: `july_institutions`
*   *Output URL*:
    ```
    https://vivaexams.com/pricing?utm_source=newsletter&utm_medium=email&utm_campaign=july_institutions
    ```

### 3. Outbound Sales Sequences
*   *Base URL*: `https://vivaexams.com/demo`
*   *Parameters*: Source: `sales_outbound`, Medium: `cold_email`, Campaign: `goa_academies`
*   *Output URL*:
    ```
    https://vivaexams.com/demo?utm_source=sales_outbound&utm_medium=cold_email&utm_campaign=goa_academies
    ```
