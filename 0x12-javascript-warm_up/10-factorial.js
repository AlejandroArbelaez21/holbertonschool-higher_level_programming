#!/usr/bin/node
function factorialize (num) {
  if (num < 0) {
    return -1;
  } else if (num === 0) {
    return 1;
  } else if (num === undefined) {
    return 1;
  } else {
    return (num * factorialize(num - 1));
  }
}

const fact = process.argv[2];
console.log(factorialize(fact));
