#!/usr/bin/node
exports.callMeMoby = callMeMoby;
function callMeMoby (x, theFunction) {
    for (let index = 0; index < x; index++) {
      theFunction();
    }
  }