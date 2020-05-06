#!/usr/bin/node
const number = parseInt(process.argv[2]);
if (number === undefined) {
  console.log('Missing size');
}
for (let index = 0; index < number; index++) {
  console.log('X'.repeat(number));
}
