#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || h === undefined || w === undefined) {
      w = {};
      h = {};
    } else {
      this.width = w;
      this.height = h;
    }
  }
}
Rectangle.prototype.print = function print () {
  for (let index = 0; index < this.height; index++) {
    console.log('X'.repeat(parseInt(this.width)));
  }
};
module.exports = Rectangle;
