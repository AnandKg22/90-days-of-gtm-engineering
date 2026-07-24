# Cheatsheet - GTM Foundations
- **ARR Formula**: MRR * 12
- **LTV Formula**: (ARPU * Gross Margin) / Churn Rate
- **CAC Payback Period**: CAC / (ARPU * Gross Margin %)
- **NRR Formula**: (Starting MRR - Churn - Contractions + Expansion) / Starting MRR * 100
- **CRM Standard Objects**: Contacts, Companies, Deals, Activities
- **HubSpot Search API Curl**:
  ```bash
  curl -X POST https://api.hubapi.com/crm/v3/objects/contacts/search \
    -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{ "filterGroups": [{ "filters": [{ "propertyName": "email", "operator": "EQ", "value": "test@domain.com" }] }] }'
  ```
