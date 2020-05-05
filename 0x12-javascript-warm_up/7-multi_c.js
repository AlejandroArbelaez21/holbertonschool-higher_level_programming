#!/usr/bin/node
const number = process.argv[2];
if (number === undefined) {
  console.log('Missing number of occurrences');
}
for (let index = 0; index < number; index++) {
  console.log('C is fun');
}
