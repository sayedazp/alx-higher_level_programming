#!/usr/bin/node
let x = 0;
exports.logMe = function (item) {
  function logging () {
    x++;
  }
  console.log(x + ': ' + item);
  logging();
};
