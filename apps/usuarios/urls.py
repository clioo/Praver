from django.conf.urls import url
from apps.usuarios.views import *
urlpatterns = [
    url(r'^$', index, name="index" ),
    url(r'^login/', vista_login, name="login" ),
    url(r'^usuarios/registrar',vista_registrar , name="registrar" ),
    url(r'^logout/',vista_logout,name='logout'),
    url(r'^regEx/',vista_regex,name='regEx'),
    url(r'^json/correoDisponible',vista_json_correoDisponible,name='correoDisponible'),
    url(r'^ajax/autenticar',vista_ajax_autenticar,name='autenticar'),
    url(r'^inmueble/tus-inmuebles',vista_tus_inmuebles,name="tusInmuebles"),
    url(r'^usuarios/perfil',vista_updateProfile , name="actualizarPerfil" ),
]
