$("#frm-buscar").submit(function(event){
    event.preventDefault();
    window.location.href = "/inmueble/lista-inmueble/" + document.getElementById('pac-input').value + "/";
});