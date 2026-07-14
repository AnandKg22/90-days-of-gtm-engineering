# Exercises - Day 002: SaaS Metrics Calculator

This document contains instructions for calculating SaaS metrics using Excel and a corresponding Python program to compute them from raw transaction inputs.

---

## 📊 Excel Spreadsheet Setup

To calculate SaaS metrics for a company, set up a spreadsheet with the following columns:

### 1. Raw Customer Data Sheet (`Customers`)
*   **Column A**: `Customer ID`
*   **Column B**: `Company Name`
*   **Column C**: `Monthly Subscription Fee ($)`
*   **Column D**: `Status` (`Active` or `Churned`)
*   **Column E**: `Acquisition Cost ($)`

### 2. Metrics Summary Sheet Formulas
Configure cell calculations as follows:

*   **Total Active Customers**:
    ```excel
    =COUNTIF(Customers!D:D, "Active")
    ```
*   **MRR (Monthly Recurring Revenue)**:
    ```excel
    =SUMIF(Customers!D:D, "Active", Customers!C:C)
    ```
*   **ARR (Annual Recurring Revenue)**:
    ```excel
    =B2 * 12  (where B2 is the MRR cell)
    ```
*   **Average Revenue Per Account (ARPU)**:
    ```excel
    =AVERAGEIF(Customers!D:D, "Active", Customers!C:C)
    ```
*   **Total CAC Spent**:
    ```excel
    =SUM(Customers!E:E)
    ```
*   **Average CAC**:
    ```excel
    =AVERAGE(Customers!E:E)
    ```
*   **Churn Rate %**:
    ```excel
    =COUNTIF(Customers!D:D, "Churned") / COUNTA(Customers!A:A)
    ```
*   **Lifetime Value (LTV)**:
    ```excel
    =ARPU / Churn_Rate_Cell
    ```

---

## 💻 Python Metrics Engine

Instead of manual spreadsheet entry, we can automate this math. A python calculator script has been added to [Code/metrics_calculator.py](Code/metrics_calculator.py).

### How to Run:
1. Open terminal and run:
   ```bash
   python "D:\\Books\\90Days-GTM-Engineer\\90-days-of-gtm-engineering\\daily\\Day-002-Understanding-Modern-SaaS\\Code\\metrics_calculator.py"
   ```
2. The script outputs a detailed JSON report of SaaS metrics.