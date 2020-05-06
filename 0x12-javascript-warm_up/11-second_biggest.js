#!/usr/bin/node
const number = process.argv[2];
if (isNaN(number)) {
  console.log(0);
} else if (process.argv.length < 4) {
  console.log(0);
} else {
  const list = [];
  for (let index = 2; index < process.argv.length; index++) {
    list.push(parseInt(process.argv[index]));
  }
  list.sort(function (a, b) {
    return a - b;
  });
  console.log(list[list.length - 2]);
}
