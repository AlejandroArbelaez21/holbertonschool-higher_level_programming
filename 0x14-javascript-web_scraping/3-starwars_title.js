#!/usr/bin/node
const requests = require('request');

requests(`http://swapi.co/api/films/${process.argv[2]}`, function writestatus (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
