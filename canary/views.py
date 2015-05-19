from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from models import *
from django import http
from django.template.loader import get_template
from django.template import Context
import ho.pisa as pisa
import cStringIO as StringIO
import cgi, sqlite3
from django.contrib.auth.decorators import login_required

def view_api(request, id):
    return render_to_response('view_api.html', {
            'api': get_object_or_404(API, id=id)
    })

def view_arquitetura(request, id):
    return render_to_response('view_arquitetura.html', {
            'arquitetura': get_object_or_404(Arquitetura, id=id)
    })

def view_componente(request, id):
    return render_to_response('view_componente.html', {
            'componente': get_object_or_404(Componente, id=id)
    })

def view_elemento(request, id):
    return render_to_response('view_elemento.html', {
            'elemento': get_object_or_404(Elemento, id=id)
    })

def view_modulo(request, id):
    return render_to_response('view_modulo.html', {
            'modulo': get_object_or_404(Modulo, id=id)
    })

def view_tecnologia(request, id):
    return render_to_response('view_tecnologia.html', {
            'tecnologia': get_object_or_404(Tecnologia, id=id)
    })

def view_visao_comp(request, id):
    return render_to_response('view_visao_comp.html', {
            'visao_comp': get_object_or_404(VisaoComportamental, id=id)
    })

def view_visao_est(request, id):
    return render_to_response('view_visao_est.html', {
            'visao_est': get_object_or_404(VisaoEstrutural, id=id)
    })

def write_to_pdf(template_src, context_dict, filename):
    template = get_template(template_src)
    context = Context(context_dict)
    html = template.render(context)
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
    if not pdf.err:
        response = http.HttpResponse(mimetype='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=%s.pdf' % filename
        response.write(result.getvalue())
        return response
    return http.HttpResponse('Problema ao gerar PDF: %s' % cgi.escape(html))

def gerar_pdf(request, id, pdf=''):
    projeto = get_object_or_404(Arquitetura, pk=id)
    referencias = Referencia.objects.filter(projeto=id)
    atributoDeQualidade = AtributoDeQualidade.objects.filter(projeto=id)
    featuresFuncionais = NaoFuncional.objects.filter(projeto=id)
    featuresNaoFuncionais = Funcional.objects.filter(projeto=id)
    pontosDeVista = PontoDeVista.objects.filter(projeto=id)

    if(pdf == ''):
        return render_to_response('canary/pdf_projeto.html', {'arquitetura': projeto, 'referencias': referencias,
                            'atributoDeQualidade': atributoDeQualidade, 'featuresFuncionais': featuresFuncionais,
                            'featuresNaoFuncionais': featuresNaoFuncionais, 'pontosDeVista': pontosDeVista, 'link_to_pdf': True})
    else:
        return write_to_pdf('canary/pdf_projeto.html', {'arquitetura': projeto, 'referencias': referencias,
                            'atributoDeQualidade': atributoDeQualidade, 'featuresFuncionais': featuresFuncionais,'featuresNaoFuncionais': featuresNaoFuncionais, 'pontosDeVista': pontosDeVista
    }, 'projeto_'+projeto.nome)
