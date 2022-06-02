const del_button = document.getElementById('del_button');
const confirmation_alert = document.getElementById('confirmation_alert');
const close_modal = document.getElementsByClassName('close_modal')[0];
const button_modal = document.getElementsByClassName('button_modal')[0];
const delete_button = document.getElementById('delete_button');

del_button.addEventListener('click', function(){
    confirmation_alert.style.display = 'flex';
    confirmation_alert.style.justifyContent = 'center';
    confirmation_alert.style.alignItems = 'center';
})

close_modal.addEventListener('click', function(){
    confirmation_alert.style.display = 'none';
})

confirmation_alert.addEventListener('click', function() {
    confirmation_alert.style.display = 'none';
})

function validateSend(){
    if (delete_button.onclick() == true){
        return true;
    } else {
        return false;
    }
}