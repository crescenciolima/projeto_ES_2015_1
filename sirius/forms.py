from django import forms
from models import ModeloArquitetura,ModeloArquiteturaAvaliacao,Tecnologias,TradeOff,Diretriz,Referencia

class FormModeloArquitetura(forms.ModelForm):
    class Meta:
        model = ModeloArquitetura
        fields = ('nome', 'professor', 'n1', 'n2', 'n3')