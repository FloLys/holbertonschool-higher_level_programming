#!/usr/bin/node
// prints all characters of a Star Wars movie. First arg is Movie ID
// Display one character name by line in the same order
// of the list characters in the /films/ response

const axios = require('axios');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

axios.get(url, 'utf8')
  .then(async response => {
    const characters = response.data.characters;
    for (const i in characters) {
      await axios.get(characters[i])
        .then(character => {
          console.log(character.data.name);
        });
    }
  })
  .catch(error => {
    console.log(error);
  });
