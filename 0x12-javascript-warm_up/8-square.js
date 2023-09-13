#!/usr/bin/node
const x = Number(process.argv[2]);

if (!(isNaN(x))) {
  for (let i = 0; i < x; i++) {
    for (let z = 0; z < x; z++) {
      process.stdout.write('X');
    }
    console.log('');
  }
} else {
  console.log('Missing size');
}
