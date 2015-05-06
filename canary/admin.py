# -*- coding: utf-8 -*-
from django.contrib import admin
from django.forms import forms
from canary.models import Projeto, Referencia, API, Tecnologia, AtributoDeQualidade, Funcional, NaoFuncional, Elemento, PontoDeVista
from django.http import HttpResponseRedirect

nomeCampo1 = ""
nomeCampo2 = ""
choicesCampo1 = ""
choicesCampo2 = ""
projetoId = 0


class ReferenciaInline(admin.TabularInline):
    model = Referencia
    extra = 0

class ReqFuncInline(admin.TabularInline):
    model = Funcional
    extra = 0

class ReqNaoFuncInline(admin.StackedInline):
    model = NaoFuncional
    extra = 0

class AttrQualidadeInline(admin.TabularInline):
    model = AtributoDeQualidade
    # extra = 0

class PontoDeVistaInline(admin.StackedInline):
    model = PontoDeVista
    extra = 0

class ProjetoAdmin(admin.ModelAdmin):
    model = Projeto
    fieldsets = (
        ("Informações Iniciais", {
            'fields': ('nome', 'descricao', 'introducao', 'objetivo')
        }),
        ("Informações Adicionais", {
            'fields': ('autores', 'tecnologias')
        }),
        ("Relação entre atributos", {
            'fields': ('relacao1', 'relacao2', 'fator')
        })
    )
    inlines = [ReferenciaInline, ReqFuncInline, ReqNaoFuncInline, PontoDeVistaInline]

    def response_add(self, request, obj, post_url_continue=None):


        global nomeCampo1
        nomeCampo1 = obj.relacao1
        global nomeCampo2
        nomeCampo2 = obj.relacao2

        global choicesCampo1
        global choicesCampo2

        global projetoId
        projetoId = obj.id

        if(obj.fator == '1'):
            choicesCampo1 = "4"
            choicesCampo2 = "3"
        if(obj.fator == '2'):
            choicesCampo1 = "4"
            choicesCampo2 = "2"
        if(obj.fator == '3'):
            choicesCampo1 = "4"
            choicesCampo2 = "1"
        if(obj.fator == '4'):
            choicesCampo1 = "4"
            choicesCampo2 = "0"

        return HttpResponseRedirect('/admin/canary/atributodequalidade/add/')




class AtributoDeQualidadeAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(AtributoDeQualidadeAdmin, self).get_form(request, obj, **kwargs)

        if(choicesCampo1 != ""):
            form.base_fields[nomeCampo1].initial = choicesCampo1
            #form.base_fields[nomeCampo1].widget.attrs['readonly'] = 'readonly'
        
        if(choicesCampo2 != ""):
            form.base_fields[nomeCampo2].initial = choicesCampo2
            #form.base_fields[nomeCampo2].widget.attrs['readonly'] = 'readonly'

        if(projetoId != 0):
            form.base_fields['projeto'].initial = projetoId
            #form.base_fields['projeto'].widget.attrs['readonly'] = 'readonly'

        return form



admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(API)
admin.site.register(Tecnologia)
admin.site.register(Elemento)
admin.site.register(AtributoDeQualidade, AtributoDeQualidadeAdmin)
# admin.site.register(PontoDeVista)
