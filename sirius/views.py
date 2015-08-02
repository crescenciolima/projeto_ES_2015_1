from django.contrib.admin.models import LogEntry
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.template import Context
import ho.pisa as pisa
from django import http
import cStringIO as StringIO
import cgi, os
from django.http import HttpResponseRedirect, HttpResponse
from models import ModeloArquitetura, ModeloArquiteturaAvaliacao, Tecnologias, TradeOff, Diretriz, Referencia, \
    VisaoBehavioral, VisaoImplementacao, DescricaoVisaoAtual, Apresentacao, StakeHoldersBehavioral, StakeHoldersImplementacao, \
    ModuloCatalog, DiretrizesVariabilidade, ApresentacaoModulo, Estilo, AtributoDiretriz
from formulario import FormModeloArquitetura, FormReferenciaInline, FormTecnologiasInline, FormChoice

def visualizar_documento2(request, id):
    modeloarquiteturaavaliacao = get_object_or_404(ModeloArquiteturaAvaliacao, id=id)
    modeloarquitetura = get_object_or_404(ModuloCatalog, pk=modeloarquiteturaavaliacao.modeloArquitetura.id)
    lista_tradeoff = TradeOff.objects.filter(modeloArquitetura=modeloarquiteturaavaliacao.id)
    diretriz = get_object_or_404(Diretriz, pk=lista_tradeoff)
    lista_atributos_diretrizes = AtributoDiretriz.objects.filter(diretriz=diretriz.id)

    cliques = modeloarquiteturaavaliacao.cliques
    modeloarquiteturaavaliacao.cliques = cliques + 1
    modeloarquiteturaavaliacao.save()

    recomendacoes = ModeloArquiteturaAvaliacao.objects.order_by('-cliques').distinct()[:3]

    return render_to_response('visualizar-documento2.html', {
        'modelo': get_object_or_404(ModeloArquiteturaAvaliacao, id=id),
        'modelo2': modeloarquitetura,
        'lista_tradeoff': lista_tradeoff,
        'diretriz': diretriz,
        'lista_atributos_diretrizes': lista_atributos_diretrizes,
        'recomendacoes' : recomendacoes,

    })

def visualizar_documento(request, id):
    modeloarquitetura = get_object_or_404(ModeloArquitetura, id=id)

    cliques = modeloarquitetura.cliques
    modeloarquitetura.cliques = cliques + 1
    modeloarquitetura.save()

    recomendacoes = ModeloArquitetura.objects.order_by('-cliques').distinct()[:3]

    lista_referencia = Referencia.objects.filter(modeloArquitetura=id)
    lista_tecnologia = Tecnologias.objects.filter(modeloArquitetura=id)
    modulo_catalogo_apresentacao = get_object_or_404(ApresentacaoModulo, pk=modeloarquitetura.apresentacao_modulo.id)

    visao_coportamental = get_object_or_404(VisaoBehavioral, pk=modeloarquitetura.visao_comportamental.id)
    descricao_visao_atual = get_object_or_404(DescricaoVisaoAtual, pk=visao_coportamental.visao_atual.id)
    apresentacao_visao_comportamental = get_object_or_404(Apresentacao, pk=visao_coportamental.apresentacao_behavioral.id)
    diretrizes_variabilidade_comportamental = DiretrizesVariabilidade.objects.filter(apresentacao_behavioral=apresentacao_visao_comportamental.id)
    lista_stakeholders_comportamental = StakeHoldersBehavioral.objects.filter(visao_behavioral=visao_coportamental.id) #Verificar se essa chave esta sendo coletada de forma correta, talvez possa ta comparando com a id de ModeloArquitetura

    visao_de_implementacao = get_object_or_404(VisaoImplementacao, pk=modeloarquitetura.visao_de_implementacao.id)
    apresentacao_de_implementacao = get_object_or_404(Apresentacao, pk=visao_de_implementacao.apresentacao_de_implementacao.id)
    diretrizes_variabilidade_implementacao = DiretrizesVariabilidade.objects.filter(apresentacao_behavioral=apresentacao_de_implementacao.id)
    lista_stakeholders_implementacao = StakeHoldersImplementacao.objects.filter(visao_de_implementacao=visao_de_implementacao.id)

    visao_atual = get_object_or_404(DescricaoVisaoAtual, pk=modeloarquitetura.visao_atual.id)
    modulo_catalogo = get_object_or_404(ModuloCatalog, pk=modeloarquitetura.apresentacao_modulo.id)
    lista_estilo = Estilo.objects.filter(modeloArquitetura=id)
    diretriz = get_object_or_404(Diretriz, pk=modeloarquitetura.diretriz.id)
    lista_atributo_diretriz = AtributoDiretriz.objects.filter(diretriz=diretriz.id)

    return render_to_response('visualizar-documento.html', {
        'modelo': get_object_or_404(ModeloArquitetura, id=id),
        'lista_referencia': lista_referencia,
        'lista_tecnologia': lista_tecnologia,
        'visao_coportamental': visao_coportamental,
        'descricao_visao_atual': descricao_visao_atual,
        'apresentacao_visao_comportamental': apresentacao_visao_comportamental,
        'visao_de_implementacao': visao_de_implementacao,
        'lista_stakeholders_comportamental': lista_stakeholders_comportamental,
        'apresentacao_de_implementacao': apresentacao_de_implementacao,
        'lista_stakeholders_implementacao': lista_stakeholders_implementacao,
        'visao_atual': visao_atual,
        'modulo_catalogo': modulo_catalogo,
        'modulo_catalogo_apresentacao': modulo_catalogo_apresentacao,
        'diretrizes_variabilidade_comportamental': diretrizes_variabilidade_comportamental,
        'diretrizes_variabilidade_implementacao': diretrizes_variabilidade_implementacao,
        'lista_estilo': lista_estilo,
        'recomendacoes' : recomendacoes,
        "diretriz": diretriz,
        "lista_atributo_diretriz": lista_atributo_diretriz
    })

def pesquisa(request):
    return render(request, 'pesquisa.html')

def form_pesquisa_sirius(request):
    return render(request, 'form-pesquisa-sirius.html')

def pesquisar_documento(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        por = request.GET['por']
    if por == 'ModeloArquitetura':
        lista_documentos = ModeloArquitetura.objects.filter(nome__contains=q)
        recomendacoes = ModeloArquitetura.objects.order_by('-cliques')[:3]
        return render(request, 'documentos.html', {'lista_documentos': lista_documentos, 'query': q, 'recomendacoes':recomendacoes})
    if por == 'ModeloArquiteturaAvaliacao':
        lista_documentos = ModeloArquiteturaAvaliacao.objects.filter(nome__contains=q)
        recomendacoes = ModeloArquiteturaAvaliacao.objects.order_by('-cliques')[:3]
        return render(request, 'documento2.html', {'lista_documentos': lista_documentos, 'query': q, 'recomendacoes':recomendacoes})

@login_required
def index(request):
    return http.HttpResponseRedirect('http://127.0.0.1:8000/admin/')

def adiciona_documento(request):
    if request.method == "POST":
        choice_form = FormChoice(request.POST)
        item = choice_form.save(commit=False)
        if item.referencia_escolha:
            form = FormModeloArquitetura(request.POST, instance=ModeloArquitetura())
            rform = FormReferenciaInline(request.POST)
            tform = FormTecnologiasInline(request.POST)
            if form.is_valid() and rform.is_valid() and tform.is_valid():
                new_modelo = form.save(commit=False)
                new_referencia = rform.save(commit=False)
                new_tecnologia = tform.save(commit=False)
                new_modelo.save()
                new_tecnologia.modeloArquitetura = new_modelo
                new_referencia.modeloArquitetura = new_modelo
                new_referencia.save()
                new_tecnologia.save()
                return render(request, "aviso_salvo.html", {})
            else:
                form = FormModeloArquitetura(instance=ModeloArquitetura())
                rform = FormReferenciaInline(instance=ModeloArquitetura())
                tform = FormTecnologiasInline(instance=ModeloArquitetura())
                return render(request, "adiciona_documento.html", {"form": form, "rform": rform, "tform": tform},
                              context_instance=RequestContext(request))
        else:
            form = FormModeloArquitetura(request.POST, instance=ModeloArquitetura())
            tform = FormTecnologiasInline(request.POST)
            if form.is_valid() and tform.is_valid():
                new_modelo = form.save(commit=False)
                new_tecnologia = tform.save(commit=False)
                new_modelo.save()
                new_tecnologia.modeloArquitetura = new_modelo
                new_tecnologia.save()
                return render(request, "aviso_salvo.html", {})
            else:
                form = FormModeloArquitetura(instance=ModeloArquitetura())
                tform = FormTecnologiasInline(instance=ModeloArquitetura())
                return render(request, "adiciona_documento_noref.html", {"form": form, "tform": tform},
                              context_instance=RequestContext(request))
    else:
        choice_form = FormChoice()
        return render(request, "choice_ref.html", {"choice_form": choice_form},
                      context_instance=RequestContext(request))


def write_to_pdf(template_src, context_dict, filename):
    # Create the HttpResponse object with the appropriate PDF headers.
    # response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="notas.pdf"'
    #
    # # Create the PDF object, using the response object as its "file."
    # p = canvas.Canvas(response)
    #
    # # Draw things on the PDF. Here's where the PDF generation happens.
    # # See the ReportLab documentation for the full list of functionality.
    # p.drawCentredString(10, 10, "Relatorio de Notas")
    #
    # # Close the PDF object cleanly, and we're don.
    # p.showPage()
    # p.save()
    # return response
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

def pdf2(request,id):
    modeloarquiteturaavaliacao = get_object_or_404(ModeloArquiteturaAvaliacao, id=id)
    modeloarquitetura = get_object_or_404(ModuloCatalog, pk=modeloarquiteturaavaliacao.modeloArquitetura.id)
    lista_tradeoff = TradeOff.objects.filter(modeloArquitetura=modeloarquiteturaavaliacao.id)
    diretriz = get_object_or_404(Diretriz, pk=lista_tradeoff)
    lista_atributos_diretrizes = AtributoDiretriz.objects.filter(diretriz=diretriz.id)

    cliques = modeloarquiteturaavaliacao.cliques
    modeloarquiteturaavaliacao.cliques = cliques + 1
    modeloarquiteturaavaliacao.save()


    return write_to_pdf("pdf2.html", {
        "modelo": get_object_or_404(ModeloArquiteturaAvaliacao, id=id),
        "modelo2": modeloarquitetura,
        "lista_tradeoff": lista_tradeoff,
        "diretriz": diretriz,
        "lista_atributos_diretrizes": lista_atributos_diretrizes},"documento_pdf")


def pdf(request, id):
    modeloarquitetura = get_object_or_404(ModeloArquitetura, pk=id)
    lista_ferencia = Referencia.objects.filter(modeloArquitetura=id)
    lista_tecnologia = Tecnologias.objects.filter(modeloArquitetura=id)
    modulo_catalogo_apresentacao = get_object_or_404(ApresentacaoModulo, pk=modeloarquitetura.apresentacao_modulo.id)

    visao_coportamental = get_object_or_404(VisaoBehavioral, pk=modeloarquitetura.visao_comportamental.id)
    descricao_visao_atual = get_object_or_404(DescricaoVisaoAtual, pk=visao_coportamental.visao_atual.id)
    apresentacao_visao_comportamental = get_object_or_404(Apresentacao, pk=visao_coportamental.apresentacao_behavioral.id)
    diretrizes_variabilidade_comportamental = DiretrizesVariabilidade.objects.filter(apresentacao_behavioral=apresentacao_visao_comportamental.id)
    lista_stakeholders_comportamental = StakeHoldersBehavioral.objects.filter(visao_behavioral=visao_coportamental.id)

    visao_de_implementacao = get_object_or_404(VisaoImplementacao, pk=modeloarquitetura.visao_de_implementacao.id)
    apresentacao_de_implementacao = get_object_or_404(Apresentacao, pk=visao_de_implementacao.apresentacao_de_implementacao.id)
    diretrizes_variabilidade_implementacao = DiretrizesVariabilidade.objects.filter(apresentacao_behavioral=apresentacao_de_implementacao.id)
    lista_stakeholders_implementacao = StakeHoldersImplementacao.objects.filter(visao_de_implementacao=visao_de_implementacao.id)

    visao_atual = get_object_or_404(DescricaoVisaoAtual, pk=modeloarquitetura.visao_atual.id)
    modulo_catalogo = get_object_or_404(ModuloCatalog, pk=modeloarquitetura.apresentacao_modulo.id)
    lista_estilo = Estilo.objects.filter(modeloArquitetura=id)
    diretriz = get_object_or_404(Diretriz, pk=modeloarquitetura.diretriz.id)
    lista_atributo_diretriz = AtributoDiretriz.objects.filter(diretriz=diretriz.id)


    return write_to_pdf("pdf.html", {"modelo": modeloarquitetura, "lista_referencia": lista_ferencia,
                                     "lista_tecnologia": lista_tecnologia,
                                     "visao_coportamental": visao_coportamental,
                                     "descricao_visao_atual": descricao_visao_atual,
                                     "apresentacao_visao_comportamental": apresentacao_visao_comportamental,
                                     "visao_de_implementacao": visao_de_implementacao,
                                     "lista_stakeholders_comportamental": lista_stakeholders_comportamental,
                                     "apresentacao_de_implementacao": apresentacao_de_implementacao,
                                     "lista_stakeholders_implementacao": lista_stakeholders_implementacao,
                                     "visao_atual": visao_atual,
                                     "modulo_catalogo": modulo_catalogo,
                                     "modulo_catalogo_apresentacao": modulo_catalogo_apresentacao,
                                     "diretrizes_variabilidade_comportamental": diretrizes_variabilidade_comportamental,
                                     "diretrizes_variabilidade_implementacao": diretrizes_variabilidade_implementacao,
                                     "lista_estilo": lista_estilo,
                                     "diretriz": diretriz,
                                     "lista_atributo_diretriz": lista_atributo_diretriz}, "documento_pdf")
