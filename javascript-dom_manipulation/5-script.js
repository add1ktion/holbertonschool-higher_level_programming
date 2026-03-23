/* Write a JavaScript script that updates the text of the header element to
New Header!!! when the user clicks on the element with id update_header */
const updateHeader = document.querySelector('#update_header');
const header = document.querySelector('header');

function updateHeaderText() {
    header.textContent = 'New Header!!!';
}

updateHeader.addEventListener('click', updateHeaderText);
