from django import forms
from models import ModeloArquitetura,ModeloArquiteturaAvaliacao,Tecnologias,TradeOff,Diretriz,Referencia
from django.forms import ModelForm
from django.forms.models import inlineformset_factory

class FormTecnologiasInline(forms.ModelForm):
    class Meta:
        model = Tecnologias
        exclude = ['modeloArquitetura'] #Essa eh a chave estrangeira (verificar se exclui-la do form causa problema de referencias ao salvar, caso sim, tentar hidden (esconder))
        fields = ('tecnologia', 'justificativa', 'modeloArquitetura')

class FormReferenciaInline(forms.ModelForm):
    class Meta:
        model = Referencia
        exclude = ['modeloArquitetura']
        fields = ('referencia', 'modeloArquitetura')

class FormModeloArquitetura(forms.ModelForm):
    class Meta:
        model = ModeloArquitetura
        exclude = ['referencia_escolha']



class FormChoice(forms.ModelForm):
    class Meta:
        model = ModeloArquitetura
        exclude = ['nome', 'introducao']
        fields = ('nome', 'introducao', 'referencia_escolha')
