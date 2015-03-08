var path = require('path');
var exec = require('child_process').exec
var express = require('express')
var app = express()
app.use(express.static(__dirname + '/View'));
app.use(express.static(__dirname + '/Script'));

app.get('/', function (req, res) {
  res.sendFile('index.html');
})
 
app.get('/trend', function (req, res) {

  exec("python Script/giffy.py trending", function (error, stdout, stderr) {
    res.send(stdout);
    if (error !== null) {
      console.log('exec error: ' + error);
    }});
  
})

app.get('/translate', function (req, res) {

  exec("python Script/giffy.py translate "+req.query.q, function (error, stdout, stderr) {
    res.send(stdout);
    if (error !== null) {
      console.log('exec error: ' + error);
    }});
  
})

app.get('/random', function (req, res) {

  exec("python Script/giffy.py random "+req.query.q, function (error, stdout, stderr) {
    res.send(stdout);
    if (error !== null) {
      console.log('exec error: ' + error);
    }});
  
})

var server = app.listen(4000, function () {
  var host = server.address().address
  var port = server.address().port

  console.log('Example app listening at http://%s:%s', host, port)

})
