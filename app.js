const express = require('express');
const app = express();
const { spawn } = require('child_process');

const runPythonScript = (res, inputText, isMultiple) => {
  const pythonProcess = spawn('python3', ['cas_etude2.py', inputText, isMultiple]);

  pythonProcess.stdout.on('data', (data) => {
    console.log('data returned', data.toString())
    res.send(
      JSON.stringify(`{${data.toString()}}`)
      )
  });
  
  pythonProcess.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
    throw new Error('problem while running python script')
  });
  
  pythonProcess.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
  });
}

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

app.get('/single/:textInput', async (req, res) => {
  const textInput = req.params.textInput;

  runPythonScript(res, textInput, false);
});

app.get('/multiple/:textInput', async (req, res) => {
  const textInput = req.params.textInput;
  
  runPythonScript(res, textInput, true);
});

app.listen(3000, () => {
  console.log('App listening on port 3000!');
});