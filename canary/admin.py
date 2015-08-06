# -*- coding: utf-8 -*-
from django.contrib import admin
from django.forms import forms
from canary.models import *
from django.http import HttpResponseRedirect

from canary.models import *
nomeCampo1 = ""
nomeCampo2 = ""
nomeCampo3 = ""
nomeCampo4 = ""
nomeCampo5 = ""
nomeCampo6 = ""
choicesCampo1 = ""
choicesCampo2 = ""
choicesCampo3 = ""
choicesCampo4 = ""
choicesCampo5 = ""
choicesCampo6 = ""
projetoId = 0
qtdRelacoes = ""

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

class AvaliacaoInline(admin.StackedInline):
    model = ModeloArquiteturaAvaliacao
    extra = 0

class ProjetoAdmin(admin.ModelAdmin):
    model = Arquitetura
    search_fields = ['nome']
    list_display = ['nome', 'preview']
    fieldsets = (
        ("Informações Iniciais", {
            'fields': ('nome', 'descricao', 'introducao', 'objetivo')
        }),
        ("Informações Adicionais", {
            'fields': ('autores', 'tecnologias')
        }),
        ("Informações Iniciais dos Cenários de Qualidade", {
            'fields': ('introducao_qualidade','referencias_qualidade')
        }),
        ("Atributos de qualidade", {
            'fields': ('qtdrelacoes',)
        })
    )

    inlines = [ReferenciaInline, ReqFuncInline, ReqNaoFuncInline, PontoDeVistaInline, AvaliacaoInline]

    def response_add(self, request, obj, post_url_continue=None):

        global projetoId
        projetoId = obj.id

        global qtdRelacoes
        qtdRelacoes = obj.qtdrelacoes

        if(obj.qtdrelacoes == '1'):
            return HttpResponseRedirect('/admin/canary/relacionamento2/add/')
        if(obj.qtdrelacoes == '2'):
            return HttpResponseRedirect('/admin/canary/relacionamento4/add/')
        if(obj.qtdrelacoes == '3'):
            return HttpResponseRedirect('/admin/canary/relacionamento6/add/')




class AtributoDeQualidadeAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(AtributoDeQualidadeAdmin, self).get_form(request, obj, **kwargs)


        if(qtdRelacoes == '1'):
            if(choicesCampo1 != ""):
                form.base_fields[nomeCampo1].initial = choicesCampo1
                #form.base_fields[nomeCampo1].widget.attrs['readonly'] = 'readonly'

            if(choicesCampo2 != ""):
                form.base_fields[nomeCampo2].initial = choicesCampo2
                #form.base_fields[nomeCampo2].widget.attrs['readonly'] = 'readonly'

            if(projetoId != 0):
                form.base_fields['arquitetura'].initial = projetoId
                #form.base_fields['projeto'].widget.attrs['readonly'] = 'readonly'

        if(qtdRelacoes == '2'):
            if(choicesCampo1 != ""):
                form.base_fields[nomeCampo1].initial = choicesCampo1
                #form.base_fields[nomeCampo1].widget.attrs['readonly'] = 'readonly'

            if(choicesCampo2 != ""):
                form.base_fields[nomeCampo2].initial = choicesCampo2
                #form.base_fields[nomeCampo2].widget.attrs['readonly'] = 'readonly'

            if(choicesCampo3 != ""):
                form.base_fields[nomeCampo3].initial = choicesCampo3
                #form.base_fields[nomeCampo1].widget.attrs['readonly'] = 'readonly'

            if(choicesCampo4 != ""):
                form.base_fields[nomeCampo4].initial = choicesCampo4
                #form.base_fields[nomeCampo2].widget.attrs['readonly'] = 'readonly'

            if(projetoId != 0):
                form.base_fields['arquitetura'].initial = projetoId
                #form.base_fields['projeto'].widget.attrs['readonly'] = 'readonly'

        if(qtdRelacoes == '3'):
            if(choicesCampo1 != ""):
                form.base_fields[nomeCampo1].initial = choicesCampo1
                #form.base_fields[nomeCampo1].widget.attrs['readonly'] = 'readonly'

            if(choicesCampo2 != ""):
                form.base_fields[nomeCampo2].initial = choicesCampo2
                #form.base_fields[nomeCampo2].widget.attrs['readonly'] = 'readonly'

            if(choicesCampo3 != ""):
                form.base_fields[nomeCampo3].initial = choicesCampo3
                #form.base_fields[nomeCampo1].widget.attrs['readonly'] = 'readonly'

            if(choicesCampo4 != ""):
                form.base_fields[nomeCampo4].initial = choicesCampo4
                #form.base_fields[nomeCampo2].widget.attrs['readonly'] = 'readonly'

            if(choicesCampo5 != ""):
                form.base_fields[nomeCampo5].initial = choicesCampo5
                #form.base_fields[nomeCampo1].widget.attrs['readonly'] = 'readonly'

            if(choicesCampo6 != ""):
                form.base_fields[nomeCampo6].initial = choicesCampo6
                #form.base_fields[nomeCampo2].widget.attrs['readonly'] = 'readonly'

            if(projetoId != 0):
                form.base_fields['arquitetura'].initial = projetoId
                #form.base_fields['projeto'].widget.attrs['readonly'] = 'readonly'


        return form


class Relacionamento2Admin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(Relacionamento2Admin, self).get_form(request, obj, **kwargs)

        if(projetoId != 0):
           form.base_fields['projeto'].initial = projetoId

        return form

    def response_add(self, request, obj, post_url_continue=None):

        global nomeCampo1, nomeCampo2, choicesCampo1, choicesCampo2

        nomeCampo1 = obj.relacao1
        nomeCampo2 = obj.relacao2

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


class Relacionamento4Admin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(Relacionamento4Admin, self).get_form(request, obj, **kwargs)

        if(projetoId != 0):
           form.base_fields['projeto'].initial = projetoId

        return form

    def response_add(self, request, obj, post_url_continue=None):

        global nomeCampo1, nomeCampo2, nomeCampo3, nomeCampo4, choicesCampo1, choicesCampo2, choicesCampo3, choicesCampo4

        nomeCampo1 = obj.relacao1
        nomeCampo2 = obj.relacao2
        nomeCampo3 = obj.relacao3
        nomeCampo4 = obj.relacao4

        if(obj.fator1 == '1'):
            choicesCampo1 = "4"
            choicesCampo2 = "3"
        if(obj.fator1 == '2'):
            choicesCampo1 = "4"
            choicesCampo2 = "2"
        if(obj.fator1 == '3'):
            choicesCampo1 = "4"
            choicesCampo2 = "1"
        if(obj.fator1 == '4'):
            choicesCampo1 = "4"
            choicesCampo2 = "0"

        if(obj.fator2 == '1'):
            choicesCampo3 = "4"
            choicesCampo4 = "3"
        if(obj.fator2 == '2'):
            choicesCampo3 = "4"
            choicesCampo4 = "2"
        if(obj.fator2 == '3'):
            choicesCampo3 = "4"
            choicesCampo4 = "1"
        if(obj.fator2 == '4'):
            choicesCampo3 = "4"
            choicesCampo4 = "0"

        return HttpResponseRedirect('/admin/canary/atributodequalidade/add/')



class Relacionamento6Admin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(Relacionamento6Admin, self).get_form(request, obj, **kwargs)

        if(projetoId != 0):
           form.base_fields['projeto'].initial = projetoId

        return form

    def response_add(self, request, obj, post_url_continue=None):

        global nomeCampo1, nomeCampo2, nomeCampo3, nomeCampo4, nomeCampo5, nomeCampo6, choicesCampo1, choicesCampo2, choicesCampo3, choicesCampo4, choicesCampo5, choicesCampo6

        nomeCampo1 = obj.relacao1
        nomeCampo2 = obj.relacao2
        nomeCampo3 = obj.relacao3
        nomeCampo4 = obj.relacao4
        nomeCampo5 = obj.relacao5
        nomeCampo6 = obj.relacao6

        if(obj.fator1 == '1'):
            choicesCampo1 = "4"
            choicesCampo2 = "3"
        if(obj.fator1 == '2'):
            choicesCampo1 = "4"
            choicesCampo2 = "2"
        if(obj.fator1 == '3'):
            choicesCampo1 = "4"
            choicesCampo2 = "1"
        if(obj.fator1 == '4'):
            choicesCampo1 = "4"
            choicesCampo2 = "0"

        if(obj.fator2 == '1'):
            choicesCampo3 = "4"
            choicesCampo4 = "3"
        if(obj.fator2 == '2'):
            choicesCampo3 = "4"
            choicesCampo4 = "2"
        if(obj.fator2 == '3'):
            choicesCampo3 = "4"
            choicesCampo4 = "1"
        if(obj.fator2 == '4'):
            choicesCampo3 = "4"
            choicesCampo4 = "0"

        if(obj.fator3 == '1'):
            choicesCampo5 = "4"
            choicesCampo6 = "3"
        if(obj.fator3 == '2'):
            choicesCampo5 = "4"
            choicesCampo6 = "2"
        if(obj.fator3 == '3'):
            choicesCampo5 = "4"
            choicesCampo6 = "1"
        if(obj.fator3 == '4'):
            choicesCampo5 = "4"
            choicesCampo6 = "0"

        return HttpResponseRedirect('/admin/canary/atributodequalidade/add/')



admin.site.register(Arquitetura, ProjetoAdmin)
admin.site.register(API)
admin.site.register(Tecnologia)
admin.site.register(Elemento)
admin.site.register(VisaoComportamental)
admin.site.register(VisaoEstrutural)
admin.site.register(Modulo)
admin.site.register(Componente)
admin.site.register(ClassificacaoMetricaAvaliacao)
admin.site.register(Relacionamento2, Relacionamento2Admin)
admin.site.register(Relacionamento4, Relacionamento4Admin)
admin.site.register(Relacionamento6, Relacionamento6Admin)
admin.site.register(AtributoDeQualidade, AtributoDeQualidadeAdmin)
# admin.site.register(PontoDeVista)
