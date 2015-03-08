var path = require('path');
var express = require('express')
var PythonShell = require('python-shell');
var app = express()
app.use(express.static(__dirname + '/View'));
app.use(express.static(__dirname + '/Script'));
var pyshell = new PythonShell('giffy.py');

app.get('/', function (req, res) {
  res.sendFile('index.html');
})
 
app.get('/trend', function (req, res) {
  // sends a message to the Python script via stdin 
  //pyshell.send('trend');
  //pyshell.on('message', function (message) {
  //  console.log(message);
  res.send('GET request');
  console.log("trend");
  //});
})

pyshell.end(function (err){});

var server = app.listen(3000, function () {
  var host = server.address().address
  var port = server.address().port

  console.log('Example app listening at http://%s:%s', host, port)

})
