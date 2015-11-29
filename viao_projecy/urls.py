from django.conf.urls import include, url
from django.contrib import admin
from viao.views import horas_adelante,fpersonas,person,fcultivo,inicio,inf_user,editar
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^personas/$',person, name='personas'),
    url(r'^crear/personas/$',fpersonas, name='crear_personas'),
    url(r'^$','django.contrib.auth.views.login', {'template_name':'index.html'},name='login'),
    url(r'^cerrar/$','django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^cultivo/$',fcultivo, name='crear_cultivo'),
    url(r'^inicio/$',inicio, name='inicio'),
    url(r'^informacion/usuario/(?P<cedula>\w+)/$',inf_user,name="informacion"),
    url(r'^editar/usuario/(?P<cedula>\w+)/$',editar,name="editar_usuario"),
]


