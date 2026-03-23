/* Write a JavaScript script that adds the class red to the
header element when the user clicks on the tag with id red_header */
const header = document.querySelector('header');
const redHeader = document.querySelector('#red_header');

function addClass() {
  header.classList.add('red');
}

redHeader.addEventListener('click', addClass);
