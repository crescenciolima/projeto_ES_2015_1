from django.contrib import admin
from siliqua.models import TipoPadrao, TipoDecisao, Padrao, Decisao

class TipoPadraoAdmin(admin.ModelAdmin):
    pass

class TipoDecisaoAdmin(admin.ModelAdmin):
    pass

class PadraoAdmin(admin.ModelAdmin):
    pass

class DecisaoAdmin(admin.ModelAdmin):
    pass

admin.site.register(TipoPadrao)
admin.site.register(TipoDecisao)
admin.site.register(Padrao)
admin.site.register(Decisao)