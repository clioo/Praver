$(document).ready(function(){
    $('.telefono').mask('(000) 000 00 00');
});
$("#id_tipo_agente").click(function(){
    $("#div_id_apellido_paterno").show(500);
    $("#div_id_apellido_materno").show(500);
});
$("#id_tipo_inmobiliaria").click(function(){
    $("#div_id_apellido_paterno").hide(500);
    $("#div_id_apellido_materno").hide(500);
});
$("#id_btn_registrar").click(function(){
    if (validateForm()) {
        document.getElementById('id_frm_registrar').submit();
    }
});
$("#id_correo").blur(function() {
    $.ajax({
        type: 'GET',
        url: '/json/correoDisponible',
        data:{
          'correo': document.getElementById('id_correo').value,
        },
        dataType: 'text',
        success:function(datos){
            var correo = document.getElementById('id_correo');
            if (validateEmail(correo.value)) {
                document.getElementById('id_strong_correo').style.visibility = "hidden";
                if(datos == "True"){
                    document.getElementById('id_strong_correo').style.visibility = "visible";
                    document.getElementById('id_strong_correo').style.color = "green";
                    correo.classList.remove("has-danger");
                    correo.classList.add("hass-success");
                    document.getElementById('id_strong_correo').innerText = "Correo disponible";
                }
                else{
                    document.getElementById('id_strong_correo').style.visibility = "visible";
                    document.getElementById('id_strong_correo').style.color = "red";
                    document.getElementById('id_strong_correo').innerText = "Correo no disponible";
                    correo.classList.add("has-danger");
                    correo.classList.remove("hass-success");
                }
            }
            else{
                document.getElementById('id_strong_correo').style.visibility = "visible";
                document.getElementById('id_strong_correo').style.color = "red";
                document.getElementById('id_strong_correo').innerText = "Correo inválido";
                correo.classList.remove("has-success");
                correo.classList.add("has-danger");
            }
            console.log(datos);
        },
        error : function(xhr,errmsg,err) {
          console.log(errmsg);
        }
      });
});
function validateForm() {
    var salidas = [];
    salidas.push(validarInput('id_telefono1'));
    if ($('#id_tipo_agente').is(':checked')) {
        salidas.push(validarInput('id_apellido_paterno'));
    }
    salidas.push(validarInput('id_nombre'));
    salidas.push(validarInput('id_contrasena2',8));
    salidas.push(validarInput('id_contrasena',8));
    if ($("#id_contrasena").val() != $("#id_contrasena2").val()) {
        document.getElementById('id_strong_contrasenas').style.visibility = "visible";
        document.getElementById('id_strong_contrasenas').innerText = "Las contraseñas no coinciden";
        document.getElementById('id_contrasena').value = "";
        document.getElementById('id_contrasena2').value = "";
        salidas.push(validarInput('id_contrasena'));
        salidas.push(validarInput('id_contrasena2'));
    }
    else{
        document.getElementById('id_strong_contrasenas').style.visibility = "hidden";
    }
    var salir =  true;
  salidas.forEach(salida => {
    if (salida == false) {
      salir = false;
    }
  });
  console.log(salir);
  return salir;
}

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