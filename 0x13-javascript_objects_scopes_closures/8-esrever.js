#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  let reverse = list.length - 1;
  for (let index = 0; index < list.length; index++) {
    newList[index] = list[reverse];
    reverse--;
  }
  return newList;
};
