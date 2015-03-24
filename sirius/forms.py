from django import forms
from models import ModeloArquitetura,ModeloArquiteturaAvaliacao,Tecnologias,TradeOff,Diretriz,Referencia

class FormModeloArquitetura(forms.ModelForm):
    class Meta:
        model = ModeloArquitetura
        tecnologia = [FormTecnologiasInline]
        referencia = [FormReferenciaInline]
        fields = ('nome', 'introducao', 'tecnologia', 'refencia')

class FormTecnologiasInline(forms.TabularInline):
    class Meta:
        model = Tecnologias
        extra = 0

class FormReferenciaInline(forms.TabularInline):
    class Meta:
        model = Referencia
        extra = 0

