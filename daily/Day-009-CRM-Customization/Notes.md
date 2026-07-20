# Study Notes - Day 009: CRM Customization

Today's studies focused on custom properties (text, numbers, dropdowns, dates), data mapping between systems, and webhooks for real-time CRM updates.

---

## 1. Custom Properties in CRMs

Out-of-the-box standard properties (like name or email) are not enough to store specialized business data. GTM Engineers configure custom fields:

*   **Dropdown / Enum**: Restricts inputs to predefined options (e.g., Shipping Line: `Synergy`, `Maersk`, `Fleet`). Essential for clean routing.
*   **Number**: Stores integers or decimals (e.g., `cadet_seats_purchased`, `exam_pass_rate_percent`). Used for calculations.
*   **Date**: Logs specific milestones (e.g., `onboarding_kickoff_date`). Used to measure SLAs.
*   **Boolean (Checkbox)**: Binary state (e.g., `proctoring_compliance_approved`). Triggers secondary workflows.

---

## 2. Deep-Dive: CRM Customization Subtopics

To customize CRM environments, a GTM Engineer must master these three subtopics:

### 1. API Custom Field Schema Integration
*   **Definition**: CRM APIs represent custom fields with unique internal names (e.g., HubSpot prefix `hs_` or custom properties like `cadet_seats_purchased`; Salesforce uses suffixes like `Cadet_Seats__c`).
*   **GTM Application**: When querying or updating records via REST/GraphQL APIs, the code must reference these exact system identifiers, not the user-facing label.

### 2. Data Mapping (Transformation)
*   **Definition**: The translation layer mapping database fields or third-party webhooks to the corresponding CRM custom properties.
*   **GTM Application**: You must write a translation dictionary in your synchronization code:
    ```python
    # Map external Stripe payload values to CRM Custom API fields
    mapping = {
        "stripe_seats": "cadet_seats_purchased",
        "stripe_customer_email": "email",
        "stripe_plan_name": "vivaexams_plan_tier"
    }
    ```

### 3. Schema Configuration (Metadata Management)
*   **Definition**: Defining CRM custom properties programmatically using JSON configurations rather than manual clicks in the admin UI.
*   **GTM Application**: The GTM Engineer writes schema scripts that call HubSpot/Salesforce metadata endpoints to create properties automatically, ensuring environment consistency between staging and production CRMs.
