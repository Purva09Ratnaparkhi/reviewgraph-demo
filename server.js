const express = require('express');
const app = express();

app.get('/status', (req, res) => {
  res.send('Server is active.');
});

app.listen(3000);
