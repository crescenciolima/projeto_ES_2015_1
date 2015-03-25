from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from models import ModeloArquitetura, ModeloArquiteturaAvaliacao, Tecnologias, TradeOff, Diretriz, Referencia
from forms import FormModeloArquitetura
import operator

def index(request):
    lista_documentos = ModeloArquitetura.objects.all()

    return render(request, "documentos.html",
              {"lista_documentos": lista_documentos}, context_instance=RequestContext(request))

def adiciona_documento(request):
    if request.method == "POST":
        form = FormModeloArquitetura(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            #item.usuario = request.user
            item.save()
            return render(request, "aviso_salvo.html", {})
    else:
        form = FormModeloArquitetura()
    return render(request, "adiciona_documento.html", {"form": form},
                  context_instance=RequestContext(request))