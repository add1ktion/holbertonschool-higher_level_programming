#!/usr/bin/node
/* 2-arguments.js
Write a JavaScript script that prints the first argument passed to it
*/

const myVar = process.argv;

if (myVar.length <= 2) {
  console.log('No argument');
}
else if (myVar.length === 3) {
  console.log('Argument found');
}
else {
  console.log('Arguments found');
}
