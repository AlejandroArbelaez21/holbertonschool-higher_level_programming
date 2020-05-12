#!/usr/bin/node
const Map = require('./100-data');
const newList = [];
for (let index = 0; index < Map.list.length; index++) {
  const map1 = Map.list.map((x, index) => x * index);
  newList[index] = map1[index];
}
console.log(Map.list);
console.log(newList);
