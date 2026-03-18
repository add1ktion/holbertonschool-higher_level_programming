#!/usr/bin/node
/* 2-arguments.js
Write a script that prints a message depending of the number of arguments passed
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
