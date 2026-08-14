// Node.js Webhook Express Server
const express = require('express');
const crypto = require('crypto');
const app = express();

const WEBHOOK_SECRET = process.env.WEBHOOK_SECRET || "mock_secret";

app.use(express.json());

app.post('/webhook/intake', (req, res) => {
    const signature = req.headers['x-signature'];
    
    if (!signature) {
        return res.status(401).send("Missing signature header");
    }
    
    // Hash validation
    const hmac = crypto.createHmac('sha256', WEBHOOK_SECRET);
    hmac.update(JSON.stringify(req.body));
    const expectedSignature = hmac.digest('hex');
    
    if (signature !== expectedSignature) {
        console.log("[SECURITY ALERT] Invalid signature received");
        return res.status(403).send("Forbidden: Invalid signature");
    }
    
    console.log("[WORKFLOW] Event received and verified:", req.body.event);
    res.status(200).send("Verified & Enqueued");
});

app.listen(8080, () => console.log('Intake Gateway running on port 8080'));
