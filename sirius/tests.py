"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from sirius.models import Apresentacao
from sirius.models import DiretrizesVariabilidade
from sirius.models import Estilo
from sirius.models import ModeloArquitetura
from sirius.models import AtributoDiretriz
from sirius.models import VisaoImplementacao
from django.core.files import File

# teste de caracteres maximo positivoApresentação
class ApresentacaoTestePositivo(TestCase):
    def create_apresentacao(self,
                            descricao="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesqu"):
        return Apresentacao.objects.create(descricao=descricao)

    def test_apresentacao_positivo(self):
        self.assertTrue(len(self.create_apresentacao().descricao) <= 150)


#teste de caracteres maximo negativoApresentação
class ApresentacaoTesteNegativo(TestCase):
    def create_apresentacao(self,
                            descricao="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesquasd"):
        return Apresentacao.objects.create(descricao=descricao)

    def test_apresentacao_negativo(self):
        self.assertTrue(len(self.create_apresentacao().descricao) <= 150)

#teste de campo em branco positivoVisaoImplementação
class VisaoImplementacaoTestePositivo(TestCase):
    def create_apresentacao(self, descricao = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesqu"):
        return Apresentacao.objects.create(descricao=descricao)
    def create_visao_atual(self,visao = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesqu"):
        return VisaoImplementacao.objects.create(visao=visao)
    def test_visiao_atual_positivo(self):
        self.assertTrue(len(self.create_visao_atual().visao) != 0)

#teste de campo em branco NegativoVisaoImplementação
class VisaoImplementacaoTestePositivo(TestCase):
    def create_apresentacao(self, descricao = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesqu"):
        return Apresentacao.objects.create(descricao=descricao)
    def create_visao_atual(self,visao = ""):
        return VisaoImplementacao.objects.create(visao=visao)
    def test_visiao_atual_positivo(self):
        self.assertTrue(len(self.create_visao_atual().visao) != 0)

#teste de campo em branco positivoDiretrizesDeVariabilidade
class DiretrizesVariabilidadeTestePositivo(TestCase):
    def create_apresentacao(self,
                            descricao="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesqu"):
        return Apresentacao.objects.create(descricao=descricao)

    def create_diretrizesvariabilidade(self, mensagem="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesqua"):
        return DiretrizesVariabilidade.objects.create(mensagem=mensagem, apresentacao_behavioral=self.create_apresentacao())

    def test_diretrizes_variabilidade_positivo(self):
        self.assertTrue(len(self.create_diretrizesvariabilidade().mensagem) != 0)

#teste de campo em branco negativoDiretrizesDeVariabilidade
class DiretrizesVariabilidadeTesteNegativo(TestCase):
    def create_apresentacao(self,
                            descricao="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesqu"):
        return Apresentacao.objects.create(descricao=descricao)

    def create_diretrizesvariabilidade(self, mensagem=""):
        return DiretrizesVariabilidade.objects.create(mensagem=mensagem, apresentacao_behavioral=self.create_apresentacao())

    def test_diretrizes_variabilidade_negativo(self):
        self.assertTrue(len(self.create_diretrizesvariabilidade().mensagem) != 0)


#teste de campo máximo positivoAtributoDiretriz
class AtriburtoTestePositivo(TestCase):
    def atributoDiretriz(self, diretriz = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. PellentesquLorem ipsum dolor sit amet, consectetuer "):
        return AtributoDiretriz.objects.create(diretriz=diretriz)
    def create_atributo(self, atrib_quali_afetado = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. PellentesquLorem ipsum dolor sit amet, consectetuer ",
                        estimulo = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. PellentesquLorem ipsum dolor sit amet, consectetuer ",
                        resposta = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. PellentesquLorem ipsum dolor sit amet, consectetuer ",
                        estrategia = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. PellentesquLorem ipsum dolor sit amet, consectetuer "):
        return AtributoDiretriz.objetcs.create(atrib_quali_afetado=atrib_quali_afetado, estimulo=estimulo, resposta=resposta, estrategia=estrategia)
    def test_atributo_diretriz_positivo(self):
        self.assertTrue(self.create_atributo().atrib_quali_afetado <= 200)


#teste de campo máximo negativoAtributoDiretriz
class AtriburtoTesteNegativo(TestCase):
    def atributoDiretriz(self, diretriz = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. PellentesquLorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesqu"):
        return AtributoDiretriz.objects.create(diretriz=diretriz)
    def create_atributo(self, atrib_quali_afetado = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. PellentesquLorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesqu",
                        estimulo = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. PellentesquLorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesqu",
                        resposta = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. PellentesquLorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesqu",
                        estrategia = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. PellentesquLorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesqu"):
        return AtributoDiretriz.objetcs.create(atrib_quali_afetado=atrib_quali_afetado, estimulo=estimulo, resposta=resposta, estrategia=estrategia)
    def test_atributo_diretriz_positivo(self):
        self.assertTrue(self.create_atributo().atrib_quali_afetado <= 200)


#teste de campo máximo positivoEstilo
class EstiloTestesPositivo(TestCase):

    def modeloArquitetura(self, nome = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. PellentesquLorem ipsum dolor sit amet, consectetuer "):
        return ModeloArquitetura.objects.create(nome=nome)
    def create_estilo(self, estilo = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. PellentesquLorem ipsum dolor sit amet, consectetuer ",
                      abordagem = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. PellentesquLorem ipsum dolor sit amet, consectetuer ",
                      justificativa = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. PellentesquLorem ipsum dolor sit amet, consectetuer "):
        return Estilo.objects.create(estilo=estilo, abordagem=abordagem, justificativa=justificativa, modeloArquitetura=self.create_estilo())

    def test_estilo_positivo(self):
        self.assertTrue(self.create_estilo().estilo <= 200)


#teste de campo máximo negativoEstilo
class EstiloTestesNegativo(TestCase):
    def modeloArquitetura(self, nome = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. PellentesquLorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesqu"):
        return ModeloArquitetura.objects.create(nome=nome)
    def create_estilo(self, estilo = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. PellentesquLorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesqu",
                      abordagem = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. PellentesquLorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesqu",
                      justificativa = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. PellentesquLorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesqu"):
        return Estilo.objects.create(estilo=estilo, abordagem=abordagem, justificativa=justificativa, modeloArquitetura=self.create_estilo())

    def test_estilo_negativo(self):
        self.assertTrue(self.create_estilo().estilo <= 200)