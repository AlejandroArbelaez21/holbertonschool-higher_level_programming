#!/usr/bin/node
const number = parseInt(process.argv[2]);
if (isNaN(number)) {
  console.log(0);
} else if (process.argv.length < 4) {
  console.log(0);
} else {
  const list = [];
  for (let index = 2; index < process.argv.length; index++) {
    list.push(process.argv[index]);
  }
  list.sort();
  console.log(list[list.length - 2]);
}
