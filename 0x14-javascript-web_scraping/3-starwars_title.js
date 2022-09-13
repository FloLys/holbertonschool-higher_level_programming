#!/usr/bin/node

const axios = require('axios');
const url = 'https://swapi-api.hbtn.io/api/films/';

axios.get(url + process.argv[2], 'utf8')
  .then(response => {
    console.log(response.data.title);
  })
  .catch(error => {
    console.log(error.message);
  });
