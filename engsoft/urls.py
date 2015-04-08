from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'sirius.views.index'),
    url(r'^adiciona_documento/', 'sirius.views.adiciona_documento'),
    # url(r'^engsoft/', include('engsoft.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/destino/', include('django.contrib.admindocs.urls')),

    #url(r'^view_imagem/', 'sirius.views.view_imagem'),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
