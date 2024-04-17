#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const movieURL = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

function getMovieCharacters (characterList, index) {
  if (characterList.length === index) {
    return;
  }

  request(characterList[index], { json: true }, (error, response, body) => {
    if (error) {
      console.error(error);
    }
    console.log(body.name);
    getMovieCharacters(characterList, index + 1);
  });
}

request(movieURL, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const characterList = body.characters;
  getMovieCharacters(characterList, 0);
});
