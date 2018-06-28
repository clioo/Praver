var emailValido = true;
var email;
$(document).ready(function(){
    email = $("#id_correo").val();
});

$("#frm-cambiarContrasena").submit(function(event){
    event.preventDefault();
    var salidas = [];
    
    salidas.push(validarInput('id_confirmarContrasena',8));
    salidas.push(validarInput('id_contrasenaNueva',8));
    salidas.push(validarInput('id_contrasenaActual',8));
    document.getElementById('id_strong_contrasenas').style.visibility = "hidden";
    if ($("#id_contrasenaNueva").val() != $("#id_confirmarContrasena").val()) {
        document.getElementById('id_strong_contrasenas').style.visibility = "visible";
        document.getElementById('id_strong_contrasenas').innerText = "Las contraseñas no coinciden";
        document.getElementById('id_contrasenaNueva').value = "";
        document.getElementById('id_contrasenaNueva').classList.remove("has-success")
        document.getElementById('id_confirmarContrasena').value = "";
        document.getElementById('id_confirmarContrasena').classList.remove("has-success")
        salidas.push(validarInput('id_contrasenaNueva'));
        salidas.push(validarInput('id_confirmarContrasena'));
    }
    var salir =  true;
    salidas.forEach(salida => {
    if (salida == false) {
      salir = false;
    }
  });
  if (salir) {
    $.ajax({
        type: 'GET',
        url: '/ajax/autenticar',
        data:{
            'contrasena': document.getElementById('id_contrasenaActual').value,
        },
        dataType: 'text',
        success:function(datos){
            console.log(datos)
            if (datos == "True") {
                $("#pageloader").fadeIn();
                document.getElementById("frm-cambiarContrasena").submit();
            }else{
                document.getElementById("id_contrasenaActual").classList.remove("has-success")
                document.getElementById("id_contrasenaActual").classList.add("has-danger")
                document.getElementById("id_strong_contrasenaCorrecta").style.visibility="visible";
                document.getElementById("id_strong_contrasenaCorrecta").innerText="La contraseña no es correcta"
            }
            
        },
        error : function(xhr,errmsg,err) {
            console.log(errmsg);
        }
        });
  }
});

$("#input-b9").fileinput({
    language:"es",
    showPreview: true,
    showUpload: false,
    elErrorContainer: '#kartik-file-errors',
    allowedFileExtensions: ["jpg", "png", "gif", "jpeg"]
    //uploadUrl: '/site/file-upload-single'
});

$("#form-datos").submit(function(event){
    event.preventDefault();
    if (emailValido) {
        $("#pageloader").fadeIn();
        document.getElementById("form-datos").submit();
    }
    
});
$("#id_correo").blur(function(){
        $.ajax({
            type: 'GET',
            url: '/json/correoDisponible',
            data:{
                'correo': document.getElementById('id_correo').value,
            },
            dataType: 'text',
            success:function(datos){
                //si el email original es diferente al del input
                if (email != $("#id_correo").val()) {
                    var correo = document.getElementById('id_correo');
                if (validateEmail(correo.value)) {
                    
                    document.getElementById('id_strong_correo').style.visibility = "hidden";
                    if(datos == "True"){
                        emailValido = true;
                        document.getElementById('id_strong_correo').style.visibility = "visible";
                        document.getElementById('id_strong_correo').style.color = "green";
                        correo.classList.remove("has-danger");
                        correo.classList.add("hass-success");
                        document.getElementById('id_strong_correo').innerText = "Correo disponible";
                    }
                    else{
                        emailValido = false;
                        document.getElementById('id_strong_correo').style.visibility = "visible";
                        document.getElementById('id_strong_correo').style.color = "red";
                        document.getElementById('id_strong_correo').innerText = "Correo no disponible";
                        correo.classList.add("has-danger");
                        correo.classList.remove("hass-success");
                    }
                    }
                    else{
                        emailValido = false;
                        document.getElementById('id_strong_correo').style.visibility = "visible";
                        document.getElementById('id_strong_correo').style.color = "red";
                        document.getElementById('id_strong_correo').innerText = "Correo inválido";
                        correo.classList.remove("has-success");
                        correo.classList.add("has-danger");
                    }
                    console.log(datos);
                }
                
            },
            error : function(xhr,errmsg,err) {
                console.log(errmsg);
            }
            });
        
            
    
});
function validateEmail(email) {
    var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
    }
function validarInput(id,min=0){
    var input = document.getElementById(id);
    if (input != null) {
        
        if (input.value == ""){
        input.classList.add('has-danger');
        $("#" + id).focus();
        return false;
        }
        else if (input.value.length < min) {
        input.classList.add('has-danger');
        if (document.querySelector('#strong'+id) == null) {
            var strong = document.createElement('strong');
            strong.innerText = `Mínimo ${min} caracteres`;
            strong.id = "strong"+id;
            strong.style.color = "red";
            strong.style.fontSize = "11";
            input.parentElement.appendChild(strong);
            $("#" + id).focus();
        }
        return false;
        }
        else{
        input.classList.add('has-success');
        input.classList.remove('has-danger');
        try {
            document.getElementById("strong"+id).remove();
        }finally{
            return true;
        }
        
        
        }
        
    }
    alert('algo salió mal');

}