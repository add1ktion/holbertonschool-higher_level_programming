#!/usr/bin/node
/* 11-second_biggest.js
Write a script that searches the second biggest integer in the list of arguments.
*/

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = process.argv.slice(2).map(Number);
  args.sort((a, b) => b - a);
  console.log(args[1]);
}
