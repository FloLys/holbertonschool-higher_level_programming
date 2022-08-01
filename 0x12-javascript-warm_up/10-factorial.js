#!/usr/bin/node
const num = parseInt(process.argv[2]);
function factorial (a) {
  if (isNaN(a) || a === 0) {
    return (1);
  } else if (a > 0) {
    return (a * factorial(a - 1));
  }
}
console.log(factorial(num));
