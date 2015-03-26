from django.contrib import admin

from canary.models import Projeto, Referencia, API, Tecnologia, AtributoDeQualidade, Funcional, NaoFuncional

class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Projeto)
# admin.site.register(Referencia)
admin.site.register(API)
admin.site.register(Tecnologia)
# admin.site.register(AtributoDeQualidade)
# admin.site.register(Funcional)
# admin.site.register(NaoFuncional)
