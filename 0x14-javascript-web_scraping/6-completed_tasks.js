#!/usr/bin/node
// computes the number of tasks completed by user id

const axios = require('axios');
const dict = {};

axios.get(process.argv[2], 'utf8')
  .then(response => {
    const body = response.data;
    // iterate through body
    for (const i in body) {
      const tasks = body[i];
      // if task completed...
      if (tasks.completed === true) {
        // check if user already in dictionary
        if (!(tasks.userId in dict)) {
          dict[tasks.userId] = 0;
        }
        dict[tasks.userId] += 1;
      }
    }
    console.log(dict);
  })
  .catch(error => {
    console.log(error);
  });
