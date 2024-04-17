#!/usr/bin/node
const request = require('request');
const id = process.argv[2];

function makeAPIRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

async function fetchAPIData () {
  try {
    const filmData = await makeAPIRequest(`https://swapi-api.alx-tools.com/api/films/${id}/`);
    const charactersURL = filmData.characters;
    charactersURL.map(async (characterURL) => {
      const characterData = await makeAPIRequest(characterURL);
      const characterName = characterData.name;
      console.log(characterName);
    });
  } catch (error) {
    console.error(error);
  }
}

fetchAPIData();
