#!/usr/bin/node

const axios = require('axios');
let count = 0;

axios.get(process.argv[2], 'utf8')
  .then(response => {
    const movies = response.data.results;
    for (const i in movies) {
      const people = movies[i].characters;
      for (const j in people) {
        if (people[j].includes('/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  })
  .catch(error => {
    console.log(error);
  });
