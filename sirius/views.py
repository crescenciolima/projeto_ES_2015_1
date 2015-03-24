from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from models import ModeloArquitetura, ModeloArquiteturaAvaliacao, Tecnologias, TradeOff, Diretriz, Referencia
from forms import FormModeloArquitetura
import operator

def index(request):
    lista_documentos = ModeloArquitetura.objects.sort(key=operator.attrgetter('nome'))

    return render(request, "documentos.html",
              {"lista_documentos": lista_documentos}, context_instance=RequestContext(request))

