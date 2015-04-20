from django.test import TestCase
from sirius.models import Apresentacao
from sirius.models import DiretrizesVariabilidade
from sirius.models import Estilo
from sirius.models import ModeloArquitetura
from sirius.models import AtributoDiretriz
from sirius.models import VisaoImplementacao
from sirius.models import Diretriz
from sirius.models import Referencia
from sirius.models import VisaoBehavioral
from sirius.models import DescricaoVisaoAtual
from sirius.models import ApresentacaoModulo
from sirius.models import StakeHoldersImplementacao
from sirius.models import ModeloArquiteturaAvaliacao
from django.core.files import File
import unittest


# teste de caracteres maximo positivoApresentacao
@unittest.skip("Pula esse teste")
class ApresentacaoTestePositivo(TestCase):
    def create_apresentacao(self,
                            descricao="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesqu"):
        return Apresentacao.objects.create(descricao=descricao)

    def test_apresentacao_positivo(self):
        self.assertTrue(len(self.create_apresentacao().descricao) <= 150)


#teste de caracteres maximo negativoApresentacao
@unittest.skip("Pula esse teste")
class ApresentacaoTesteNegativo(TestCase):
    def create_apresentacao(self,
                            descricao="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesquasd"):
        return Apresentacao.objects.create(descricao=descricao)

    def test_apresentacao_negativo(self):
        self.assertTrue(len(self.create_apresentacao().descricao) <= 150)

#teste de campo em branco positivoVisaoImplementacao
@unittest.skip("Pula esse teste")
class VisaoImplementacaoTestePositivo(TestCase):
    def create_apresentacao(self, descricao = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesqu"):
        return Apresentacao.objects.create(descricao=descricao)
    def create_visao_atual(self,visao = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesqu"):
        return VisaoImplementacao.objects.create(visao=visao)
    def test_visiao_atual_positivo(self):
        self.assertTrue(len(self.create_visao_atual().visao) != 0)

#teste de campo em branco NegativoVisaoImplementacao
@unittest.skip("Pula esse teste")
class VisaoImplementacaoTestePositivo(TestCase):
    def create_apresentacao(self, descricao = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesqu"):
        return Apresentacao.objects.create(descricao=descricao)
    def create_visao_atual(self,visao = ""):
        return VisaoImplementacao.objects.create(visao=visao)
    def test_visiao_atual_positivo(self):
        self.assertTrue(len(self.create_visao_atual().visao) != 0)

#teste de campo em branco positivoDiretrizesDeVariabilidade
@unittest.skip("Pula esse teste")
class DiretrizesVariabilidadeTestePositivo(TestCase):
    def create_apresentacao(self,
                            descricao="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesqu"):
        return Apresentacao.objects.create(descricao=descricao)

    def create_diretrizesvariabilidade(self, mensagem="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesqua"):
        return DiretrizesVariabilidade.objects.create(mensagem=mensagem, apresentacao_behavioral=self.create_apresentacao())

    def test_diretrizes_variabilidade_positivo(self):
        self.assertTrue(len(self.create_diretrizesvariabilidade().mensagem) != 0)

#teste de campo em branco negativoDiretrizesDeVariabilidade
@unittest.skip("Pula esse teste")
class DiretrizesVariabilidadeTesteNegativo(TestCase):
    def create_apresentacao(self,
                            descricao="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesqu"):
        return Apresentacao.objects.create(descricao=descricao)

    def create_diretrizesvariabilidade(self, mensagem=""):
        return DiretrizesVariabilidade.objects.create(mensagem=mensagem, apresentacao_behavioral=self.create_apresentacao())

    def test_diretrizes_variabilidade_negativo(self):
        self.assertTrue(len(self.create_diretrizesvariabilidade().mensagem) != 0)


#teste de campo maximo positivoAtributoDiretriz
@unittest.skip("Pula esse teste")
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
@unittest.skip("Pula esse teste")
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
@unittest.skip("Pula esse teste")
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
@unittest.skip("Pula esse teste")
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
@unittest.skip("Pula esse teste")
class DiretrizPositivo(TestCase):
    def create_diretriz(self, diretriz="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam rutrum, nisl sed bibendum euismod, dui magna fringilla nibh, quis efficitur ante nunc nec augue. In sagittis ultrices felis id dapibus. Ae"):
        return Diretriz.objects.create(diretriz=diretriz)

    def test_diretriz_positivo(self):
        self.assertTrue(len(self.create_diretriz().diretriz) <= 200)

#teste de caracteres maximo negativo
@unittest.skip("Pula esse teste")
class DiretrizNegativo(TestCase):
    def create_diretriz(self, diretriz="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam rutrum, nisl sed bibendum euismod, dui magna fringilla nibh, quis efficitur ante nunc nec augue. In sagittis ultrices felis id dapibus. Aenedsadasas"):
        return Diretriz.objects.create(diretriz=diretriz)

    def test_diretriz_negativo(self):
        self.assertTrue(len(self.create_diretriz().diretriz) <= 200)

#TESTE CARACTERES MAXIMO SOCRATES positivo
class StakeHoldersImplementacaoTestePositivo(TestCase):
    def create_visao_implementacao(self, visao_atual="visao atual"):
        return VisaoImplementacao(id=1, visao_atual=visao_atual)

    def create_stakeholders_implementacao(self,stakeholders="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesqu", precupacoes="teste preocupacoes"):
        instacia_visao_implementacao = self.create_visao_implementacao()
        return StakeHoldersImplementacao.objects.create(stakeholders=stakeholders, precupacoes=precupacoes, visao_de_implementacao=instacia_visao_implementacao)

    def test_stakeholders_implementacao_positivo(self):
       self.assertTrue(len(self.create_stakeholders_implementacao().stakeholders) <= 150)

#teste caracteres maximo negativo
class StakeHoldersImplementacaoTesteNegativo(TestCase):
    def create_visao_implementacao(self, visao_atual="visao atual"):
        return VisaoImplementacao(id=1, visao_atual=visao_atual)

    def create_stakeholders_implementacao(self,stakeholders="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesquasasada", precupacoes="teste preocupacoes"):
        instacia_visao_implementacao = self.create_visao_implementacao()
        return StakeHoldersImplementacao.objects.create(stakeholders=stakeholders, precupacoes=precupacoes, visao_de_implementacao=instacia_visao_implementacao)

    def test_stakeholders_implementacao_negativo(self):
       self.assertTrue(len(self.create_stakeholders_implementacao().stakeholders) <= 150)

