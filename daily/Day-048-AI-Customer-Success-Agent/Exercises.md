# Exercises - Day 048: Health Scoring & Onboarding

This document details practical exercises on writing customer health scoring logic and mapping onboarding stages.

---

## 📋 Exercise 1: Calculating CHS & Rating Tiers

### Goal:
Write a Python function that takes a customer's usage metrics and outputs their health score and tier rating.

### Script Implementation:
```python
def get_customer_health_status(
    adoption_rate: float, # 0.0 to 1.0
    onboarding_completed: bool,
    open_tickets_count: int
) -> dict:
    # 1. Product Adoption (60%)
    adoption_points = adoption_rate * 60.0
    
    # 2. Onboarding Status (15%)
    onboarding_points = 15.0 if onboarding_completed else 0.0
    
    # 3. Support Tickets (25%, deducts 5 points per ticket)
    ticket_points = max(0.0, 25.0 - (open_tickets_count * 5.0))
    
    total_score = adoption_points + onboarding_points + ticket_points
    
    if total_score >= 80:
        rating = "GREEN (Healthy / Expansion target)"
    elif total_score >= 50:
        rating = "YELLOW (Stable / Watch list)"
    else:
        rating = "RED (At-Risk / Escalation target)"
        
    return {
        "score": total_score,
        "rating": rating
    }

# Test run matching Wayne Enterprises scenario (42% usage, 5 tickets, onboarding complete):
res = get_customer_health_status(0.42, True, 5)
print(f"Score: {res['score']:.1f} | Tier: {res['rating']}")
# Expected: Score: 40.2 | Tier: RED
```

---

## ⚙️ Exercise 2: Mapping Onboarding Milestones

Define a tracking dictionary template that evaluates onboarding progress for a newly closed contract:

```python
onboarding_milestones = {
    "milestone_1_kickoff": {
        "completed": True,
        "date": "2026-07-01",
        "weight": 25
    },
    "milestone_2_api_configured": {
        "completed": True,
        "date": "2026-07-05",
        "weight": 25
    },
    "milestone_3_schema_mapped": {
        "completed": False,
        "date": None,
        "weight": 25
    },
    "milestone_4_team_trained": {
        "completed": False,
        "date": None,
        "weight": 25
    }
}

# Calculate onboarding progress:
completed_weight = sum(m["weight"] for m in onboarding_milestones.values() if m["completed"])
print(f"Onboarding Setup Progress: {completed_weight}%") # Output: 50%
```