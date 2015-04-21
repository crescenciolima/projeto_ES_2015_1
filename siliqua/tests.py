#coding:utf-8
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase, Client
from models import TipoPadrao, TipoDecisao, Padrao, Decisao, TagPadrao, TagDecisao
from django.core.urlresolvers import resolve

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


###########################################testes de bd##############################################

#testes positivos
class TipoPadraoTest(TestCase):

    def setUp(self):
        self.tipoPadrao = TipoPadrao.objects.create(nome="tipo de padrao")

    def test_models(self):
        tipoPadrao = TipoPadrao.objects.get(id=1)
        self.assertEqual(tipoPadrao.nome, "tipo de padrao")

class TipoDecisaoTest(TestCase):

    def setUp(self):
        self.tipoDecisao = TipoDecisao.objects.create(nome="tipo de decisao")

    def test_models(self):
        tipoDecisao = TipoDecisao.objects.get(id=1)
        self.assertEqual(tipoDecisao.nome, "tipo de decisao")

class TagPadraoTest(TestCase):

    def setUp(self):
        self.tagPadrao = TagPadrao.objects.create(nome="tag de padrao")

    def test_models(self):
        tagPadrao = TagPadrao.objects.get(id=1)
        self.assertEqual(tagPadrao.nome, "tag de padrao")

class TagDecisaoTest(TestCase):

    def setUp(self):
        self.tagDecisa = TagDecisao.objects.create(nome="tag de decisao")

    def test_models(self):
        tagDecisao = TagDecisao.objects.get(id=1)
        self.assertEqual(tagDecisao.nome, "tag de decisao")

class PadraoTest(TestCase):

    def setUp(self):
        self.tipoPadrao = TipoPadrao.objects.create(nome="padrao")
        self.padrao = Padrao.objects.create(nome="padrao", aliase="aliase", contexto="contexto",
                                            problema="problema", vantagens="vantagens", desvantagens="desvantagens",
                                            aplicabilidade="aplicabilidade", referencias="referencias",
                                            tipoDePadrao=self.tipoPadrao)
        self.padrao.padroesRelacionados.create(nome="padrao", aliase="aliase", contexto="contexto",
                                            problema="problema", vantagens="vantagens", desvantagens="desvantagens",
                                            aplicabilidade="aplicabilidade", referencias="referencias", tipoDePadrao=self.tipoPadrao)
        self.padrao.padroesRelacionados.create(nome="padrao", aliase="aliase", contexto="contexto",
                                            problema="problema", vantagens="vantagens", desvantagens="desvantagens",
                                            aplicabilidade="aplicabilidade", referencias="referencias", tipoDePadrao=self.tipoPadrao)


    def test_models(self):
        padroes = Padrao.objects.all()
        self.assertEqual(padroes.count(), 3)

class DecisaoTest(TestCase):

    def setUp(self):
        self.tipoPadrao = TipoPadrao.objects.create(nome="padrao")
        self.tipoDecisao = TipoDecisao.objects.create(nome="tipo de decisao")
        self.decisao = Decisao.objects.create(nome="decisao", descricao="descricao", objetivo="objetivo", motivacao="motivacao",
                                                tipoDeDecisao=self.tipoDecisao, escopo="escopo", hipoteses="hipoteses", restricoes="restricoes",
                                                alternativas="alternativas", implicacoes="implicacoes", necessidades="necessidades",
                                                notas="notas", estado='Aprovado')
        self.decisao.categorias.create(nome="tagdecisao")

        self.decisaoRelacionada = self.decisao.decisaoRelacionada.create(nome="decisao", descricao="descricao", objetivo="objetivo", motivacao="motivacao",
                                                tipoDeDecisao=self.tipoDecisao, escopo="escopo", hipoteses="hipoteses", restricoes="restricoes",
                                                alternativas="alternativas", implicacoes="implicacoes", necessidades="necessidades",
                                                notas="notas", estado='Aprovado')
        self.decisaoRelacionada.categorias.create(nome="tagdecisao")



        self.decisao.padraoUtilizado.create(nome="padrao", aliase="aliase", contexto="contexto",
                                            problema="problema", vantagens="vantagens", desvantagens="desvantagens",
                                            aplicabilidade="aplicabilidade", referencias="referencias", tipoDePadrao=self.tipoPadrao)

    def test_models(self):
        decisoes = Decisao.objects.all()
        self.assertEqual(decisoes.count(), 2)




################################################## teste views #########################################################

##positivo

class HomePageTest(TestCase):

    def test_url(self):
      c = Client()
      response = c.get('/')
      self.assertEqual(response.status_code, 200)

class PaginaPesquisa(TestCase):

    def test_url(self):
        c = Client()
        response = c.get('/form_pesquisa')
        self.assertEqual(response.status_code, 301)

    def test_pesquisa_decisao(self):
        c = Client()
        response = c.get('/pesquisar/?q=d&por=decisao')
        self.assertEqual(response.status_code, 200)

    def test_detalhe_decisao(self):
        self.tipoPadrao = TipoPadrao.objects.create(nome="padrao")
        self.tipoDecisao = TipoDecisao.objects.create(nome="tipo de decisao")
        self.decisao = Decisao.objects.create(nome="decisao", descricao="descricao", objetivo="objetivo", motivacao="motivacao",
                                                tipoDeDecisao=self.tipoDecisao, escopo="escopo", hipoteses="hipoteses", restricoes="restricoes",
                                                alternativas="alternativas", implicacoes="implicacoes", necessidades="necessidades",
                                                notas="notas", estado='Aprovado')

        self.decisao.decisaoRelacionada.create(nome="decisao", descricao="descricao", objetivo="objetivo", motivacao="motivacao",
                                                tipoDeDecisao=self.tipoDecisao, escopo="escopo", hipoteses="hipoteses", restricoes="restricoes",
                                                alternativas="alternativas", implicacoes="implicacoes", necessidades="necessidades",
                                                notas="notas", estado='Aprovado')

        self.decisao.padraoUtilizado.create(nome="padrao", aliase="aliase", contexto="contexto",
                                            problema="problema", vantagens="vantagens", desvantagens="desvantagens",
                                            aplicabilidade="aplicabilidade", referencias="referencias", tipoDePadrao=self.tipoPadrao)

        c = Client()
        response = c.get('/pesquisar/decisao/1.html')
        self.assertEqual(response.status_code, 200)

        ##teste gerar pdf
        response = c.get('/gerarpdfdecisao/?id=1')
        self.assertEqual(response.status_code, 200)

        ##teste historico
        response = c.get('/historico/?id=1')
        self.assertEqual(response.status_code, 200)

    def test_pesquisa_padrao(self):
        c = Client()
        response = c.get('/pesquisar/?q=p&por=padrao')
        self.assertEqual(response.status_code, 200)

    def test_detalhe_padrao(self):
        self.tipoPadrao = TipoPadrao.objects.create(nome="padrao")
        self.padrao = Padrao.objects.create(nome="padrao", aliase="aliase", contexto="contexto",
                                            problema="problema", vantagens="vantagens", desvantagens="desvantagens",
                                            aplicabilidade="aplicabilidade", referencias="referencias",
                                            tipoDePadrao=self.tipoPadrao)
        self.padrao.padroesRelacionados.create(nome="padrao", aliase="aliase", contexto="contexto",
                                            problema="problema", vantagens="vantagens", desvantagens="desvantagens",
                                            aplicabilidade="aplicabilidade", referencias="referencias", tipoDePadrao=self.tipoPadrao)
        c = Client()
        response = c.get('/pesquisar/padrao/1.html')
        self.assertEqual(response.status_code, 200)
        ##teste gerar pdf
        response = c.get('/gerarpdfpadrao/?id=1')
        self.assertEqual(response.status_code, 200)

    def test_pesquisa_tipodecisao(self):
        c = Client()
        response = c.get('/pesquisar/?q=tipodecisao&por=tipdecisao')
        self.assertEqual(response.status_code, 200)

    def test_detalhe_tipodecisao(self):
        self.tipoDecisao = TipoDecisao.objects.create(nome="tipo de decisao")
        c = Client()
        response = c.get('/pesquisar/tipo-decisao/1.html')
        self.assertEqual(response.status_code, 200)

    def test_pesquisa_tipopadrao(self):
        c = Client()
        response = c.get('/pesquisar/?q=tipopadrao&por=tippadrao')
        self.assertEqual(response.status_code, 200)

    def test_detalhe_tipopadrao(self):
        self.tipoPadrao = TipoPadrao.objects.create(nome="tipo de padrao")
        c = Client()
        response = c.get('/pesquisar/tipo-padrao/1.html')
        self.assertEqual(response.status_code, 200)


    ##testes de cadastro
    def test_cadastro_decisao(self):
        c = Client()
        self.tipoDecisao = TipoDecisao.objects.create(nome="tipo de decisao")
        response = c.post('/admin/siliqua/decisao/add/', {'nome': 'decisao', 'descricao': 'descricao', 'objetivo':'objetivo',
                                                            'motivacao':'motivacao', 'tipoDeDecisao':1, 'escopo':'escopo', 'hipoteses':'hipoteses',
                                                            'restricoes':'restricoes', 'alternativas':'alternativas', 'implicacoes':'implicacoes',
                                                            'necessidades':'necessidade', 'notas':'notas', 'estado':'Sugerido', '_save':'Salvar'})
        self.assertEqual(response.status_code, 200)

    def test_cadastro_padrao(self):
        c = Client()
        self.tipoPadrao = TipoPadrao.objects.create(nome="tipo de padrao")
        response = c.post('/admin/siliqua/padrao/add/',{'nome':'padrao', 'aliase':'aliase', 'contexto':'conteto', 'problema':'problema',
                                                        'vantagens':'vantagens', 'desvantagens':'desvantagens', 'aplicabiliddade':'aplicabilidade',
                                                        'referencias':'referencias', 'tipoDePadrao':1, '_save':'Salvar'})
        self.assertEqual(response.status_code, 200)

    def test_cadastrado_tipodecisao(self):
        c = Client()
        response = c.post('/admin/siliqua/tipodecisao/add/',{'nome':'tipo de decisao', '_save':'Salvar'})
        self.assertEqual(response.status_code, 200)

    def test_cadastrado_tipopadrao(self):
        c = Client()
        response = c.post('/admin/siliqua/tipopadrao/add/',{'nome':'tipo de padrao', '_save':'Salvar'})
        self.assertEqual(response.status_code, 200)

    def test_cadastrado_tagdecisao(self):
        c = Client()
        response = c.post('/admin/siliqua/tagdecisao/add/',{'nome':'tag de decisao', '_save':'Salvar'})
        self.assertEqual(response.status_code, 200)

    def test_cadastrado_tagpadrao(self):
        c = Client()
        response = c.post('/admin/siliqua/tagpadrao/add/',{'nome':'tag de padrao', '_save':'Salvar'})
        self.assertEqual(response.status_code, 200)


