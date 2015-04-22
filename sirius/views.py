from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.template import Context
import ho.pisa as pisa
from django import http
import cStringIO as StringIO
import cgi, os
from django.http import HttpResponseRedirect, HttpResponse
from models import ModeloArquitetura, ModeloArquiteturaAvaliacao, Tecnologias, TradeOff, Diretriz, Referencia, \
    VisaoBehavioral, VisaoImplementacao, DescricaoVisaoAtual, Apresentacao, StakeHoldersBehavioral, StakeHoldersImplementacao, ModuloCatalog, DiretrizesVariabilidade, ApresentacaoModulo, Estilo
from formulario import FormModeloArquitetura, FormReferenciaInline, FormTecnologiasInline, FormChoice

@login_required
def index(request):
    lista_documentos = ModeloArquitetura.objects.filter(usuario=request.user)

    return render(request, "documentos.html",
                  {"lista_documentos": lista_documentos}, context_instance=RequestContext(request))


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
    # # Close the PDF object cleanly, and we're done.
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

def pdf(request, id):
    modeloarquitetura = get_object_or_404(ModeloArquitetura, pk=id)
    lista_ferencia = Referencia.objects.filter(modeloArquitetura=id)
    lista_tecnologia = Tecnologias.objects.filter(modeloArquitetura=id)

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
    modulo_catalogo_apresentacao = get_object_or_404(ApresentacaoModulo, pk=modeloarquitetura.modulo_catalog.id)
    lista_modulo_catalogo = ModuloCatalog.objects.filter(apresentacaoModulo=modulo_catalogo_apresentacao.id)
    lista_estilo = Estilo.objects.filter(modeloArquitetura=id)


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
                                     "modulo_catalogo": modulo_catalogo_apresentacao,
                                     "lista_modulo_catalogo": lista_modulo_catalogo,
                                     "diretrizes_variabilidade_comportamental": diretrizes_variabilidade_comportamental,
                                     "diretrizes_variabilidade_implementacao": diretrizes_variabilidade_implementacao,
                                     "lista_estilo": lista_estilo}, "documento_pdf")

def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/boletim/index.html')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Sua conta esta desativada!")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('boletim/login.html', {}, context)