# GTM APIs, Integrations & Webhook Receivers

Integrating commercial platforms requires a mastery of REST standards, OAuth protocols, Composite CRM requests, and secure Webhook servers.

---

## 1. REST API Standards & OAuth Flow

GTM platforms use REST endpoints secured via OAuth 2.0. The standard flow for accessing a CRM API on behalf of a user:

```
User ──> App (Requests Integration) ──> Redirects to CRM Login
User ──> Approves Permissions ──> CRM redirects to App callback with ?code=xyz
App ──> POST /oauth/token { code } ──> CRM returns { access_token, refresh_token }
App ──> GET /contacts (Header: Authorization Bearer access_token)
```

---

## 2. Composite and Bulk APIs

When working with Salesforce or HubSpot at scale:
*   **Composite APIs**: Group multiple operations into a single HTTP request payload (reduces network roundtrips and API call limits usage).
*   **Bulk APIs**: Process large datasets asynchronously (useful for migrations or daily data warehouses sync).

---

## 3. Webhooks & Verification

Webhooks notify our app instantly when data changes in HubSpot/Salesforce. 

> [!CAUTION]
> Always verify webhook signatures to prevent unauthorized users from spoofing events and polluting your database.

### Signature Verification Workflow (HubSpot Example)

HubSpot signs requests using a Client Secret. The signature is in the `X-HubSpot-Signature` header.
*   **Algorithm**: HMAC-SHA256
*   **Hash Input**: `Client_Secret + HTTP_Method + Request_URI + Request_Body`

### Express.js Webhook Receiver implementation

```javascript
const express = require('express');
const crypto = require('crypto');
const app = express();

const HUBSPOT_CLIENT_SECRET = process.env.HUBSPOT_CLIENT_SECRET;

// Middleware to capture raw body for signature verification
app.use(express.json({
  verify: (req, res, buf) => { req.rawBody = buf.toString(); }
}));

app.post('/webhooks/hubspot', (req, res) => {
  const signature = req.headers['x-hubspot-signature'];
  const requestUri = 'https://' + req.headers.host + req.originalUrl;
  const requestBody = req.rawBody || '';
  const httpMethod = req.method;

  // Build the source string
  const source = HUBSPOT_CLIENT_SECRET + httpMethod + requestUri + requestBody;
  
  // Calculate HMAC-SHA256 hash
  const hash = crypto.createHmac('sha256', HUBSPOT_CLIENT_SECRET)
                     .update(source)
                     .digest('hex');

  // Perform constant-time comparison to prevent timing attacks
  try {
    const signatureBuffer = Buffer.from(signature, 'hex');
    const hashBuffer = Buffer.from(hash, 'hex');
    if (crypto.timingSafeEqual(signatureBuffer, hashBuffer)) {
      console.log('Webhook verified!');
      // Process payload asynchronously to return 200 immediately
      processWebhookPayload(req.body);
      return res.status(200).send('OK');
    }
  } catch (err) {
    console.error('Signature verification failed');
  }

  return res.status(401).send('Unauthorized');
});

function processWebhookPayload(payload) {
  // Enqueue to Redis/RabbitMQ queue
  console.log('Received events:', payload);
}

app.listen(3000, () => console.log('Listening...'));
```

### Python Webhook Signature Verification

```python
import hmac
import hashlib

def verify_hubspot_signature(client_secret, method, uri, body, signature):
    source = f"{client_secret}{method}{uri}{body}"
    calculated_signature = hmac.new(
        key=client_secret.encode('utf-8'),
        msg=source.encode('utf-8'),
        digestmod=hashlib.sha256
    ).hexdigest()
    
    return hmac.compare_digest(calculated_signature, signature)
```
