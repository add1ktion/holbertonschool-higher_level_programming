#!/usr/bin/node
/* 9-add.js
Write a script that prints the addition of 2 integers
*/

if (isNaN(process.argv[2]) || isNaN(process.argv[3])) {
  console.log('NaN');
} else {
  console.log(parseInt(process.argv[2]) + parseInt(process.argv[3]));
}
