#!/usr/bin/node
function add (a, b) {
  return parseInt(a) + parseInt(b);
}

const number1 = process.argv[2];
const number2 = process.argv[3];
console.log(add(number1, number2));
