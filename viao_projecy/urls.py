from django.conf.urls import include, url, patterns
from django.contrib import admin
from viao.views import horas_adelante,fpersonas,person

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^fecha/$', horas_adelante),
    url(r'^personas/$',person, name='personas'),
    url(r'^crear/personas/$',fpersonas, name='crear_personas'),
    url(r'^$','django.contrib.auth.views.login', {'template_name':'index.html'},name='login'),
    url(r'^cerrar/$','django.contrib.auth.views.logout_then_login', name='logout'),
]

