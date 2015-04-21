#coding:utf-8

from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from models import Decisao, Padrao, TipoDecisao, TipoPadrao
from django.contrib.admin.models import LogEntry, ContentType
from django.contrib.auth.models import User
from django import http
from django.template.loader import get_template
from django.template import Context
import ho.pisa as pisa
import cStringIO as StringIO
import cgi, sqlite3
from django.contrib.auth.decorators import login_required

@login_required(login_url='/admin')
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
        recomendacoes = Padrao.objects.order_by('-cliques')[:3]
        return render(request, 'resutado_padrao.html', {'padroes': padroes, 'query': q, 'recomendacoes':recomendacoes})
    if por == 'tipdecisao':
        tiposdecisoes = TipoDecisao.objects.filter(nome__contains=q)
        recomendacoes = TipoDecisao.objects.order_by('-cliques')[:3]
        return render(request, 'resultado_tipodecisao.html', {'tiposdecisoes': tiposdecisoes, 'query': q, 'recomendacoes': recomendacoes})
    if por == 'tippadrao':
        tipospadroes = TipoPadrao.objects.filter(nome__contains=q)
        recomendacoes = TipoPadrao.objects.order_by('-cliques')[:3]
        return render(request, 'resultado_tipopadrao.html', {'tipospadroes': tipospadroes, 'query': q, 'recomendacoes':recomendacoes})


def view_decisao(request, id):
    decisao = get_object_or_404(Decisao, id=id)
    content = ContentType.objects.get_for_model(decisao)
    cliques = decisao.cliques
    decisao.cliques = cliques + 1
    decisao.save()
    tags = decisao.categorias.all()
    recomendacoes = Decisao.objects.filter(categorias__in=tags).order_by('-cliques').distinct()[:6]
    return render_to_response('view_decisao.html', {
        'decisao': get_object_or_404(Decisao, id=id),
        'historicos' : LogEntry.objects.filter(content_type_id=content.id),
        'recomendacoes' : recomendacoes
    })

def view_padrao(request, id):
    padrao = get_object_or_404(Padrao, id=id)
    cliques = padrao.cliques
    padrao.cliques = cliques + 1
    padrao.save()
    tags = padrao.categorias.all()
    recomendacoes = Padrao.objects.filter(categorias__in=tags).order_by('-cliques').distinct()[:6]
    return render_to_response('view_padrao.html', {
        'padrao': get_object_or_404(Padrao, id=id),
        'recomendacoes':recomendacoes
    })

def view_tipo_padrao(request, id):
    tipopadrao = get_object_or_404(TipoPadrao, id=id)
    cliques = tipopadrao.cliques
    tipopadrao.cliques = cliques + 1
    tipopadrao.save()
    return render_to_response('view_tipo_padrao.html', {
        'padroes': Padrao.objects.filter(tipoDePadrao=tipopadrao)
    })

def view_tipo_decisao(request, id):
    tipodecisao = get_object_or_404(TipoDecisao, id=id)
    cliques = tipodecisao.cliques
    tipodecisao.cliques = cliques + 1
    tipodecisao.save()
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


@login_required(login_url='/admin')
def home(request):
    return http.HttpResponseRedirect('http://127.0.0.1:8000/admin/')

def historico(request):
    id = request.GET['id']
    decisao = get_object_or_404(Decisao, id=id)
    content = ContentType.objects.get_for_model(decisao)
    historicos = LogEntry.objects.filter(content_type_id=content.id, object_id=id)
    userList = []
    for historico in historicos:
        usuario = get_object_or_404(User, id = historico.user_id)
        userList.append(usuario)

    return render_to_response('view_historico.html', {
        'historicos' : historicos, 'usuarios' : userList
    })