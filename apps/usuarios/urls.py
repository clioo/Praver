from django.conf.urls import url
from apps.usuarios.views import vista_regex,index,vista_login,vista_registrar,vista_logout,vista_json_correoDisponible,vista_tus_inmuebles
urlpatterns = [
    url(r'^$', index, name="index" ),
    url(r'^login/', vista_login, name="login" ),
    url(r'^usuarios/registrar',vista_registrar , name="registrar" ),
    url(r'^logout/',vista_logout,name='logout'),
    url(r'^regEx/',vista_regex,name='regEx'),
    url(r'^json/correoDisponible',vista_json_correoDisponible,name='correoDisponible'),
    url(r'^inmueble/tus-inmuebles',vista_tus_inmuebles,name="tusInmuebles"),
]
