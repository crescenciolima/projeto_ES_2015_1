from sirius.models import ModeloArquitetura, ModeloArquiteturaAvaliacao, Tecnologias, Referencia, TradeOff, Diretriz
from django.contrib import admin

class TecnologiaInline(admin.TabularInline):
    model = Tecnologias
    extra = 1

class ReferenciaInline(admin.TabularInline):
    model = Referencia
    extra = 0

class ModeloArquiteturaAdmin(admin.ModelAdmin):
    model = ModeloArquitetura
    list_display = ['nome','introducao']
    search_fields = ['nome']
    inlines = [TecnologiaInline, ReferenciaInline]
    save_on_top = True
    exclude = ['referencia_escolha']

class TradeOffInline(admin.TabularInline):
    model = TradeOff
    extra = 1

class DiretrizAdmin(admin.ModelAdmin):
    model = Diretriz
    extra = 1

class ModeloArquiteturaAvaliacaoAdmin(admin.ModelAdmin):
    model = ModeloArquitetura
    list_display = ['desc_qualidade', 'desc_ponto_sensibilidade', 'desc_nao_riscos', 'desc_riscos', 'desc_arquitetura_texto', 'desc_arquitetura', 'desc_pricipais_abordagens_arquitetura', 'desc_restricao_sensibilidade']
    search_fields = ['nome']
    inlines = [TradeOffInline]
    save_on_top =True

admin.site.register(ModeloArquitetura, ModeloArquiteturaAdmin)
admin.site.register(ModeloArquiteturaAvaliacao, ModeloArquiteturaAvaliacaoAdmin)
admin.site.register(Diretriz, DiretrizAdmin)