from django.contrib import admin
from siliqua.models import TipoPadrao, TipoDecisao, Padrao, Decisao, TagDecisao, TagPadrao

class TipoPadraoAdmin(admin.ModelAdmin):
    pass

class TipoDecisaoAdmin(admin.ModelAdmin):
    pass

class PadraoAdmin(admin.ModelAdmin):
    pass

class DecisaoAdmin(admin.ModelAdmin):
    pass

class TagDecisaoAdmin(admin.ModelAdmin):
    pass

class TagPadraoAdmin(admin.ModelAdmin):
    pass

admin.site.register(TipoPadrao)
admin.site.register(TipoDecisao)
admin.site.register(Padrao)
admin.site.register(Decisao)
admin.site.register(TagDecisao)
admin.site.register(TagPadrao)
