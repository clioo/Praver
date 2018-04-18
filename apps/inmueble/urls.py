from django.conf.urls import url
from apps.inmueble.views import vistaPublicar,ajax_getMunicipios,ajax_getColonias
urlpatterns = [
    url(r'^inmueble/publicar',vistaPublicar,name="publicar"),
    url(r'^ajax/municipios',ajax_getMunicipios,name="municipios"),
    url(r'^ajax/colonias',ajax_getColonias,name="colonias"),
]