from django.conf.urls import include, url
from django.contrib import admin
from viao.views import horas_adelante,crear_usuario,listar,crear_cultivo,inicio,inf_user,inf_cultivo,editar_usuario,editar_cultivo,eliminar_usuario,eliminar_cultivo
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^fecha/$', horas_adelante),
    url(r'^personas/$',listar, name='personas'),
    url(r'^crear/personas/$',crear_usuario, name='crear_personas'),
    url(r'^$','django.contrib.auth.views.login', {'template_name':'index.html'},name='login'),
    url(r'^cerrar/$','django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^cultivo/$',crear_cultivo, name='crear_cultivo'),
    url(r'^inicio/$',inicio, name='inicio'),
    url(r'^informacion/usuario/(?P<cedula>\w+)/$',inf_user,name="informacion"),
    url(r'^informacion/cultivo/(?P<id_cultivo>\w+)/$',inf_cultivo,name="info_cultivo"),
    url(r'^editar/usuario/(?P<cedula>\w+)/$',editar_usuario,name="editar_usuario"),
    url(r'^editar/cultivo/(?P<id_cultivo>\w+)/$',editar_cultivo,name="editar_cultivo"),
    url(r'^eliminar/usuario/(?P<cedula>\w+)/$',eliminar_usuario,name="eliminar_usuario"),
    url(r'^eliminar/cultivo/(?P<id_cultivo>\w+)/$',eliminar_cultivo,name="eliminar_cultivo"),
    
   
]


