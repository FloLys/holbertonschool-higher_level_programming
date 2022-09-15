#!/usr/bin/node
// prints all characters of a Star Wars movie
// The first argument is the Movie ID
// Display one character name by line

const axios = require('axios');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

axios.get(url, 'utf8')
  .then(response => {
    const characters = response.data.characters;
    for (const i in characters) {
      axios.get(characters[i])
        .then(character => {
          console.log(character.data.name);
        });
    }
  })
  .catch(error => {
    console.log(error);
  });
