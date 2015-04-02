#coding:utf-8

from django.shortcuts import render
from django.http import HttpResponse
from models import Decisao, Padrao, TipoDecisao, TipoPadrao

def form_pesquisa(request):
    return render(request, 'form-pesquisa.html')


def pesquisar(request):
   if 'q' in request.GET and request.GET['q']:
    q = request.GET['q']
    por = request.GET['por']
    if por == 'decisao':
     decisoes = Decisao.objects.filter(nome__contains=q)
     return render(request, 'resultado-decisao.html', {'decisoes': decisoes, 'query': q})
    if por == 'padrao':
     padroes = Padrao.objects.filter(nome__contains=q)
     return render(request, 'resutado_padrao.html', {'padroes': padroes, 'query': q})
    if por == 'tipdecisao':
     tiposdecisoes = TipoDecisao.objects.filter(nome__contains=q)
     return render(request, 'resultado_tipodecisao.html', {'tiposdecisoes': tiposdecisoes, 'query': q})
    if por == 'tippadrao':
     tipospadroes = TipoPadrao.objects.filter(nome__contains=q)
     return render(request, 'resultado_tipopadrao.html', {'tipospadroes': tipospadroes, 'query': q})
   else:
    return HttpResponse('Please submit a search term.')