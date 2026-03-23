/* Write a JavaScript script that fetches the character
name from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json */
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
const characterName = document.querySelector('#character');

fetch(url)
    .then(response => response.json())
    .then(data => {
        characterName.textContent = data.name;
    });
