/* Write a JavaScript script that fetches and lists the title for all
movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json */
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
const movieList = document.querySelector('#list_movies');

fetch(url)
    .then(response => response.json())
    .then(data => {
        const movies = data.results;
        movies.forEach(movie => {
            const newMovie = document.createElement('li');
            newMovie.textContent = movie.title;
            movieList.appendChild(newMovie);
        });
    });
