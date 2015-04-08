#coding:utf-8

from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from models import Decisao, Padrao, TipoDecisao, TipoPadrao
from django import http
from django.template.loader import get_template
from django.template import Context
import ho.pisa as pisa
import cStringIO as StringIO
import cgi

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
    return HttpResponse('Por favor envie um termo para pesquisa.')


def view_decisao(request, id):
    return render_to_response('view_decisao.html', {
        'decisao': get_object_or_404(Decisao, id=id)
    })

def view_padrao(request, id):
    return render_to_response('view_padrao.html', {
        'padrao': get_object_or_404(Padrao, id=id)
    })

def view_tipo_padrao(request, id):
    tipopadrao = get_object_or_404(TipoPadrao, id=id)
    return render_to_response('view_tipo_padrao.html', {
        'padroes': Padrao.objects.filter(tipoDePadrao=tipopadrao)
    })

def view_tipo_decisao(request, id):
    tipodecisao = get_object_or_404(TipoDecisao, id=id)
    return render_to_response('view_tipo_decisao.html', {
        'decisoes': Decisao.objects.filter(tipoDeDecisao=tipodecisao)
    })


def write_to_pdf(template_src, context_dict, filename):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
    if not pdf.err:
        response = http.HttpResponse(mimetype='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=%s.pdf' % filename
        response.write(result.getvalue())
        return response
    return http.HttpResponse('Problema ao gerar PDF: %s' % cgi.escape(html))

def gerarpdfdecisao(request):
    id = request.GET['id']
    decisao = get_object_or_404(Decisao, id=id)
    return write_to_pdf('templatepdfdecisao.html', {'decisao': decisao}, 'relatorio_decisao')

def gerarpdfpadrao(request):
    id = request.GET['id']
    padrao = get_object_or_404(Padrao, id=id)
    return write_to_pdf('templatepdfpadrao.html', {'padrao': padrao}, 'relatorio_padrao')
