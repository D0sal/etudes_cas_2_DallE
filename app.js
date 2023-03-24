const express = require('express');
const tf = require('@tensorflow/tfjs-core');
const app = express();

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

app.get('/single/:textInput', async (req, res) => {
  const textInput = req.params.textInput;

  // Loading model
  /*
  const model = await tf.loadLayersModel('file://path/to/my-model/model.json');
  const output = model.predict(input);

  res.send(output) <-- à convertir en format JSON
  */
 
  res.send({inputText: textInput})
});

app.get('/multiple/:textInput', async (req, res) => {
  const textInput = req.params.textInput;

  // Loading model
  /*
  const model = await tf.loadLayersModel('file://path/to/my-model/model.json');
  const output = model.predict(input);

  res.send(output) <-- à convertir en format JSON
  */
 
  res.send({inputText: textInput})
});

app.listen(3000, () => {
  console.log('App listening on port 3000!');
});