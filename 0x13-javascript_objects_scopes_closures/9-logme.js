#!/usr/bin/node
exports.logMe = function (item) {
  let logged = 0;
  console.log(logged + ': ' + item);
  logged++;
};
