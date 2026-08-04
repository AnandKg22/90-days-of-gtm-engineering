# Exercises - Day 018: GTM Event Tracking Plan

This document details the event tracking plan designed to standardize and validate telemetry data captured across the VivaExams application.

---

## 📋 VivaExams Segment Tracking Plan

This matrix defines the required schema structures and property type validation rules for core GTM events:

| Event Name | Trigger Condition | Required Properties | Property Data Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| **`Identify`** | User registers or logs in. | `email`<br>`name`<br>`role` | `string`<br>`string`<br>`string` | Logs user traits and binds `anonymous_id` to database `user_id`. |
| **`Group`** | User links to a college. | `company_name`<br>`employees` | `string`<br>`integer` | Associates the contact with a B2B HubSpot Company record. |
| **`Exam Completed`** | Cadet finishes a mock exam. | `exam_id`<br>`score`<br>`pass_status` | `string`<br>`number` (float)<br>`boolean` | Captures cadet performance to sync to the CRM health dashboard. |
| **`Subscription Upgraded`** | Admin upgrades package. | `plan_tier`<br>`seats_added`<br>`amount` | `string`<br>`integer`<br>`number` (float) | Triggers automated sales pipeline expansion deals. |

---

## ⚙️ JSON Schema Event Validation Example
Below is the JSON validation contract for the `Exam Completed` event:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Exam Completed",
  "type": "object",
  "properties": {
    "exam_id": { "type": "string" },
    "score": { "type": "number", "minimum": 0, "maximum": 100 },
    "pass_status": { "type": "boolean" }
  },
  "required": ["exam_id", "score", "pass_status"]
}
```
