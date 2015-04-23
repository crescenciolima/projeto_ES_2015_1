from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'sirius.views.index'),
    url(r'^adiciona_documento/', 'sirius.views.adiciona_documento'),

    # url(r'^engsoft/', include('engsoft.foo.urls')),
     url(r'login/', "django.contrib.auth.views.login", {
            "template_name": "login.html"}),
     url(r'logout/', "django.contrib.auth.views.logout_then_login", {
            'login_url': "/login/"}),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/fotos/', include('django.contrib.admindocs.urls')),
    url(r'^admin/fotos(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),

    #url(r'^view_imagem/', 'sirius.views.view_imagem'),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

     #url para imagens
    url(r'^admin/fotos(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),

    url(r'form_pesquisa/$', 'siliqua.views.form_pesquisa'),
    url(r'^pesquisar/$', 'siliqua.views.pesquisar'),
    url(r'^pesquisar/decisao/(?P<id>[^\.]+).html', 'siliqua.views.view_decisao', name='view_decisao'),
    url(r'^pesquisar/padrao/(?P<id>[^\.]+).html', 'siliqua.views.view_padrao', name='view_padrao'),
    url(r'^pesquisar/tipo-padrao/(?P<id>[^\.]+).html', 'siliqua.views.view_tipo_padrao', name='view_tipo_padrao'),
    url(r'^pesquisar/tipo-decisao/(?P<id>[^\.]+).html', 'siliqua.views.view_tipo_decisao', name='view_tipo_decisao'),
    url(r'gerarpdfdecisao/$', 'siliqua.views.gerarpdfdecisao'),
    url(r'gerarpdfpadrao/$', 'siliqua.views.gerarpdfpadrao'),
    #url(r'^$', 'siliqua.views.home', name='home'),
    url(r'historico/$', 'siliqua.views.historico'),

    url(r'pesquisa/$', 'sirius.views.pesquisa'),
    url(r'form_pesquisa_sirius/$', 'sirius.views.form_pesquisa_sirius'),
    url(r'visualizar_documento/(?P<id>\d+)/$', 'sirius.views.visualizar_documento'),
    url(r'visualizar_documento2/(?P<id>\d+)/$', 'sirius.views.visualizar_documento2'),
    url(r'pesquisar_documento/$', 'sirius.views.pesquisar_documento'),
    url(r'pdf/(?P<id>\d+)/$', 'sirius.views.pdf'),
    #url(r'pdf2/(?P<id>\d+)/$', 'sirius.views.pdf2'),


)
