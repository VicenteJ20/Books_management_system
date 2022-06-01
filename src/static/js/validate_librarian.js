document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("form").addEventListener('submit', validateLibrarian); 
});

function validateLibrarian(){
    if (document.form.password.value != document.form.confirm_password.value || document.form.email.value != document.form.confirm_email.value){
        alert('Las contraseñas o los correos electrónicos no coinciden');
        document.form.nombre.focus();
        return 0;
    }

    // Se envía el formulario
    document.form.submit();
}