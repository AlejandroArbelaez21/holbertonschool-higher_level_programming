#!/usr/bin/node
const Map = require('./100-data');

const map1 = Map.list.map((x, index) => x * index);

console.log(Map.list);
console.log(map1);
