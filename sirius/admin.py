from sirius.models import ModeloArquitetura,ModeloArquiteturaAvaliacao,Tecnologias,Referencia,TradeOff,Diretriz
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
    search_fildes = ['nome']
    inlines = [TecnologiaInline, ReferenciaInline]
    save_on_top =True

admin.site.register(ModeloArquitetura, ModeloArquiteturaAdmin)
