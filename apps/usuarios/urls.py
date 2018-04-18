from django.conf.urls import url
from apps.usuarios.views import vista_regex,index,vista_login,vista_registrarAgente,vista_logout
urlpatterns = [
    url(r'^$', index, name="index" ),
    url(r'^login/', vista_login, name="login" ),
    url(r'^usuarios/registrar/agente',vista_registrarAgente , name="registrarAgente" ),
    url(r'^logout/',vista_logout,name='logout'),
    url(r'^regEx/',vista_regex,name='regEx')
]
