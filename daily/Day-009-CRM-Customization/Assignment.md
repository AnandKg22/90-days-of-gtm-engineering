# Project Assignment - Day 009: Webhook Integration Engine

This project requires developing a Python integration handler that maps incoming checkout webhooks to custom CRM properties and posts the payload to a simulated API endpoint.

---

## 🎯 Requirements

Your Python integration handler must:
1.  Consume a mock billing webhook payload (e.g. from Stripe checkout) containing:
    *   `customer_email`
    *   `quantity` (number of seats)
    *   `sponsors` (comma-separated string)
    *   `compliance_verified` (boolean)
2.  Apply a schema data mapper to translate source properties to CRM API property tags:
    *   `customer_email` ──> `email`
    *   `quantity` ──> `cadet_seats_purchased`
    *   `sponsors` ──> `sponsoring_shipping_lines` (convert to string list)
    *   `compliance_verified` ──> `proctoring_compliance_approved`
3.  Simulate posting this payload via HTTP to the HubSpot Contacts API, printing the validated payload and the mock response logs.

---

## 💻 Deliverable Code

A complete, working integration script has been created and placed in [Code/webhook_sync.py](Code/webhook_sync.py). It models the checkout webhooks, runs the property mappings, and outputs the simulated sync logs.
