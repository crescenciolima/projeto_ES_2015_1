# -*- coding: utf-8 -*-
from django.contrib import admin

from canary.models import Projeto, Referencia, API, Tecnologia, AtributoDeQualidade, Funcional, NaoFuncional

class ReferenciaInline(admin.TabularInline):
    model = Referencia
    extra = 0

class ReqFuncInline(admin.TabularInline):
    model = Funcional
    extra = 0

class ReqNaoFuncInline(admin.TabularInline):
    model = NaoFuncional
    extra = 0

class AttrQualidadeInline(admin.TabularInline):
    model = AtributoDeQualidade
    # extra = 0

class ProjetoAdmin(admin.ModelAdmin):
    model = Projeto
    fieldsets = (
        ("Informações Iniciais", {
            'fields': ('nome', 'descricao', 'introducao', 'objetivo')
        }),
        ("Informações Adicionais", {
            'fields': ('autores', 'tecnologias')
        })
    )
    inlines = [ReferenciaInline, ReqFuncInline, ReqNaoFuncInline, AttrQualidadeInline]

admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(API)
admin.site.register(Tecnologia)
