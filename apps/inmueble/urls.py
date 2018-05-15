from django.conf.urls import url
from apps.inmueble.views import vista_json_latLonInmueble,vista_json_filtroInmuebles,vistaPublicar,ajax_getMunicipios,ajax_getColonias,vista_json_mapaInmuebles,vista_json_imagenesInmueble
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    url(r'^inmueble/publicar',vistaPublicar,name="publicar"),
    url(r'^ajax/municipios',ajax_getMunicipios,name="municipios"),
    url(r'^ajax/colonias',ajax_getColonias,name="colonias"),
    url(r'^api/inmuebles/(?P<lat1>.*)/(?P<lat2>.*)/(?P<lon1>.*)/(?P<lon2>.*)$',vista_json_mapaInmuebles,name="jsonMapaInmuebles"),#/(?P<lat1>\d+)/(?P<lat2>\d+)/(?P<lon1>\d+)/(?P<lon2>\d+)/$
    url(r'^api/imagenes-inmueble/(?P<idInmueble>.*)$',vista_json_imagenesInmueble,name="jsonImagenesInmueble"),
    url(r'^api/filtroInmuebles',vista_json_filtroInmuebles,name="jsonFiltroInmuebles"),
    url(r'^api/inmuebleLatLon/(?P<lat>.*)/(?P<lon>.*)$',vista_json_latLonInmueble,name="jsonLatLonInmueble"),
]
urlpatterns =  format_suffix_patterns(urlpatterns)