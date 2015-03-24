from django import forms
from models import ModeloArquitetura,ModeloArquiteturaAvaliacao,Tecnologias,TradeOff,Diretriz,Referencia

class FormTecnologiasInline(forms.ModelForm):
    class Meta:
        model = Tecnologias
        extra = 0

class FormReferenciaInline(forms.ModelForm):
    class Meta:
        model = Referencia
        extra = 0

class FormModeloArquitetura(forms.ModelForm):
    class Meta:
        model = ModeloArquitetura
        tecnologia = [FormTecnologiasInline]
        referencia = [FormReferenciaInline]
        widgets = {'yes_or_no': forms.RadioSelect}
        fields = ('nome', 'introducao')

