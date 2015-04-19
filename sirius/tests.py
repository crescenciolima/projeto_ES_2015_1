"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from sirius.models import DescricaoVisaoAtual
from sirius.models import Apresentacao
from django.core.files import File

#teste positivo
class VisaoAtualTest(TestCase):
    def create_visao_atual(self, visao_atual="um teste", tipo_de_elementos="elementos teste", relacao_de_elementos="relacoes teste", propriedades="propriedades teste", restricoes="restricoes teste"):
        return DescricaoVisaoAtual.objects.create(visao_atual=visao_atual, tipo_de_elementos=tipo_de_elementos, relacao_de_elementos=relacao_de_elementos, propriedades=propriedades, restricoes=restricoes)
    def test_visao_atual_creation(self):
        v = self.create_visao_atual()
        self.assertTrue(isinstance(v, DescricaoVisaoAtual))
        self.assertEqual(v.__unicode__(), v.visao_atual)

#teste positivo
class ApresentacaoTestePositivo(TestCase):
    def create_apresentacao(self, descricao = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesqu"):
        return descricao
    def test_apresentacao_positivo(self):
        verificacao = self.create_apresentacao()
        self.assertTrue(len(verificacao)<=150)

#teste negativo
class ApresentacaoTesteNegativo(TestCase):
    def create_apresentacao(self, descricao = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesquasd"):
        return descricao
    def test_apresentacao_negativo(self):
        verificacao = self.create_apresentacao()
        self.assertTrue(len(verificacao)<=150)
