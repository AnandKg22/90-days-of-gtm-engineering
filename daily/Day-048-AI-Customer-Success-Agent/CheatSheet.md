# Cheat Sheet - AI Customer Success

This cheat sheet compiles health scoring structures, retention formulas, and Slack alert templates.

---

## 1. Key Terminology

*   **CHS (Customer Health Score)**: A metric indicating customer satisfaction and renewal likelihood.
*   **NRR (Net Revenue Retention)**: The percentage of recurring revenue retained from existing customers, including expansion.
*   **GRR (Gross Revenue Retention)**: The percentage of recurring revenue retained from existing customers, excluding expansion.
*   **Churn**: The percentage of customers (or revenue) lost over a period.
*   **Onboarding Milestones**: Setup phases (kick-off, integration, training, launch) that indicate progress toward product adoption.

---

## 2. Customer Health Score (CHS) Calculation Template

```python
def calculate_chs(adoption: float, onboarding: bool, open_tickets: int) -> float:
    # 1. Product Adoption (0.0 to 1.0) -> Max 60 points
    adoption_score = adoption * 60.0
    
    # 2. Onboarding Status -> Max 15 points
    onboarding_score = 15.0 if onboarding else 0.0
    
    # 3. Support Tickets Penalty -> Max 25 points, minus 5 per ticket
    ticket_score = max(0.0, 25.0 - (open_tickets * 5.0))
    
    return adoption_score + onboarding_score + ticket_score
```

---

## 3. Slack Webhook Notification Payload

When an account health falls below 50.0, post this JSON payload to the CSM Slack channel:
```json
{
  "text": "🚨 *CRITICAL CHURN RISK DETECTED*",
  "attachments": [
    {
      "color": "#FF0000",
      "fields": [
        {"title": "Company", "value": "Wayne Enterprises", "short": true},
        {"title": "Health Score", "value": "40.2 / 100.0", "short": true},
        {"title": "Assigned CSM", "value": "Alfred Pennyworth", "short": true},
        {"title": "Open Support Tickets", "value": "5 tickets", "short": true},
        {"title": "Days to Renewal", "value": "24 days", "short": false}
      ]
    }
  ]
}
```
---

## 4. Retention Formulas

$$\text{Logo Churn Rate} = \frac{\text{Lost Customers during period}}{\text{Starting Customers at start of period}} \times 100\%$$

$$\text{Net Revenue Retention (NRR)} = \frac{\text{ARR}_\text{Start} + \text{Expansion} - \text{Downgrades} - \text{Churn}}{\text{ARR}_\text{Start}} \times 100\%$$
