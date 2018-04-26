from django.conf.urls import url
from apps.inmueble.views import vistaPublicar,ajax_getMunicipios,ajax_getColonias,vista_json_inmuebles
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    url(r'^inmueble/publicar',vistaPublicar,name="publicar"),
    url(r'^ajax/municipios',ajax_getMunicipios,name="municipios"),
    url(r'^ajax/colonias',ajax_getColonias,name="colonias"),
    url(r'^api/inmuebles/(?P<lat1>.*)/(?P<lat2>.*)/(?P<lon1>.*)/(?P<lon2>.*)$',vista_json_inmuebles,name="jsonInmuebles"),#/(?P<lat1>\d+)/(?P<lat2>\d+)/(?P<lon1>\d+)/(?P<lon2>\d+)/$
]
urlpatterns =  format_suffix_patterns(urlpatterns)