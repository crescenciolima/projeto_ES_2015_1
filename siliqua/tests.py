#coding:utf-8
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase, Client
from models import TipoPadrao, TipoDecisao, Padrao, Decisao, TagPadrao, TagDecisao
from canarius.models import Arquitetura, AtributoDeQualidade, Relacionamento2, Relacionamento4, Relacionamento6
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
      self.assertEqual(response.status_code, 302)

class SiliquaUrl(TestCase):

    def test_url(self):
        c = Client()
        response = c.get('/admin/siliqua/')
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

    def test_pdf_decisao(self):
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
        ##teste gerar pdf
        response = c.get('/gerarpdfdecisao/?id=0')
        self.assertEqual(response.status_code, 404)

    def test_historico_decisao(self):
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

    def test_pdf_padrao(self):
        self.tipoPadrao = TipoPadrao.objects.create(nome="padrao")
        self.padrao = Padrao.objects.create(nome="padrao", aliase="aliase", contexto="contexto",
                                            problema="problema", vantagens="vantagens", desvantagens="desvantagens",
                                            aplicabilidade="aplicabilidade", referencias="referencias",
                                            tipoDePadrao=self.tipoPadrao)
        self.padrao.padroesRelacionados.create(nome="padrao", aliase="aliase", contexto="contexto",
                                            problema="problema", vantagens="vantagens", desvantagens="desvantagens",
                                            aplicabilidade="aplicabilidade", referencias="referencias", tipoDePadrao=self.tipoPadrao)
        c = Client()
        ##teste gerar pdf
        response = c.get('/gerarpdfpadrao/?id=0')
        self.assertEqual(response.status_code, 404)

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

    ##decisao
    def test_url_decisao(self):
        c = Client()
        response = c.get('/admin/siliqua/decisao/')
        self.assertEqual(response.status_code, 200)

    def test_url_adddecisao(self):
        c = Client()
        response = c.get('/admin/siliqua/decisao/add/')
        self.assertEqual(response.status_code, 200)


    def test_url_acesso_decisao(self):
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

        c = Client()
        response = c.get('/admin/siliqua/decisao/1')
        self.assertEqual(response.status_code, 301)

    def test_cadastro_decisao(self):
        c = Client()
        self.tipoDecisao = TipoDecisao.objects.create(nome="tipo de decisao")
        response = c.post('/admin/siliqua/decisao/add/', {'nome': 'decisao', 'descricao': 'descricao', 'objetivo':'objetivo',
                                                            'motivacao':'motivacao', 'tipoDeDecisao':1, 'escopo':'escopo', 'hipoteses':'hipoteses',
                                                            'restricoes':'restricoes', 'alternativas':'alternativas', 'implicacoes':'implicacoes',
                                                            'necessidades':'necessidade', 'notas':'notas', 'estado':'Sugerido', '_save':'Salvar'})
        self.assertEqual(response.status_code, 200)

    def test_delete_decisao(self):
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

        c = Client()
        response = c.get('/admin/siliqua/decisao/1/delete')
        self.assertEqual(response.status_code, 301)
        response = c.get('/admin/siliqua/decisao/1/delete')
        self.assertEqual(response.status_code, 301)

    #padrao
    def test_url_padrao(self):
        c = Client()
        response = c.get('/admin/siliqua/padrao/')
        self.assertEqual(response.status_code, 200)

    def test_url_addpadrao(self):
        c = Client()
        response = c.get('/admin/siliqua/padrao/add/')
        self.assertEqual(response.status_code, 200)

    def test_url_acesso_padrao(self):
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
        c = Client()
        response = c.get('/admin/siliqua/padrao/1')
        self.assertEqual(response.status_code, 301)

    def test_cadastro_padrao(self):
        c = Client()
        self.tipoPadrao = TipoPadrao.objects.create(nome="tipo de padrao")
        response = c.post('/admin/siliqua/padrao/add/',{'nome':'padrao', 'aliase':'aliase', 'contexto':'conteto', 'problema':'problema',
                                                        'vantagens':'vantagens', 'desvantagens':'desvantagens', 'aplicabiliddade':'aplicabilidade',
                                                        'referencias':'referencias', 'tipoDePadrao':1, '_save':'Salvar'})
        self.assertEqual(response.status_code, 200)

    def test_delete_padrao(self):
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
        c = Client()
        response = c.get('/admin/siliqua/padrao/1/delete')
        self.assertEqual(response.status_code, 301)
        response = c.get('/admin/siliqua/padrao/1/delete')
        self.assertEqual(response.status_code, 301)



    #tipo de decisao
    def test_url_tipodecisao(self):
        c = Client()
        response = c.get('/admin/siliqua/tipodecisao/')
        self.assertEqual(response.status_code, 200)

    def test_url_addtipodecisao(self):
        c = Client()
        response = c.get('/admin/siliqua/tipodecisao/add/')
        self.assertEqual(response.status_code, 200)

    def test_url_acesso_tipodecisao(self):
        self.tipoDecisao = TipoDecisao.objects.create(nome="tipo de decisao")
        c = Client()
        response = c.get('/admin/siliqua/tipodecisao/1')
        self.assertEqual(response.status_code, 301)

    def test_cadastrado_tipodecisao(self):
        c = Client()
        response = c.post('/admin/siliqua/tipodecisao/add/',{'nome':'tipo de decisao', '_save':'Salvar'})
        self.assertEqual(response.status_code, 200)

    def test_delete_tipodecisao(self):
        self.tipoDecisao = TipoDecisao.objects.create(nome="tipo de decisao")
        c = Client()
        response = c.get('/admin/siliqua/tipodecisao/1/delete')
        self.assertEqual(response.status_code, 301)
        response = c.get('/admin/siliqua/tipodecisao/1/delete')
        self.assertEqual(response.status_code, 301)





    #tipo de padrao
    def test_url_tipopadrao(self):
        c = Client()
        response = c.get('/admin/siliqua/tipopadrao/')
        self.assertEqual(response.status_code, 200)

    def test_url_addtipopadrao(self):
        c = Client()
        response = c.get('/admin/siliqua/tipopadrao/add/')
        self.assertEqual(response.status_code, 200)

    def test_url_acesso_tipopadrao(self):
        self.tipoPadrao = TipoPadrao.objects.create(nome="tipo de padrao")
        c = Client()
        response = c.get('/admin/siliqua/tipopadrao/1')
        self.assertEqual(response.status_code, 301)

    def test_cadastrado_tipopadrao(self):
        c = Client()
        response = c.post('/admin/siliqua/tipopadrao/add/',{'nome':'tipo de padrao', '_save':'Salvar'})
        self.assertEqual(response.status_code, 200)

    def test_delete_tipopadrao(self):
        self.tipoPadrao = TipoPadrao.objects.create(nome="tipo de padrao")
        c = Client()
        response = c.get('/admin/siliqua/tipopadrao/1/delete')
        self.assertEqual(response.status_code, 301)
        response = c.get('/admin/siliqua/tipopadrao/1/delete')
        self.assertEqual(response.status_code, 301)



    #tag de decisao
    def test_url_tagdecisao(self):
        c = Client()
        response = c.get('/admin/siliqua/tagdecisao/')
        self.assertEqual(response.status_code, 200)

    def test_url_addtagdecisao(self):
        c = Client()
        response = c.get('/admin/siliqua/tagdecisao/add/')
        self.assertEqual(response.status_code, 200)

    def test_url_acesso_tagdecisao(self):
        self.tagDecisa = TagDecisao.objects.create(nome="tag de decisao")
        c = Client()
        response = c.get('/admin/siliqua/tagdecisao/1')
        self.assertEqual(response.status_code, 301)

    def test_cadastrado_tagdecisao(self):
        c = Client()
        response = c.post('/admin/siliqua/tagdecisao/add/',{'nome':'tag de decisao', '_save':'Salvar'})
        self.assertEqual(response.status_code, 200)

    def test_delete_tagdecisao(self):
        self.tagDecisa = TagDecisao.objects.create(nome="tag de decisao")
        c = Client()
        response = c.get('/admin/siliqua/tagdecisao/1/delete')
        self.assertEqual(response.status_code, 301)
        response = c.get('/admin/siliqua/tagdecisao/1/delete')
        self.assertEqual(response.status_code, 301)




    #tag de padrao
    def test_url_tagpadrao(self):
        c = Client()
        response = c.get('/admin/siliqua/tagpadrao/')
        self.assertEqual(response.status_code, 200)

    def test_url_addtagpadrao(self):
        c = Client()
        response = c.get('/admin/siliqua/tagpadrao/add/')
        self.assertEqual(response.status_code, 200)

    def test_url_acesso_tagpadrao(self):
        self.tagPadrao = TagPadrao.objects.create(nome="tag de padrao")
        c = Client()
        response = c.get('/admin/siliqua/tagpadrao/1')
        self.assertEqual(response.status_code, 301)

    def test_cadastrado_tagpadrao(self):
        c = Client()
        response = c.post('/admin/siliqua/tagpadrao/add/',{'nome':'tag de padrao', '_save':'Salvar'})
        self.assertEqual(response.status_code, 200)

    def test_delete_tagpadrao(self):
        self.tagPadrao = TagPadrao.objects.create(nome="tag de padrao")
        c = Client()
        response = c.get('/admin/siliqua/tagpadrao/1/delete')
        self.assertEqual(response.status_code, 301)
        response = c.get('/admin/siliqua/tagpadrao/1/delete')
        self.assertEqual(response.status_code, 301)






    #################################testes dos trade-offs de atributos de qualidade########################

    def test_url_arquitetura(self):
        c = Client()
        response = c.get('/admin/canarius/arquitetura/')
        self.assertEqual(response.status_code, 200)

    def test_url_arquiteturaadd(self):
        c = Client()
        response = c.get('/admin/canarius/arquitetura/add/')
        self.assertEqual(response.status_code, 200)

    def test_url_acesso_arquitetura(self):
       self.arquitetura = Arquitetura.objects.create(nome="arquitetura")
       c = Client()
       response = c.get('/admin/canarius/arquitetura/1')
       self.assertEqual(response.status_code, 301)

    def test_delete_arquitetura(self):
       self.arquitetura = Arquitetura.objects.create(nome="arquitetura")
       c = Client()
       response = c.get('/admin/canarius/arquitetura/1/delete')
       self.assertEqual(response.status_code, 301)
       response = c.get('/admin/canarius/arquitetura/1/delete')
       self.assertEqual(response.status_code, 301)

    def test_cadastro_arquitetura_1relacionamento(self):
        c = Client()
        response = c.post('/admin/canarius/arquitetura/add/', {'nome': 'decisao', 'descricao': 'descricao', 'introducao':'objetivo',
                                                            'objetivo':'motivacao', 'autores':1, 'tecnologias':1, 'qtdrelacoes':1,'_save':'Salvar'})
        self.assertEqual(response.status_code, 200)

        response = c.post('/admin/canarius/relacionamento2/add/', {'projeto':1, 'relacao1':'confiabilidade', 'relacao2':'usabilidade','fator':2, '_save':'Salvar'})
        self.assertEqual(response.status_code, 200)

        response = c.post('/admin/canarius/atributodequalidade/add/', {'projeto':1, 'funcionamento':4, 'confiabilidade':3,'usabilidade':4,
                                                                    'eficiencia':2, 'manutenibilidade':1,'portabilidade':3,'_save':'Salvar'})
        self.assertEqual(response.status_code, 200)



    def test_cadastro_arquitetura_2relacionamentos(self):
        c = Client()
        response = c.post('/admin/canarius/arquitetura/add/', {'nome': 'decisao', 'descricao': 'descricao', 'introducao':'objetivo',
                                                            'objetivo':'motivacao', 'autores':1, 'tecnologias':1, 'qtdrelacoes':2,'_save':'Salvar'})
        self.assertEqual(response.status_code, 200)

        response = c.post('/admin/canarius/relacionamento4/add/', {'projeto':1, 'relacao1':'funcionamento', 'relacao2':'confiabilidade','fator1':1,
                                                                 'relacao3':'usabilidade', 'relacao4':'eficiencia','fator2':2,'_save':'Salvar'})
        self.assertEqual(response.status_code, 200)

        response = c.post('/admin/canarius/atributodequalidade/add/', {'projeto':1, 'funcionamento':4, 'confiabilidade':3,'usabilidade':4,
                                                                    'eficiencia':2, 'manutenibilidade':1,'portabilidade':3,'_save':'Salvar'})
        self.assertEqual(response.status_code, 200)


    def test_cadastro_arquitetura_3relacionamentos(self):
        c = Client()
        response = c.post('/admin/canarius/arquitetura/add/', {'nome': 'decisao', 'descricao': 'descricao', 'introducao':'objetivo',
                                                            'objetivo':'motivacao', 'autores':1, 'tecnologias':1, 'qtdrelacoes':3,'_save':'Salvar'})
        self.assertEqual(response.status_code, 200)

        response = c.post('/admin/canarius/relacionamento4/add/', {'projeto':1, 'relacao1':'funcionamento', 'relacao2':'confiabilidade','fator1':1,
                                                                 'relacao3':'usabilidade', 'relacao4':'eficiencia','fator2':2,
                                                                 'relacao5':'manutenibilidade', 'relacao6':'portabilidade','fator3':3,'_save':'Salvar'})
        self.assertEqual(response.status_code, 200)

        response = c.post('/admin/canarius/atributodequalidade/add/', {'projeto':1, 'funcionamento':4, 'confiabilidade':3,'usabilidade':4,
                                                                    'eficiencia':2, 'manutenibilidade':1,'portabilidade':3,'_save':'Salvar'})
        self.assertEqual(response.status_code, 200)



    def test_url_atributo(self):
        c = Client()
        response = c.get('/admin/canarius/atributodequalidade/')
        self.assertEqual(response.status_code, 200)

    def test_url_atributoadd(self):
        c = Client()
        response = c.get('/admin/canarius/atributodequalidade/add/')
        self.assertEqual(response.status_code, 200)

    def test_url_acesso_atributo(self):
        self.arquitetura = Arquitetura.objects.create(nome="arquitetura")
        self.atributo = AtributoDeQualidade.objects.create(arquitetura=self.arquitetura, funcionamento=1, confiabilidade=4,
                                                                     usabilidade=3, eficiencia=2, manutenibilidade=2,
                                                                     portabilidade=3)
        c = Client()
        response = c.get('/admin/canarius/atributodequalidade/1')
        self.assertEqual(response.status_code, 301)

    def test_cadastrado_atributo(self):
        c = Client()
        response = c.post('/admin/canarius/atributodequalidade/add/', {'projeto':1, 'funcionamento':1, 'confiabilidade':4,
                                                                     'usabilidade':3, 'eficiencia':2, 'manutenibilidade':2,
                                                                     'portabilidade':3, '_save':'Salvar'})
        self.assertEqual(response.status_code, 200)

    def test_delete_atributo(self):
        self.arquitetura = Arquitetura.objects.create(nome="arquitetura")
        self.atributo = AtributoDeQualidade.objects.create(arquitetura=self.arquitetura, funcionamento=1, confiabilidade=4,
                                                                     usabilidade=3, eficiencia=2, manutenibilidade=2,
                                                                     portabilidade=3)
        c = Client()
        response = c.get('/admin/canarius/atributodequalidade/1/delete')
        self.assertEqual(response.status_code, 301)
        response = c.get('/admin/canarius/atributodequalidade/1/delete')
        self.assertEqual(response.status_code, 301)

    def test_url_1relacionamento(self):
        c = Client()
        response = c.get('/admin/canarius/relacionamento2/')
        self.assertEqual(response.status_code, 200)

    def test_url_1relacionamentoadd(self):
        c = Client()
        response = c.get('/admin/canarius/relacionamento2/add/')
        self.assertEqual(response.status_code, 200)

    def test_url_acesso_1relacionamento(self):
        self.arquitetura = Arquitetura.objects.create(nome="arquitetura")
        self.relacao1 = Relacionamento2.objects.create(projeto=self.arquitetura)
        c = Client()
        response = c.get('/admin/canarius/relacionamento2/1')
        self.assertEqual(response.status_code, 301)

    def test_delete_1relacionamento(self):
        self.arquitetura = Arquitetura.objects.create(nome="arquitetura")
        self.relacao1 = Relacionamento2.objects.create(projeto=self.arquitetura)
        c = Client()
        response = c.get('/admin/canarius/relacionamento2/1/delete')
        self.assertEqual(response.status_code, 301)

    def test_url_2relacionamentos(self):
        c = Client()
        response = c.get('/admin/canarius/relacionamento4/')
        self.assertEqual(response.status_code, 200)


    def test_url_2relacionamentosadd(self):
        c = Client()
        response = c.get('/admin/canarius/relacionamento4/add/')
        self.assertEqual(response.status_code, 200)

    def test_url_acesso_2relacionamentos(self):
        self.arquitetura = Arquitetura.objects.create(nome="arquitetura")
        self.relacao2 = Relacionamento4.objects.create(projeto=self.arquitetura)
        c = Client()
        response = c.get('/admin/canarius/relacionamento4/1')
        self.assertEqual(response.status_code, 301)

    def test_delete_2relacionamentos(self):
        self.arquitetura = Arquitetura.objects.create(nome="arquitetura")
        self.relacao2 = Relacionamento4.objects.create(projeto=self.arquitetura)
        c = Client()
        response = c.get('/admin/canarius/relacionamento4/1/delete')
        self.assertEqual(response.status_code, 301)

    def test_url_3relacionamentos(self):
        c = Client()
        response = c.get('/admin/canarius/relacionamento6/')
        self.assertEqual(response.status_code, 200)


    def test_url_3relacionamentosadd(self):
        c = Client()
        response = c.get('/admin/canarius/relacionamento6/add/')
        self.assertEqual(response.status_code, 200)

    def test_url_acesso_3relacionamentos(self):
        self.arquitetura = Arquitetura.objects.create(nome="arquitetura")
        self.relacao2 = Relacionamento6.objects.create(projeto=self.arquitetura)
        c = Client()
        response = c.get('/admin/canarius/relacionamento6/1')
        self.assertEqual(response.status_code, 301)

    def test_delete_3relacionamentos(self):
        self.arquitetura = Arquitetura.objects.create(nome="arquitetura")
        self.relacao3 = Relacionamento6.objects.create(projeto=self.arquitetura)
        c = Client()
        response = c.get('/admin/canarius/relacionamento6/1/delete')
        self.assertEqual(response.status_code, 301)

    class ProjetoDadosTest(TestCase):
        def setUp(self):
            self.arquitetura = Arquitetura.objects.create(nome="nome", descricao="descricao", introducao="introducao",
                                                  objetivo="objetivo")
        def test_nome_maxcaracteres(self):
            self.assertTrue(len(self.arquitetura.nome) <= 200)

        def test_nome_vazio(self):
            self.assertTrue(len(self.arquitetura.nome) != 0)

        def test_descricao_vazio(self):
            self.assertTrue(len(self.arquitetura.descricao) != 0)

        def test_introducao_vazio(self):
            self.assertTrue(len(self.arquitetura.introducao) != 0)

        def test_objetivo_vazio(self):
            self.assertTrue(len(self.arquitetura.objetivo) != 0)



##################################################testes de campos######################################################

class TipoDecisaoDadosTest(TestCase):
    def setUp(self):
        self.tipoDecisao = TipoDecisao.objects.create(nome="tipo de decisao")

    def test_nome_maxcaracteres(self):
        self.assertTrue(len(self.tipoDecisao.nome) <= 255)

    def test_nome_vazio(self):
        self.assertTrue(len(self.tipoDecisao.nome) != 0)

class TipoPadraoDadosTest(TestCase):
    def setUp(self):
        self.tipoPadrao = TipoPadrao.objects.create(nome="tipo de padrao")

    def test_nome_maxcaracteres(self):
        self.assertTrue(len(self.tipoPadrao.nome) <= 255)

    def test_nome_vazio(self):
        self.assertTrue(len(self.tipoPadrao.nome) != 0)


class DecisaoDadosTest(TestCase):
    def setUp(self):
        self.tipoPadrao = TipoPadrao.objects.create(nome="padrao")
        self.tipoDecisao = TipoDecisao.objects.create(nome="tipo de decisao")
        self.decisao = Decisao.objects.create(nome="decisao", descricao="descricao", objetivo="objetivo", motivacao="motivacao",
                                                tipoDeDecisao=self.tipoDecisao, escopo="escopo", hipoteses="hipoteses", restricoes="restricoes",
                                                alternativas="alternativas", implicacoes="implicacoes", necessidades="necessidades",
                                                notas="notas", estado='Aprovado')
        self.decisao.categorias.create(nome="tagdecisao")

    def test_nome_maxcaracteres(self):
        self.assertTrue(len(self.decisao.nome) <= 255)

    def test_nome_vazio(self):
        self.assertTrue(len(self.decisao.nome) != 0)

    def test_descricao_vazio(self):
        self.assertTrue(len(self.decisao.descricao) != 0)

    def test_objetivo_vazio(self):
        self.assertTrue(len(self.decisao.objetivo) != 0)

    def test_motivacao_vazio(self):
        self.assertTrue(len(self.decisao.motivacao) != 0)

    def test_escopo_vazio(self):
        self.assertTrue(len(self.decisao.escopo) != 0)

    def test_hipoteses_vazio(self):
        self.assertTrue(len(self.decisao.hipoteses) != 0)

    def test_restricoes_vazio(self):
        self.assertTrue(len(self.decisao.restricoes) != 0)

    def test_alternativas_vazio(self):
        self.assertTrue(len(self.decisao.alternativas) != 0)

    def test_implicacoes_vazio(self):
        self.assertTrue(len(self.decisao.implicacoes) != 0)

    def test_necessidades_vazio(self):
        self.assertTrue(len(self.decisao.necessidades) != 0)

    def test_notas_vazio(self):
        self.assertTrue(len(self.decisao.notas) != 0)

class PadraoDadosTest(TestCase):

    def setUp(self):
        self.tipoPadrao = TipoPadrao.objects.create(nome="padrao")
        self.padrao = Padrao.objects.create(nome="padrao", aliase="aliase", contexto="contexto",
                                            problema="problema", vantagens="vantagens", desvantagens="desvantagens",
                                            aplicabilidade="aplicabilidade", referencias="referencias",
                                            tipoDePadrao=self.tipoPadrao)


    def test_nome_maxcaracteres(self):
        self.assertTrue(len(self.padrao.nome) <= 255)

    def test_nome_vazio(self):
        self.assertTrue(len(self.padrao.nome) != 0)

    def test_aliase_vazio(self):
        self.assertTrue(len(self.padrao.aliase) != 0)

    def test_contexto_vazio(self):
        self.assertTrue(len(self.padrao.contexto) != 0)

    def test_problema_vazio(self):
        self.assertTrue(len(self.padrao.problema) != 0)

    def test_vantagens_vazio(self):
        self.assertTrue(len(self.padrao.nome) != 0)

    def test_desvantagens_vazio(self):
        self.assertTrue(len(self.padrao.desvantagens) != 0)

    def test_aplicabilidade_vazio(self):
        self.assertTrue(len(self.padrao.aplicabilidade) != 0)

    def test_referencias_vazio(self):
        self.assertTrue(len(self.padrao.referencias) != 0)

class TestTagPadraoDados(TestCase):
    def setUp(self):
        self.tagPadrao = TagPadrao.objects.create(nome="tag de padrao")

    def test_nome_maxcaracteres(self):
        self.assertTrue(len(self.tagPadrao.nome) <= 255)

    def test_nome_vazio(self):
        self.assertTrue(len(self.tagPadrao.nome) != 0)

class TestTagDecisaoDados(TestCase):
    def setUp(self):
        self.tagDecisao = TagDecisao.objects.create(nome="tag de padrao")

    def test_nome_maxcaracteres(self):
        self.assertTrue(len(self.tagDecisao.nome) <= 255)

    def test_nome_vazio(self):
        self.assertTrue(len(self.tagDecisao.nome) != 0)