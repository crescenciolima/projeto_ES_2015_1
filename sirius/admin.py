from sirius.models import ModeloArquitetura, ModeloArquiteturaAvaliacao, Tecnologias, Referencia, TradeOff, Diretriz, \
    VisaoBehavioral, DescricaoVisaoAtual, StakeHoldersImplementacao, StakeHoldersBehavioral, Apresentacao, \
    DiretrizesVariabilidade, Estilo, ModuloCatalog,  VisaoImplementacao, ComponenteModulo, ApresentacaoModulo, AtributoDiretriz
from django.contrib import admin

class TecnologiaInline(admin.TabularInline):
    model = Tecnologias
    extra = 1

class ReferenciaInline(admin.TabularInline):
    model = Referencia
    extra = 0

class EstiloInline(admin.TabularInline):
    model = Estilo
    extra = 1

class ModeloArquiteturaAdmin(admin.ModelAdmin):
    model = ModeloArquitetura
    list_display = ['nome', 'introducao']
    search_fields = ['nome']
    inlines = [TecnologiaInline, ReferenciaInline, EstiloInline]
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

class TradeOffInline(admin.TabularInline):
    model = TradeOff
    extra = 1

class AtributoDiretrizInline(admin.TabularInline):
    model = AtributoDiretriz
    extra = 1

class DiretrizAdmin(admin.ModelAdmin):
    model = Diretriz
    inlines = [AtributoDiretrizInline]

class ModeloArquiteturaAvaliacaoAdmin(admin.ModelAdmin):
    model = ModeloArquiteturaAvaliacao
    list_display = ['descricao_da_qualidade', 'descricao_de_nao_riscos', 'descricao_de_riscos',
                    'descricao_da_arquitetura', 'ponto_de_sensibilidade', 'restricao_de_sensibilidade']
    search_fields = ['descricao_da_arquitetura']
    inlines = [TradeOffInline]
    save_on_top = True

class StakeHoldersImplementacaoInline(admin.TabularInline):
    model = StakeHoldersImplementacao
    extra = 1

class StakeHoldersBehavioralInline(admin.TabularInline):
    model = StakeHoldersBehavioral
    extra = 1

class VisaoBehavioralAdmin(admin.ModelAdmin):
    model = VisaoBehavioral
    inlines = [StakeHoldersBehavioralInline]

class VisaoImplementacaoAdmin(admin.ModelAdmin):
    model = VisaoImplementacao
    inlines = [StakeHoldersImplementacaoInline]

class DiretrizesVariabilidadeInline(admin.TabularInline):
    model = DiretrizesVariabilidade
    extra = 1

class ApresentacaoAdmin(admin.ModelAdmin):
    model = Apresentacao
    inlines = [DiretrizesVariabilidadeInline]
    extra = 1

class DescricaoVisaoAtualAdmin(admin.ModelAdmin):
    model = DescricaoVisaoAtual
    extra = 1

admin.site.register(ModeloArquitetura, ModeloArquiteturaAdmin)
admin.site.register(ModeloArquiteturaAvaliacao, ModeloArquiteturaAvaliacaoAdmin)
admin.site.register(Diretriz, DiretrizAdmin)
admin.site.register(VisaoBehavioral, VisaoBehavioralAdmin)
admin.site.register(Apresentacao, ApresentacaoAdmin)
admin.site.register(DescricaoVisaoAtual, DescricaoVisaoAtualAdmin)
admin.site.register(VisaoImplementacao, VisaoImplementacaoAdmin)
admin.site.register(ModuloCatalog, ModuloCatalogAdmin)
admin.site.register(ApresentacaoModulo, ApresentacaoModuloAdmin)