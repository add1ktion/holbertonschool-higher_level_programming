/* Write a JavaScript script that fetches from https://hellosalut.stefanbohacek.com/?lang=fr
and displays the value of hello from that fetch in the HTML element with id hello */
document.addEventListener('DOMContentLoaded', function() {
    const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';
    const helloElement = document.querySelector('#hello');

    fetch(url)
        .then(response => response.json())
        .then(data => {
            helloElement.textContent = data.hello;
        });
});
