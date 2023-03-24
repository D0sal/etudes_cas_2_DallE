const express = require('express');

const app = express();

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

app.get('/:textInput', (req, res) => {
  const textInput = req.params.textInput;
  // ici load les images avec tensorflow.js
  

  res.send({image: textInput})
});

app.listen(3000, () => {
  console.log('App listening on port 3000!');
});