const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

app.get('/single/:textInput', async (req, res) => {
  const textInput = req.params.textInput;
 
  res.send({inputText: textInput})
});

app.get('/multiple/:textInput', async (req, res) => {
  const textInput = req.params.textInput;
 
  res.send({inputText: textInput})
});

app.listen(3000, () => {
  console.log('App listening on port 3000!');
});