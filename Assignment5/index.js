const express = require('express')
const app = express()
const server = require('http').createServer(app);
const WebSocket = require('ws');

app.use(express.static('public'));

const IP = "192.168.1.3";

const wss = new WebSocket.Server({ server:server });

wss.on('connection', function connection(ws) {
  console.log('A new client Connected!');
  ws.send('Welcome New Client!');

  ws.on('message', function incoming(message) {
    console.log('received: %s', message);
    var color = String(message);
    wss.clients.forEach(function each(client) {
      if (client !== ws && client.readyState === WebSocket.OPEN) {
        client.send(color);
      }
    });
    
  });
});

app.get('/', (req, res) => res.send('Hello World!'))

server.listen(3000, IP, () => console.log(`Listening on port :3000`))