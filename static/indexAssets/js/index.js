$('#cmd-buscar').click(function(){
	let cadenaFiltro = "";
	if ($("#cmd-comprar").hasClass("active")) cadenaFiltro = "c,";
	if ($("#cmd-rentar").hasClass("active")) cadenaFiltro = cadenaFiltro + "r,";
	if ($("#cmd-traspasar").hasClass("active")) cadenaFiltro = cadenaFiltro +  "t,";
	window.location.href = "/inmueble/lista-inmueble/" + document.getElementById('pac-input').value + "/" + cadenaFiltro;
});
$("#namer input").on("change keyup paste", function() {
	var inputValue = $(this).val();

	if (inputValue) {
		$("#namer").addClass("active");
	} else {
		$("#namer").removeClass("active");
	}
});

$(document).on("click", ".namer-controls.active .contenedorSpan", function() {
	if ($(this).hasClass("active")) {
		//$(".namer-controls span").removeClass("active");
		$("#namer-input").removeClass($(this).text());
		$(this).removeClass("active");
	} else {
		//$(".namer-controls span").removeClass("active");
		$(this).addClass("active");
		var styleClass = $(this).text();
		$("#namer-input").addClass(styleClass);
	}
});

$(document).ready(function() {
	$("#namer-input input").focus();
});