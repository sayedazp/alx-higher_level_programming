#!/usr/bin/node
const listy = require('./100-data').list;
const newl = listy.map((x, i) => x * i);
console.log(listy);
console.log(newl);
