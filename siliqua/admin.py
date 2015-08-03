from django.contrib import admin
from siliqua.models import TipoPadrao, TipoDecisao, Padrao, Decisao, TagDecisao, TagPadrao

class TipoPadraoAdmin(admin.ModelAdmin):
    pass

class TipoDecisaoAdmin(admin.ModelAdmin):
    pass

class PadraoAdmin(admin.ModelAdmin):
     filter_horizontal = ('padroesRelacionados','categorias')

class DecisaoAdmin(admin.ModelAdmin):
    filter_horizontal = ('decisaoRelacionada','categorias','padraoUtilizado')

class TagDecisaoAdmin(admin.ModelAdmin):
    pass

class TagPadraoAdmin(admin.ModelAdmin):
    pass

admin.site.register(TipoPadrao)
admin.site.register(TipoDecisao)
admin.site.register(Padrao, PadraoAdmin)
admin.site.register(Decisao, DecisaoAdmin)
admin.site.register(TagDecisao)
admin.site.register(TagPadrao)
