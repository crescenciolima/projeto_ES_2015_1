"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from sirius.models import DescricaoVisaoAtual
from django.core.files import File

class VisaoAtualTest(TestCase):
    def create_visao_atual(self, visao_atual="um teste", tipo_de_elementos="elementos teste", relacao_de_elementos="relacoes teste", propriedades="propriedades teste", restricoes="restricoes teste"):
        return DescricaoVisaoAtual.objects.create(visao_atual=visao_atual, tipo_de_elementos=tipo_de_elementos, relacao_de_elementos=relacao_de_elementos, propriedades=propriedades, restricoes=restricoes)
    def test_visao_atual_creation(self):
        v = self.create_visao_atual()
        self.assertTrue(isinstance(v, DescricaoVisaoAtual))
        self.assertEqual(v.__unicode__(), v.visao_atual)




#    def shoud_be_cruddable(self, teste_caracteres):
#        expect(teste_caracteres).to_be_cruddable()l

#class SimpleTest(TestCase):
    #def test_basic_addition(self):
      #  """
       # Tests that 1 + 1 always equals 2.
       # """
     #   self.assertEqual(1 + 1, 2)
