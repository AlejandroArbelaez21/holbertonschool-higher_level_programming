#!/usr/bin/node
const requests = require('request');

requests(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    let cont = 0;
    const title = JSON.parse(body);
    const val = Object.values(title.results);
    for (const value of val) {
      if (value.characters.includes('https://swapi.co/api/people/18/')) { cont++; }
    }
    console.log(cont);
    return cont
  }
});
