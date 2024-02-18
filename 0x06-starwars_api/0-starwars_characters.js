#!/usr/bin/node
const request = require('request');

const fetchCharacter = (url) =>
  new Promise((resolve, reject) => {
    request(url, (err, res, data) => {
      if (err || res.statusCode !== 200) {
        reject(err || new Error(`Failed to fetch data from ${url}`));
      } else {
        resolve(JSON.parse(data).name);
      }
    });
  });

const fetchFilmCharacters = (filmId) => {
  const filmUrl = `https://swapi-api.alx-tools.com/api/films/${filmId}`;
  return new Promise((resolve, reject) => {
    request(filmUrl, (err, res, data) => {
      if (err || res.statusCode !== 200) {
        reject(err || new Error(`Failed to fetch data from ${filmUrl}`));
      } else {
        const { characters } = JSON.parse(data);
        resolve(characters);
      }
    });
  });
};

const printCharacterNames = async (filmId) => {
  try {
    const characterUrls = await fetchFilmCharacters(filmId);
    const characterNames = await Promise.all(characterUrls.map(fetchCharacter));
    characterNames.forEach((name) => console.log(name));
  } catch (error) {
    console.error('Error:', error.message);
  }
};

const main = () => {
  const [, , filmId] = process.argv;
  if (!filmId) {
    console.error('Usage: node scriptName.js <filmId>');
    process.exit(1);
  }

  printCharacterNames(filmId);
};

main();
