# Study Notes - Day 008: CRM Fundamentals

Today's studies focused on Customer Relationship Management (CRM) databases, object properties, relationship cardinalities, and automation workflows.

---

## 1. Core CRM Objects

A CRM database is structured around standard tables representing commercial entities:

*   **Contacts**: Individual people with contact details (email, job title).
*   **Companies**: Organization details (domain, industry, size).
*   **Deals / Opportunities**: Financial values, pipeline stages, and close dates.
*   **Activities**: Interaction logs (emails, calls, meetings, notes).
*   **Pipelines**: The stages through which deals flow.

---

## 2. Deep-Dive: CRM Subtopics

To model commercial systems, a GTM Engineer must master these four CRM subtopics:

### 1. Object Relationships (Associations)
*   **Definition**: The logical links connecting database entities.
    *   *Company-to-Contacts (1:N)*: One company can have many employee contacts.
    *   *Contact-to-Deals (N:M)*: A deal can involve multiple contacts (decision-makers), and a single contact can be associated with multiple deals.
*   **GTM Application**: You must implement **association tables** in your database to link deals to contacts and companies without duplicating records.

### 2. Properties (Fields)
*   **Definition**: The individual metadata attributes stored on an object (e.g., Contact properties: `email`, `phone`, `job_title`).
*   **GTM Application**: Properties are typed (String, Number, Date, Boolean, Dropdown/Enumeration). A GTM Engineer ensures strict type validation. If a Salesforce field expects a number, the n8n sync must not send a string.

### 3. Objects (Standard vs. Custom)
*   **Definition**:
    *   *Standard Objects*: Out-of-the-box CRM tables (Contacts, Companies, Deals, Tickets).
    *   *Custom Objects*: User-defined tables built to model niche business data (e.g. creating a `Cadet_Batch__c` object for VivaExams).
*   **GTM Application**: Managing custom objects requires calling specific API metadata endpoints to fetch schemas.

### 4. CRM Automation (Workflows)
*   **Definition**: Programmatic triggers inside the CRM that execute actions when data changes (e.g., when a Contact changes status, trigger a webhook).
*   **GTM Application**: To avoid overloading CRM performance limits, the GTM Engineer builds complex automation rules externally using tools like n8n or serverless functions, leaving the CRM as a simple data triggers source.
