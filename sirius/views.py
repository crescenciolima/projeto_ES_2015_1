from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from models import ModeloArquitetura,ModeloArquiteturaAvaliacao,Tecnologias,TradeOff,Diretriz,Referencia
from forms import FormModeloArquitetura

def index(request):
    if request.method == 'POST':
        form = FormModeloArquitetura(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return render(request,"aviso_salvo",{})
    else:
        form = FormModeloArquitetura()
    return render(request,"",{"form":form},context_instance=RequestContext(request))