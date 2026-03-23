/* Write a JavaScript script that adds a li element to
a list when the user clicks on the element with id add_item */
const addItem = document.querySelector('#add_item');
const list = document.querySelector('ul.my_list');

function addListItem() {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    list.appendChild(newItem);
}

addItem.addEventListener('click', addListItem);
