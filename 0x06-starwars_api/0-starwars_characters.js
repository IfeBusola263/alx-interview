#!/usr/bin/node

// get the movie id
const movieId = process.argv[2];

// import the request module to query api
const request = require('request');

// send request
request(`https://swapi-api.alx-tools.com/api/films/{movieId}`, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    // collect info of movie and the cast in the results attribute
    // which is a list of movie objects. movieId gives us the exact movie
    // charcaters attribut of the object gives a list of api to the
    // actors of each movie
    const films = JSON.parse(body);
    const characters = films.results.characters;

    // create a promise for each character
    const arrProm = characters.map((character) => {
      return new Promise((resolve, reject) => {
        request(character, (error, response, body) => {
          if (!error && response.statusCode === 200) {
            const actor = JSON.parse(body);
            resolve(actor);
          } else {
            reject(error);
          }
        });
      });
    });

    // Resolve all the promises, and display any error encountered.
    Promise.all(arrProm).then(characterData => {
      characterData.forEach(character => console.log(character.name));
    }).catch(error => console.error(error));
  } else {
    console.log(error);
  }
});
