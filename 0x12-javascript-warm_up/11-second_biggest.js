#!/usr/bin/node

const arry = [];
for (let z = 0; z < process.argv.length; z++) {
  arry.push(Number(process.argv[z]));
}

for (let i = 1; i < arry.length; i++) {
  if (arry[i] < arry[i - 1]) {
    const tmp = arry[i - 1];
    arry[i - 1] = arry[i];
    arry[i] = tmp;
  }
}

for (let i = 1; i < arry.length - 1; i++) {
  if (arry[i] < arry[i - 1]) {
    const tmp = arry[i - 1];
    arry[i - 1] = arry[i];
    arry[i] = tmp;
  }
}

console.log(arry[arry.length - 2]);
