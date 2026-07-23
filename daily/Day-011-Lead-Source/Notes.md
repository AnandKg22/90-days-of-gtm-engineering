# Study Notes - Day 011: Lead Source & Marketing Attribution

Today's studies focused on acquisition channels, UTM campaign tracking parameters, conversion source capture, and mathematical touchpoint attribution models.

---

## 1. Acquisition Channels

A business acquires leads through several distinct channels:

*   **Organic**: Visitors finding the website via unpaid search engine results (Google search).
*   **Paid**: Visitors clicking on advertisements (Google Ads, LinkedIn Ads).
*   **Referral**: Visitors arriving from external links on other sites (e.g. click links on a maritime blog).
*   **Outbound**: Leads identified by sales outreach (cold emails, phone calls).
*   **Direct**: Visitors typing the URL directly into their browser address bar.

---

## 2. Deep-Dive: Lead Source Subtopics

To measure marketing return on investment (ROI), a GTM Engineer must master these three subtopics:

### 1. UTM Campaign Tracking
*   **Definition**: Urchin Tracking Module (UTM) codes are standardized query parameters appended to URLs to track traffic sources:
    *   `utm_source`: The platform driving traffic (e.g., `google`, `newsletter`).
    *   `utm_medium`: The channel type (e.g., `cpc`, `email`, `social`).
    *   `utm_campaign`: The specific promotion (e.g., `summer_discount`).
    *   `utm_term`: Target keywords used in paid search.
    *   `utm_content`: Specific link variants (used for A/B testing).
*   **GTM Application**: You configure website scripts to check for these parameters in the URL query string and save them in browser cookies or local storage.

### 2. Conversion Source Capture
*   **Definition**: Writing logic to extract the lead source when a visitor signs up.
*   **GTM Application**: When a lead form is submitted, the front-end code reads the stored UTM parameters from cookies and attaches them to the form webhook payload:
    *   `utm_source` ──> HubSpot field `hs_analytics_first_touch_converting_source`.
    *   `referrer_header` (if UTMs are missing) ──> Categorized as Organic, Referral, or Direct.

### 3. Attribution Models (First-Touch vs. Last-Touch)
*   **Definition**: Algorithms that distribute revenue credit among the touchpoints a user interacted with before buying.
*   **GTM Application**:
    *   **First-Touch**: Assigns 100% of the revenue credit to the very first channel that brought the user to the site (measures awareness).
    *   **Last-Touch**: Assigns 100% of the credit to the final touchpoint that occurred before the purchase (measures conversion triggers).
    *   **Linear (Multi-Touch)**: Splits the revenue credit equally across all touchpoints in the journey.
