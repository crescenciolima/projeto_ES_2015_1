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
        return Apresentacao.objects.create(id=11, descricao=descricao)
    def create_visao_atual(self,visao_atual = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesqu"):
        return VisaoImplementacao.objects.create(visao_atual=visao_atual, apresentacao_de_implementacao=self.create_apresentacao())
    def test_visao_atual_positivo(self):
        self.assertTrue(len(self.create_visao_atual().visao_atual) != 0)

#teste de campo em branco NegativoVisaoImplementacao
class VisaoImplementacaoTesteNegativo(TestCase):
    def create_apresentacao(self, descricao = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesqu"):
        return Apresentacao.objects.create(id=12, descricao=descricao)
    def create_visao_atual(self,visao_atual = ""):
        return VisaoImplementacao.objects.create(visao_atual=visao_atual, apresentacao_de_implementacao=self.create_apresentacao())
    def test_visiao_atual_negativo(self):
        self.assertTrue(len(self.create_visao_atual().visao_atual) != 0)

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
class AtributoDiretrizTestePositivo(TestCase):
    def create_diretriz(self, diretriz = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. PellentesquLorem ipsum dolor sit amet, consectetuer "):
        return Diretriz.objects.create(diretriz=diretriz)
    def create_atributo(self, atributos_de_qualidade_afetado = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. PellentesquLorem ipsum dolor sit amet, consectetuer ",
                        estimulo = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. PellentesquLorem ipsum dolor sit amet, consectetuer ",
                        resposta = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. PellentesquLorem ipsum dolor sit amet, consectetuer ",
                        estrategia = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. PellentesquLorem ipsum dolor sit amet, consectetuer "):
        id_diretriz = self.create_diretriz()
        return AtributoDiretriz.objects.create(atributos_de_qualidade_afetado=atributos_de_qualidade_afetado, estimulo=estimulo, resposta=resposta, estrategia=estrategia, diretriz=id_diretriz)
    def test_atributo_diretriz_positivo(self):
        self.assertTrue(self.create_atributo().atributos_de_qualidade_afetado <= 200)


#teste de campo maximo negativoAtributoDiretriz
class AtributoDiretrizTesteNegativo(TestCase):
    def create_diretriz(self, diretriz = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. PellentesquLorem ipsum dolor sit amet, consectetuer "):
        return Diretriz.objects.create(diretriz=diretriz)
    def create_atributo(self, atributos_de_qualidade_afetado = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. PellentesquLorem ipsum dolor sit amet, consectetuer ",
                        estimulo = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. PellentesquLorem ipsum dolor sit amet, consectetuer ",
                        resposta = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. PellentesquLorem ipsum dolor sit amet, consectetuer ",
                        estrategia = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. PellentesquLorem ipsum dolor sit amet, consectetuer "):
        id_diretriz = self.create_diretriz()
        return AtributoDiretriz.objects.create(atributos_de_qualidade_afetado=atributos_de_qualidade_afetado, estimulo=estimulo, resposta=resposta, estrategia=estrategia, diretriz=id_diretriz)
    def test_atributo_diretriz_negativo(self):
        self.assertTrue(self.create_atributo().atributos_de_qualidade_afetado <= 200)


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

