# Study Notes - Day 018: Customer Data Platforms (CDP) & Segment

Today's studies focused on Customer Data Platforms (CDPs), identity resolution graphs, Segment spec API calls (Page, Identify, Track, Group), and event validation tracking plans.

---

## 1. Customer Data Platforms (CDP) & Segment

In a modern B2B SaaS stack, tracking user events is fragmented. Without a CDP, you have to write separate JavaScript SDKs for Google Analytics, HubSpot, Amplitude, and Mixpanel, which slows down the website.

A CDP (like Segment or RudderStack) acts as a single, central event hub. You install a single Segment SDK. The SDK pushes events to the Segment API, and Segment multiplexes (routes) that single event payload to all downstream destinations (analytics, CRMs, warehouses) in real time.

---

## 2. Deep-Dive: CDP Subtopics

To implement a customer event tracking pipeline, a GTM Engineer must master these three CDP subtopics:

### 1. Identity Resolution (Identity Graph Database Design)
*   **Definition**: Linking a user's anonymous web behavior (before they log in) to their identified user profile (after they sign up).
*   **GTM Application**: When a visitor lands, Segment assigns a random `anonymous_id` (cookie). When they register, your code calls `identify` passing both `anonymous_id` and their database `user_id`. Segment links these keys in an **identity graph**, merging all pre-signup ad-clicks to their CRM contact record.

### 2. Segment API Call Standards
*   **Definition**: Implementing the four primary event methods defined by the Segment Spec:
    *   **Page**: Records page views, capture URLs and referrers.
    *   **Identify**: Logs a user's profile metadata traits (e.g. `email`, `role`, `company`).
    *   **Track**: Logs specific actions a user performs (e.g., `Exam Started`, `Payment Cleared`).
    *   **Group**: Associates an identified user with an organization or company profile (essential for B2B CRM account mappings).

### 3. Event Schema Configuration (Tracking Plans)
*   **Definition**: A central schema blueprint specifying exactly which event names are allowed, which properties are required, and their validation types.
*   **GTM Application**: To prevent front-end developers from sending corrupted data (e.g. naming an event `signed_up` on one page and `UserSignedUp` on another), you write a JSON tracking plan. Segment validates incoming events against this plan, discarding non-compliant events to keep the warehouse clean.
