$("#frm-buscar").submit(function(event){
    event.preventDefault();
    window.location.href = "/inmueble/lista-inmueble/" + document.getElementById('pac-input').value + "/";
});

$(".linkInmueble").click(function(){
    fetch("/api/contadorVisitas/" + $(this).attr("valor"));
});