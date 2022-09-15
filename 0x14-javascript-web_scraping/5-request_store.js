#!/usr/bin/node
// gets the contents of a webpage and stores it in a file
// second argument the file path to store the body response

const axios = require('axios');

axios.get(process.argv[2], 'utf8')
  .then(response => {
    const fs = require('fs');
    fs.writeFile(process.argv[3], response.data, error => {
      if (error) {
        console.log(error);
      }
    });
  });
