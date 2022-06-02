const form = document.getElementById('form');

const submit = document.getElementById('submit');

let password = document.getElementById('password');
let confirm_password = document.getElementById('confirm_password');

let email = document.getElementById('email');
let confirm_email = document.getElementById('confirm_email');

submit.addEventListener('click', function(){
    if(password.value != confirm_password.value){
        alert('Las contraseñas no coinciden, reviselas para continuar');
    } else if (email.value != confirm_email.value){
        alert('Los correos electrónicos no coinciden');
    }

    return validateButton();
});

function validateButton(){
    if ((password.value == confirm_password.value) && (email.value == confirm_email.value)){
        return true;
    } else {
        return false;
    }
}