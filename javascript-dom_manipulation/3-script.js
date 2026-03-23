/* Write a JavaScript script that toggles the class of the
header element when the user clicks on the tag id toggle_header */
const header = document.querySelector('header');
const toggleHeader = document.querySelector('#toggle_header');

function toggleClass() {
    header.classList.toggle('red');
    header.classList.toggle('green');
}

toggleHeader.addEventListener('click', toggleClass);
