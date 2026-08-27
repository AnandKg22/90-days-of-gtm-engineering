# Cheatsheet - GTM Automation & APIs
- **HTTP Methods**: GET (read), POST (create), PUT (replace), PATCH (update), DELETE (remove)
- **HubSpot Contact Creation Curl**:
  ```bash
  curl -X POST https://api.hubapi.com/crm/v3/objects/contacts \
    -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{ "properties": { "email": "lead@domain.com", "firstname": "John", "lastname": "Doe" } }'
  ```
- **Webhook Express Server skeleton**:
  ```javascript
  const express = require('express');
  const app = express();
  app.post('/webhook', (req, res) => {
    console.log(req.body);
    res.sendStatus(200);
  });
  app.listen(3000);
  ```
