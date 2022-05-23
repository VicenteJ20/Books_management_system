document.getElementById('btn_open').addEventListener('click', open_close_button);


let side_menu = document.getElementById('menu_side');
let btn_open = document.getElementById('btn_open');
let body = document.getElementById('body');

// funcionamiento
function open_close_button(){
    body.classList.toggle('body_move')
    side_menu.classList.toggle('side_menu_move');
}