from sirius.models import ModeloArquitetura,ModeloArquiteturaAvaliacao,Tecnologias,Referencia,TradeOff,Diretriz, VistaBehavioral, VerDescricao,StakeHolders, ApresentacaoBehavioral, DiretrizesVariabilidade, Estilo, ModuloCatalog, ComponenteModulo, ApresentacaoModulo
from django.contrib import admin


class TecnologiaInline(admin.TabularInline):
    model = Tecnologias
    extra = 1


class ReferenciaInline(admin.TabularInline):
    model = Referencia
    extra = 0


class ModeloArquiteturaAdmin(admin.ModelAdmin):
    model = ModeloArquitetura
    list_display = ['nome', 'introducao']
    search_fields = ['nome']
    inlines = [TecnologiaInline, ReferenciaInline]
    save_on_top = True
    exclude = ['referencia_escolha']

class ComponenteModuloInline(admin.TabularInline):
    model = ComponenteModulo
    extra = 0

class ModuloCatalogAdmin(admin.ModelAdmin):
    model = ModuloCatalog
    inlines = [ComponenteModuloInline]
    save_on_top = True

class ApresentacaoModuloAdmin(admin.ModelAdmin):
    model = ApresentacaoModulo
    extra = 0

class TradeOffInline(admin.TabularInline):
    model = TradeOff
    extra = 1

class DiretrizAdmin(admin.ModelAdmin):
    model = Diretriz
    extra = 2

class EstiloInline(admin.TabularInline):
    model = Estilo
    extra = 1

class ModeloArquiteturaAvaliacaoAdmin(admin.ModelAdmin):
    model = ModeloArquiteturaAvaliacao
    list_display = ['desc_qualidade', 'desc_ponto_sensibilidade', 'desc_nao_riscos', 'desc_riscos',
                    'desc_arquitetura_texto', 'desc_arquitetura', 'desc_pricipais_abordagens_arquitetura',
                    'desc_restricao_sensibilidade']
    search_fields = ['nome']
    inlines = [TradeOffInline, EstiloInline]
    save_on_top = True

class VistaBehavioralAdmin(admin.ModelAdmin):
    model = VistaBehavioral
    extra = 1

class DiretrizesVariabilidadeInline(admin.TabularInline):
    model = DiretrizesVariabilidade
    extra = 1

class ApresentacaoBehavioralAdmin(admin.ModelAdmin):
    model = ApresentacaoBehavioral
    inlines = [DiretrizesVariabilidadeInline]
    extra = 1

class StakeHoldersInline(admin.TabularInline):
    model = StakeHolders
    extra = 1

class VerDescricaoAdmin(admin.ModelAdmin):
    model = VerDescricao
    inlines = [StakeHoldersInline]
    extra = 1

admin.site.register(ModeloArquitetura, ModeloArquiteturaAdmin)
admin.site.register(ModeloArquiteturaAvaliacao, ModeloArquiteturaAvaliacaoAdmin)
admin.site.register(Diretriz, DiretrizAdmin)
admin.site.register(VistaBehavioral, VistaBehavioralAdmin)
admin.site.register(ApresentacaoBehavioral, ApresentacaoBehavioralAdmin)
admin.site.register(VerDescricao, VerDescricaoAdmin)
admin.site.register(ModuloCatalog, ModuloCatalogAdmin)
admin.site.register(ApresentacaoModulo, ApresentacaoModuloAdmin)