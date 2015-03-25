from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from models import ModeloArquitetura, ModeloArquiteturaAvaliacao, Tecnologias, TradeOff, Diretriz, Referencia
from forms import FormModeloArquitetura, FormReferenciaInline, FormTecnologiasInline, FormChoice


def index(request):
    lista_documentos = ModeloArquitetura.objects.all()

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
