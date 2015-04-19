"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from sirius.models import Apresentacao
from sirius.models import DiretrizesVariabilidade
from sirius.models import Estilo
from django.core.files import File

# teste de caracteres maximo positivo
class ApresentacaoTestePositivo(TestCase):
    def create_apresentacao(self,
                            descricao="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesqu"):
        return Apresentacao.objects.create(descricao=descricao)

    def test_apresentacao_positivo(self):
        self.assertTrue(len(self.create_apresentacao().descricao) <= 150)


#teste de caracteres maximo negativo
class ApresentacaoTesteNegativo(TestCase):
    def create_apresentacao(self,
                            descricao="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesquasd"):
        return Apresentacao.objects.create(descricao=descricao)

    def test_apresentacao_negativo(self):
        self.assertTrue(len(self.create_apresentacao().descricao) <= 150)


#teste de campo em branco positivo
class DiretrizesVariabilidadeTestePositivo(TestCase):
    def create_apresentacao(self,
                            descricao="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesqu"):
        return Apresentacao.objects.create(descricao=descricao)

    def create_diretrizesvariabilidade(self, mensagem="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesqua"):
        return DiretrizesVariabilidade.objects.create(mensagem=mensagem, apresentacao_behavioral=self.create_apresentacao())

    def test_diretrizes_variabilidade_positivo(self):
        self.assertTrue(len(self.create_diretrizesvariabilidade().mensagem) != 0)

#teste de campo em branco negativo
class DiretrizesVariabilidadeTesteNegativo(TestCase):
    def create_apresentacao(self,
                            descricao="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesqu"):
        return Apresentacao.objects.create(descricao=descricao)

    def create_diretrizesvariabilidade(self, mensagem=""):
        return DiretrizesVariabilidade.objects.create(mensagem=mensagem, apresentacao_behavioral=self.create_apresentacao())

    def test_diretrizes_variabilidade_negativo(self):
        self.assertTrue(len(self.create_diretrizesvariabilidade().mensagem) != 0)



#teste de campo máximo positivoSaionara
class EstiloTestesPositivo(TestCase):
    def create_estilo(self, estilo = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. PellentesquLorem ipsum dolor sit amet, consectetuer "):
        return Estilo.objects.create(estilo=estilo)
    def test_estilo_positivo(self):
        self.assertTrue(self.create_estilo().estilo <= 200)
