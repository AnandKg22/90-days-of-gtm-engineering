# Exercises - Day 047: Pricing & ROI Calculations

This document details practical exercises on writing pricing engines, executing ROI savings calculations, and setting up discount compliance checks.

---

## 📋 Exercise 1: Implementing ROI Math in Python

### Goal:
Write a Python function that takes a prospect's operational parameters and the software cost to return a structured financial evaluation dictionary.

### Script Implementation:
```python
def calculate_deal_financials(
    monthly_wasted_hours: float,
    average_hourly_labor: float,
    software_annual_cost: float
) -> dict:
    # 1. Cost of pain
    annual_loss = (monthly_wasted_hours * average_hourly_labor) * 12
    
    # 2. Net savings
    net_savings = annual_loss - software_annual_cost
    
    # 3. ROI %
    roi_percent = (net_savings / software_annual_cost) * 100 if software_annual_cost > 0 else 0
    
    return {
        "annual_loss": annual_loss,
        "net_savings": net_savings,
        "roi_percent": roi_percent
    }

# Example validation check:
res = calculate_deal_financials(120, 80.0, 99000.0)
print(f"Annual Loss: ${res['annual_loss']:,}")   # Expected: $115,200
print(f"ROI: {res['roi_percent']:.1f}%")          # Expected: 16.4%
```

---

## ⚙️ Exercise 2: Mapping a Phased Scope of Work (SOW)

Draft the SOW text block for a target client integration utilizing **AWS**, **Salesforce**, and **Oracle Financials**:

### Phased SOW Output:
*   **Phase 1: API Configuration**
    *   Setup AWS endpoint connectors. Configure Salesforce routing rules and authentication headers.
*   **Phase 2: Database Schema Alignment**
    *   Map Salesforce contact fields to Oracle billing objects. Setup usage credit reconciliation rules.
*   **Phase 3: Integration Dry-Run**
    *   Deploy parallel syncing processes. Validate data parity across AWS logs, Salesforce contacts, and Oracle databases for 14 days before going live.