const express = require('express')
const bodyParser = require('body-parser');
const base64Img = require('base64-img');
const PyFi = require('pyfi');
const { spawn } = require('child_process');

const app = express()

app.use(express.static('public'))
app.use(bodyParser.urlencoded({ extended: false }));

app.post('/type', (req, res) => {
  // Only going to parse one image at a time for now -- so there are no keys for images.
  // If we are to scale this thing up in the future thats going to need to change.
  const image = req.body.image;
  base64Img.imgSync(req.body.image, 'data/', 'sketch');

  const py = spawn('python', ['/Users/mcgingras/IDEO/Summer18/Build/Boston/chairs/python/analysis/classify.py']);
  py.stdout.on('data', (data) => { console.log(`The type of classification is: ${data}!`);});
  py.stderr.on('data', (data) => { console.log(`stderr: ${data}`); });
  py.on('close', (code) => { console.log(`child process exited with code ${code}`); });
  
  res.status(200).send();
})


app.listen(3000, () => {
  console.log('listening on port 3000!');
});
