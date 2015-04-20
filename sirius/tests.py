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

# teste de caracteres maximo positivoApresentacao
class ApresentacaoTestePositivo(TestCase):
    def create_apresentacao(self,
                            descricao="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesqu"):
        return Apresentacao.objects.create(descricao=descricao)

    def test_apresentacao_positivo(self):
        self.assertTrue(len(self.create_apresentacao().descricao) <= 150)


#teste de caracteres maximo negativoApresentacao
class ApresentacaoTesteNegativo(TestCase):
    def create_apresentacao(self,
                            descricao="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesquasd"):
        return Apresentacao.objects.create(descricao=descricao)

    def test_apresentacao_negativo(self):
        self.assertTrue(len(self.create_apresentacao().descricao) <= 150)

#teste de campo em branco positivoVisaoImplementacao
class VisaoImplementacaoTestePositivo(TestCase):
    def create_apresentacao(self, descricao = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesqu"):
        return Apresentacao.objects.create(descricao=descricao)
    def create_visao_atual(self,visao = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesqu"):
        return VisaoImplementacao.objects.create(visao=visao)
    def test_visiao_atual_positivo(self):
        self.assertTrue(len(self.create_visao_atual().visao) != 0)

#teste de campo em branco NegativoVisaoImplementacao
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


#teste de campo maximo positivoAtributoDiretriz
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


#teste de campo maximo negativoAtributoDiretriz
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


#teste de campo maximo positivoEstilo
class EstiloTestesPositivo(TestCase):

    def modeloArquitetura(self, nome = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. PellentesquLorem ipsum dolor sit amet, consectetuer "):
        return ModeloArquitetura.objects.create(nome=nome)
    def create_estilo(self, estilo = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. PellentesquLorem ipsum dolor sit amet, consectetuer ",
                      abordagem = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. PellentesquLorem ipsum dolor sit amet, consectetuer ",
                      justificativa = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. PellentesquLorem ipsum dolor sit amet, consectetuer "):
        return Estilo.objects.create(estilo=estilo, abordagem=abordagem, justificativa=justificativa, modeloArquitetura=self.create_estilo())

    def test_estilo_positivo(self):
        self.assertTrue(self.create_estilo().estilo <= 200)


#teste de campo maximo negativoEstilo
class EstiloTestesNegativo(TestCase):
    def modeloArquitetura(self, nome = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. PellentesquLorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesqu"):
        return ModeloArquitetura.objects.create(nome=nome)
    def create_estilo(self, estilo = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. PellentesquLorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesqu",
                      abordagem = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. PellentesquLorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesqu",
                      justificativa = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. PellentesquLorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesqu"):
        return Estilo.objects.create(estilo=estilo, abordagem=abordagem, justificativa=justificativa, modeloArquitetura=self.create_estilo())

    def test_estilo_negativo(self):
        self.assertTrue(self.create_estilo().estilo <= 200)

#teste de caracteres maximo positivo
class DiretrizPositivo(TestCase):
    def create_diretriz(self, diretriz="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam rutrum, nisl sed bibendum euismod, dui magna fringilla nibh, quis efficitur ante nunc nec augue. In sagittis ultrices felis id dapibus. Ae"):
        return Diretriz.objects.create(diretriz=diretriz)

    def test_diretriz_positivo(self):
        self.assertTrue(len(self.create_diretriz().diretriz) <= 200)

#teste de caracteres maximo negativo
class DiretrizNegativo(TestCase):
    def create_diretriz(self, diretriz="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam rutrum, nisl sed bibendum euismod, dui magna fringilla nibh, quis efficitur ante nunc nec augue. In sagittis ultrices felis id dapibus. Aenedsadasas"):
        return Diretriz.objects.create(diretriz=diretriz)

    def test_diretriz_negativo(self):
        self.assertTrue(len(self.create_diretriz().diretriz) <= 200)

class ReferenciaPositivo(TestCase):
    def create_apresentacao(self, descricao="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesqu"):
        return Apresentacao.objects.create(descricao=descricao)

    def create_descricao_visao_atual(self, visao_atual="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam rutrum, nisl sed bibendum euismod, dui magna fringilla nibh, quis efficitur ante nunc nec augue. In sagittis ultrices felis id dapibus. Aene",
                                     tipo_de_elementos="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam rutrum, nisl sed bibendum euismod, dui magna fringilla nibh, quis efficitur ante nunc nec augue. In sagittis ultrices felis id dapibus. Aene",
                                     relacao_de_elementos="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam rutrum, nisl sed bibendum euismod, dui magna fringilla nibh, quis efficitur ante nunc nec augue. In sagittis ultrices felis id dapibus. Aene",
                                     propriedades="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam rutrum, nisl sed bibendum euismod, dui magna fringilla nibh, quis efficitur ante nunc nec augue. In sagittis ultrices felis id dapibus. Aene",
                                     restricoes="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam rutrum, nisl sed bibendum euismod, dui magna fringilla nibh, quis efficitur ante nunc nec augue. In sagittis ultrices felis id dapibus. Aene"):
        return DescricaoVisaoAtual.objects.create(visao_atual=visao_atual, tipo_de_elementos=tipo_de_elementos, relacao_de_elementos=relacao_de_elementos, propriedades=propriedades, restricoes=restricoes)

    def create_visao_behavioral(self, descricao_do_comportamento_de_dominio="teste"):
        return VisaoBehavioral(descricao_do_comportamento_de_dominio=descricao_do_comportamento_de_dominio, visao_atual=self.create_descricao_visao_atual(), apresentacao_behavioral=self.create_apresentacao())

    def create_visao_implementacao(self, visao_atual="visao atual"):
        return VisaoImplementacao(visao_atual=visao_atual, apresentacao_de_implementacao=self.create_apresentacao())

    def create_apresentacao_modulo(self, relacionamento_dos_modulos="relacionamento"):
        return ApresentacaoModulo.objects.create(relacionamento_dos_modulos=relacionamento_dos_modulos)

    def create_modeloarquitetura(self, nome="arquitetura", introducao="introducao", drives_arquitetonicos="drivers"):
        return ModeloArquitetura.objects.create(nome=nome, introducao=introducao, drives_arquitetonicos=drives_arquitetonicos, visao_comportamental=self.create_visao_behavioral(), visao_de_implementacao=self.create_visao_implementacao(), visao_atual=self.create_descricao_visao_atual(), modulo_catalog=self.create_apresentacao_modulo())

    def create_referencia(self, referencia="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam rutrum, nisl sed bibendum euismod, dui magna fringilla nibh, quis efficitur ante nunc nec augue. In sagittis ultrices felis id dapibus. Ae"):
        return Referencia.objects.create(referencia=referencia, modeloArquitetura=self.create_modeloarquitetura())

    def test_referencia_positivo(self):
        self.assertTrue(len(self.create_referencia().referencia) <= 200)
