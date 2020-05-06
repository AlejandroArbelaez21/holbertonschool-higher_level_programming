#!/usr/bin/node
exports.addMeMaybe = addMeMaybe;

function addMeMaybe (number, theFunction) {
  return theFunction(number + 1);
}
