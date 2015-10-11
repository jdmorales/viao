from django.conf.urls import patterns, include, url
from django.contrib import admin
from viao.views import horas_adelante

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'viao_projecy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'fecha/(\d{1,2})/$', horas_adelante),
)
