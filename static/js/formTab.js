var currentTab = 0; // Current tab is set to be the first tab (0)
document.getElementById('id_tipoVenta_3').addEventListener('click',checkBoxTipoVenta);
document.getElementById('id_tipoVenta_2').addEventListener('click',checkBoxTipoVenta);
document.getElementById('id_tipoVenta_1').addEventListener('click',checkBoxTipoVenta);
showTab(currentTab); // Display the current tab
$('#select_image').change(function(){
  $('#upload_form').submit();  
});
$("#input-42-es").fileinput({
  language:"es",
  maxFileCount: 10,
  allowedFileExtensions: ["jpg", "gif", "png", "txt", "jpeg"]
});
$("#id_descripcion").each(function(){
  $(this).typeProgress();
});
$("#id_titulo").each(function(){
  $(this).typeProgress();
});
$("#id_descripcion").on('input',function(e){
  var valor = $(this).val();
  var elemento = document.getElementById("id_descripcion");
  if (valor.length >49) {
    elemento.parentElement.querySelector(".type-progress").style.background ="#00ff00";
  }
  else{
    elemento.parentElement.querySelector(".type-progress").style.background ="#ff0000";
  }
});
$("#id_titulo").on('input',function(){
  var valor = $(this).val();
  var elemento = document.getElementById("id_titulo");
  if (valor.length >19) {
    elemento.parentElement.querySelector(".type-progress").style.background ="#00ff00";

  }
  else{
    elemento.parentElement.querySelector(".type-progress").style.background ="#ff0000";
  }
});

$('#upload_form').on('submit', function(e){  
  e.preventDefault();  
});
$('#id_estado').change(changeEstado);
$('#id_municipio').change(function(){
  var municipio = $(this).val();
  var estado = $('#id_estado').val();
  $('#id_colonia').empty();
  $.ajax({
    type: 'GET',
    url: '/ajax/colonias',
    data:{
      'municipio': municipio,
      'estado':estado
    },
    dataType: 'json',
    success:function(datos){
      var comboBox = document.getElementById('id_colonia');
      $(datos).each(function(i,obj){
        var opcion = document.createElement('option');
        opcion.value = obj.id;
        opcion.innerText = obj.d_asenta;
        opcion.setAttribute("codigopostal",obj.d_codigo);
        comboBox.appendChild(opcion);
      });
      document.getElementById('id_codigoPostal').value = $('#id_colonia').find(":selected").attr("codigopostal");
    },
    error : function(xhr,errmsg,err) {
      console.log(errmsg);
    }
  });
});
$('#id_colonia').change(function(){
  document.getElementById('id_codigoPostal').value = $('#id_colonia').find(":selected").attr("codigopostal");
});
$(document).ready(function(){
  
  $('.2digitos').mask('00');
  $('.4digitos').mask('0,000.00', {reverse:true});
  $('.numExt').mask('0000');
  $('.CP').mask('00000');
  $('.money').mask("000'000,000.00", {reverse: true});
  $('[data-toggle="tooltip"]').tooltip(); 

});

function changeEstado(){
  $('#id_municipio').empty();
  addTupla0(document.getElementById('id_municipio'),'--------------');
  $('#id_colonia').empty();
  addTupla0(document.getElementById('id_colonia'),'--------------');
  var estado = $(this).val();
  $.ajax({
    type: 'GET',
    url: '/ajax/municipios',
    data:{
      'estado': estado
    },
    dataType: 'json',
    success:function(datos){
      console.log(datos);
      var comboBox = document.getElementById('id_municipio');
      for (let i = 0; i < datos[0].length; i++) {
        var opcion = document.createElement('option');
        opcion.value = datos[1][i];
        opcion.innerText = datos[0][i];
        comboBox.appendChild(opcion);
      }
    },
    error : function(xhr,errmsg,err) {
      console.log(errmsg);
    }
  });
}
function checkBoxTipoVenta(e){
  if (e.target.checked == true) {
    if (e.target.value == "vent") {
      document.getElementById('id_precioVenta').disabled = false;
    }
    else if (e.target.value == "rent") {
      document.getElementById('id_precioRenta').disabled = false;
    }
    else if (e.target.value == "tras") {
      document.getElementById('id_precioTraspaso').disabled = false;
    }
  }
  else{
    if (e.target.value == "vent") {
      document.getElementById('id_precioVenta').disabled = true;
    }
    else if (e.target.value == "rent") {
      document.getElementById('id_precioRenta').disabled = true;
    }
    else if (e.target.value == "tras") {
      document.getElementById('id_precioTraspaso').disabled = true;
    }
  }
}
function showTab(n) {
  // This function will display the specified tab of the form ...
  var x = document.getElementsByClassName("tab");
  x[n].style.display = "block";
  // ... and fix the Previous/Next buttons:
  if (n == 0) {
    document.getElementById("btnAnt").style.display = "none";
  } else {
    document.getElementById("btnAnt").style.display = "inline";
  }
  if (n == (x.length - 1)) {
    document.getElementById("btnSig").innerHTML = "Publicar";
  } else {
    document.getElementById("btnSig").innerHTML = "Siguiente";
  }
  // ... and run a function that displays the correct step indicator:
  fixStepIndicator(n)
}
function nextPrev(n) {
  if (n < 0) {
    var x = document.getElementsByClassName("step");
    for (i = 0; i < x.length; i++) {
      x[i].className = x[i].className.replace("active", "");
    }
  }
  // This function will figure out which tab to display
  var x = document.getElementsByClassName("tab");
  // Exit the function if any field in the current tab is invalid:
  if (n == 1 && !validateForm()) return false;
  // Hide the current tab:
  x[currentTab].style.display = "none";
  // Increase or decrease the current tab by 1:
  currentTab = currentTab + n;
  // if you have reached the end of the form... :
  if (currentTab >= x.length) {
    //...the form gets submitted:
    document.getElementById("regForm").submit();
    $("#pageloader").fadeIn();
    return false;
  }
  // Otherwise, display the correct tab:
  showTab(currentTab);
}
function validateForm() {
  var salidas = [];
  //tab 0
  if (currentTab == 0) {
    salidas.push(validarInput('id_titulo',20));
    salidas.push(validarInput('id_descripcion',50));
  }
  //tab 1
  if (currentTab == 1) {
    var chB1 = document.getElementById('id_tipoVenta_1'), chB2 = document.getElementById('id_tipoVenta_2');
    var chB3 = document.getElementById('id_tipoVenta_3');
    salidas.push(validarInput('id_antiguedad'));
    salidas.push(validarInput('id_recamaras'));
    salidas.push(validarInput('id_estacionamiento'));
    salidas.push(validarInput('id_banos'));
    salidas.push(validarInput('id_mediosBanos'));
    salidas.push(validarInput('id_metrosConstruidos'));
    salidas.push(validarInput('id_metrosTotales'));
    if (parseInt($("#id_metrosTotales").val()) < parseInt($("#id_metrosConstruidos").val())) {
      var metrosTotales = document.getElementById('id_metrosTotales');
      var strong  = document.createElement('strong');
      strong.innerText = `El valor de metros totales es menor al de metros construidos`;
      strong.id = "strongMetros";
      strong.style.color = "red";
      strong.style.fontSize = "11";
      metrosTotales.parentElement.appendChild(strong);
      var mt = $("#id_metrosTotales").val();
      var mc = $("#id_metrosConstruidos").val();
      document.getElementById("id_metrosTotales").value = "";
      document.getElementById("id_metrosConstruidos").value = "";
      salidas.push(validarInput('id_metrosConstruidos'));
      salidas.push(validarInput('id_metrosTotales'));
      document.getElementById("id_metrosTotales").value = mt;
      document.getElementById("id_metrosConstruidos").value = mc;
    }else{
      try {
        document.getElementById('strongMetros').remove();
      } catch (error) {
        
      }
    }
    try {
      document.getElementById('strongTipoVenta').remove();
    } catch (error) {
      
    }
    if ((chB1.checked == false) && (chB2.checked ==false)&&(chB3.checked ==false)){
      salidas.push(false);
      var lblTipoVenta = document.getElementById('containerTitulo');
      strong  = document.createElement('strong');
      strong.innerText = `Se necesita seleccionar un tipo de venta`;
      strong.id = "strongTipoVenta";
      strong.style.color = "red";
      strong.style.fontSize = "11";
      lblTipoVenta.appendChild(strong);
    }
    if (chB1.checked == true) {
      salidas.push(validarInput('id_precioVenta'));
    }
    if (chB2.checked == true) {
      salidas.push(validarInput('id_precioRenta'));
    }
    if (chB3.checked == true) {
      salidas.push(validarInput('id_precioTraspaso'));
    }
  }
  //tab 2
  if (currentTab == 2) {
    var estado = document.getElementById('id_estado');
    var municipio = document.getElementById('id_municipio');
    var mostrarMapa = document.getElementById('id_mostrarMapa');
    var strongEstado = document.getElementById('idStrongEstados');
    var strongMostrarMapa = document.getElementById('idStrongMostrarMapa');
    var latitud = document.getElementById('id_latitud');
    var longitud=document.getElementById('id_longitud');
    console.log(mostrarMapa.value);
    if(estado.value == "0"){
      strongEstado.style.visibility = "visible";
      strongEstado.innerText = "Necesitas escoger un estado";
      salidas.push(false);
    }
    else if (municipio.value == "0") {
      strongEstado.style.visibility = "visible";
      strongEstado.innerText = "Necesitas escoger un municipio";
      salidas.push(false);
    }
    else{
      strongEstado.style.visibility = "hidden";
    }
    salidas.push(validarInput('id_calle'));
    salidas.push(validarInput('id_numExt'));
    if (mostrarMapa.value == "0") {
      strongMostrarMapa.innerText = "Decisión necesaria";
      strongMostrarMapa.style.visibility = "visible";
      salidas.push(false);
    }else if((mostrarMapa.value == "exac" || mostrarMapa.value == "apro") && latitud.value == "0"){
      strongMostrarMapa.innerText = "Necesita elegir el punto de su inmueble";
      strongMostrarMapa.style.visibility = "visible";
      salidas.push(false);
    } else {
      strongMostrarMapa.style.visibility = "hidden";
    }
    
  }
  //tab 3
  if (currentTab == 3) {
    if ($(".file-preview-thumbnails").children().length == 0) {
      var metrosTotales = document.querySelector('.file-preview');
      var strong  = document.createElement('strong');
      strong.innerText = `Necesitas subir al menos una imágen`;
      strong.id = "strongImagenes";
      strong.style.color = "red";
      strong.style.fontSize = "11";
      metrosTotales.appendChild(strong);
      salidas.push(false)
    }else{
      try {
        document.getElementById('strongImagenes').remove();
      } catch (error) {
        
      }
    }
  }

  var salir =  true;
  salidas.forEach(salida => {
    if (salida == false) {
      salir = false;
    }
  });
  return salir;
}

function fixStepIndicator(n) {
  // This function removes the "active" class of all steps...
  var i, x = document.getElementsByClassName("step");
  for (i = 0; i < x.length; i++) {
    x[i].className = x[i].className.replace("active", "finish");
  }
  //... and adds the "active" class to the current step:
  x[n].className += " active";
}

function validarInput(id,min=0){
  var input = document.getElementById(id);
  if (input != null) {
    
    if (input.value == ""){
      input.classList.add('has-danger');
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
function addTupla0(elemento,descripcion){
  var opcion=document.createElement('option');
  opcion.value = "0";
  opcion.innerText = descripcion;
  elemento.appendChild(opcion);
}