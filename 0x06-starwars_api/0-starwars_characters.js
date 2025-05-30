#!/usr/bin/node

const request = require('request-promise');

const args = process.argv.slice(2);
if (args.length !== 1) {
  console.log('Usage: ./0-starwars_characters movie_id');
  process.exit(1);
}

const movieUrl = 'https://swapi-api.alx-tools.com/api/films/' + args[0];

async function fetchCharacters() {
  try {
    const movieData = await request(movieUrl);
    const movie = JSON.parse(movieData);
    const characters = movie.characters;

    for (const url of characters) {
      try {
        const charData = await request(url);
        const character = JSON.parse(charData);
        console.log(character.name);
      } catch (err) {
        console.log('Error fetching character:', err.message);
        process.exit(1);
      }
    }
  } catch (err) {
    console.log('Error fetching movie:', err.message);
    process.exit(1);
  }
}

fetchCharacters();
