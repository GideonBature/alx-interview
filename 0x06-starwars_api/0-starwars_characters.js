#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];

function getAPIRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, { json: true }, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(body);
      }
    });
  });
}

async function fetchAPIData (movieId) {
  try {
    const filmData = await getAPIRequest(`https://swapi-api.alx-tools.com/api/films/${movieId}/`);
    const charactersURL = filmData.characters;
    charactersURL.forEach(async (url) => {
      const characterData = await getAPIRequest(url);
      console.log(characterData.name);
    })
  } catch (error) {
    console.error(error);
  }
}

fetchAPIData(movieId);
