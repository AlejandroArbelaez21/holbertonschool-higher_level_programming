#!/usr/bin/node
const Square1 = require('./5-square');

class Square extends Square1 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let index = 0; index < this.width; index++) {
      if (c === undefined) {
        console.log('X'.repeat(parseInt(this.width)));
      } else {
        console.log(c.repeat(parseInt(this.width)));
      }
    }
  }
}
module.exports = Square;
