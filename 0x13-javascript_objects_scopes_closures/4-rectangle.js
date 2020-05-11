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
Rectangle.prototype.double = function double () {
  this.height = this.height * 2;
  this.width = this.width * 2;
};
Rectangle.prototype.rotate = function rotate () {
  const other = this.width;
  this.width = this.height;
  this.height = other;
};
module.exports = Rectangle;
