const express = require('express');
const app = express();

// Performance issue: fetch inside a loop (creates sequential blockages)
async function logEventLogs(events) {
  for (const event of events) {
    await fetch('https://api.example.com/log', {
      method: 'POST',
      body: JSON.stringify(event)
    });
  }
}

app.post('/events', async (req, res) => {
  await logEventLogs(req.body.events);
  res.send('Done');
});

app.listen(3000);
