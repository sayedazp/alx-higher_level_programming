#!/usr/bin/node

const proargv = process.argv.length;

if (proargv.length === 3) {
  console.log('Argument found');
} else if (proargv === 2) {
  console.log('No argument');
} else {
  console.log('Arguments found');
}
