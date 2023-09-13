#!/usr/bin/node

function addMeMaybe (num, fun) {
  num++;
  fun(num);
}

module.exports = { addMeMaybe };
