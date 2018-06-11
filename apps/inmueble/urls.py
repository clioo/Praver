from django.conf.urls import url
from apps.inmueble.views import *
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    url(r'^inmueble/publicar',vistaPublicar,name="publicar"),
    url(r'^inmueble/lista-inmueble/(?P<cadenaBusqueda>.*)/(?P<tipoVenta>.*)$',vista_lista_inmuebles,name="listaInmuebles"),
    url(r'^ajax/municipios',ajax_getMunicipios,name="municipios"),
    url(r'^ajax/colonias',ajax_getColonias,name="colonias"),
    url(r'^api/inmuebles/(?P<lat1>.*)/(?P<lat2>.*)/(?P<lon1>.*)/(?P<lon2>.*)$',vista_json_mapaInmuebles,name="jsonMapaInmuebles"),#/(?P<lat1>\d+)/(?P<lat2>\d+)/(?P<lon1>\d+)/(?P<lon2>\d+)/$
    url(r'^api/imagenes-inmueble/(?P<idInmueble>.*)$',vista_json_imagenesInmueble,name="jsonImagenesInmueble"),
    url(r'^api/filtroInmuebles/(?P<lat1>.*)/(?P<lat2>.*)/(?P<lon1>.*)/(?P<lon2>.*)/(?P<precioMin>.*)/(?P<precioMax>.*)/(?P<tipoInmueble>.*)/(?P<recamaras>.*)/(?P<estacionamiento>.*)/(?P<banos>.*)/(?P<mediosBanos>.*)/(?P<tipoVenta>.*)/(?P<tipoRenta>.*)/(?P<tipoTraspaso>.*)/(?P<servicioGas>.*)/(?P<servicioAire>.*)/(?P<servicioSegu>.*)/(?P<servicioCale>.*)/(?P<servicioAmu>.*)$',vista_json_filtroInmuebles,name="jsonFiltroInmuebles"),
    url(r'^api/inmuebleLatLon/(?P<lat>.*)/(?P<lon>.*)$',vista_json_latLonInmueble,name="jsonLatLonInmueble"),
    url(r'^inmueble/inmueble-individual/(?P<id_inmueble>.*)$',vista_inmueble_individual,name="inmuebleIndividual"),
    url(r'^api/contadorVisitas/(?P<id_inmueble>.*)$',ajax_contadorVisitas,name="contadorVisitas"),
    url(r'^inmueble/eliminar-inmueble/(?P<id_inmueble>.*)$',vista_eliminarInmueble,name="eliminarInmueble"),
]
urlpatterns =  format_suffix_patterns(urlpatterns)