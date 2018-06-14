var emailValido = true;
var email;
$(document).ready(function(){
    email = $("#id_correo").val();
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
            document.getElementById("form-datos").submit();
        }
        
    });
    $("#id_correo").blur(function(){
        if(validateEmail($(this).val())){
            $.ajax({
                type: 'GET',
                url: '/json/correoDisponible',
                data:{
                  'correo': document.getElementById('id_correo').value,
                },
                dataType: 'text',
                success:function(datos){
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
            
                
        }
        
    });
    function validateEmail(email) {
        var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(email);
      }