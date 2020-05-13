#!/usr/bin/node
const requests = require('request');

requests(process.argv[2], function writestatus (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
