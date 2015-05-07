from django.test import TestCase, Client
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
from sirius.models import StakeHoldersBehavioral
from sirius.models import ModeloArquiteturaAvaliacao
from sirius.models import ModuloCatalog
from sirius.models import Tecnologias
from sirius.models import ComponenteModulo
from sirius.models import TradeOff
from sirius.models import Referencia
from django.core.files import File
import unittest

class EstiloTesteNegativo(TestCase):
	def create_estilo_negativo(self):
		self.apresentacao = Apresentacao.objects.create(diagrama_de_sequencia="C:\img\teste.jpg", descricao="descricao")
		self.visao_de_implementacao = VisaoImplementacao.objects.create(visao_atual="visao_atual", apresentacao_de_implementacao=self.apresentacao)    
		self.descricao_visao_atual= DescricaoVisaoAtual.objects.create(visao_atual="visao_atual", tipo_de_elementos="tipo_de_elementos", relacao_de_elementos="relacao_de_elementos", propriedades="propriedades", restricoes="restricoes")         
		self.visao_comportamental = VisaoBehavioral.objects.create(descricao_do_comportamento_de_dominio="descricao_do_comportamento_de_dominio", diagrama_do_comportamento="C:\img\teste.jpg", visao_atual=self.descricao_visao_atual, apresentacao_behavioral=self.apresentacao)
		self.modulo_catalog = ModuloCatalog.objects.create(nome="nome", digrama_modulo="C:\img\teste.jpg", descricao_de_modulo = "descricao_de_modulo")
		self.apresentacao_modulo = ApresentacaoModulo.objects.create(modulos="modulo", relacionamento_dos_modulos="relacionamento_dos_modulos")
		self.diretriz = Diretriz.objects.create(diretriz="diretriz")    
		self.modelo_arquitetura = ModeloArquitetura.objects.create(nome="nome", introducao="introducao", drives_arquitetonicos="drives_arquitetonicos",  visao_comportamental = self.visao_comportamental, visao_de_implementacao=self.visao_de_implementacao, visao_atual=self.descricao_visao_atual, modulo_catalog=self.modulo_catalog, apresentacao_modulo=self.apresentacao_modulo, diretriz=self.diretriz, cliques=2) 
		return Estilo.objects.create(estilo="estiloestwiloestiloestiloestiloestiloestiloestiloestiloestiloestiloestiloestiloestiloestiloestiloestiloestiloestiloestiloestiloestiloestiloestiloestiloestiloestiloestiloestiloestiloestiloestiloestiloest",
									abordagem="abordagemabordagemabordagemabordagemabordagemabordagemabordagemabordagemabordagemabordagemabordagemabordagemabordagemabordagemabordagemabordagemabordagemabordagemabordagemabordagemabordagemabordagemabordagem", 
									justificativa="justificativajustificativajustificativajustificativajustificativajustificativajustificativajustificativajustificativajustificativajustificativajustificativajustificativajustificativajustificativajustificativa", 
									modeloArquitetura=self.modelo_arquitetura)
	def test_estilo_negativo(self):	
		self.assertTrue(len(self.create_estilo_negativo().estilo) <= 200)
	def test_abordagem_negativo(self):
		self.assertTrue(len(self.create_estilo_negativo().abordagem) <= 200)
	def test_justificativa_negativo(self):
		self.assertTrue(len(self.create_estilo_negativo().justificativa) <= 200)

class EstiloTestePositivo(TestCase):
	def create_estilo_positivo(self):
		self.apresentacao = Apresentacao.objects.create(diagrama_de_sequencia="C:\img\teste.jpg", descricao="descricao")
		self.visao_de_implementacao = VisaoImplementacao.objects.create(visao_atual="visao_atual", apresentacao_de_implementacao=self.apresentacao)    
		self.descricao_visao_atual= DescricaoVisaoAtual.objects.create(visao_atual="visao_atual", tipo_de_elementos="tipo_de_elementos", relacao_de_elementos="relacao_de_elementos", propriedades="propriedades", restricoes="restricoes")         
		self.visao_comportamental = VisaoBehavioral.objects.create(descricao_do_comportamento_de_dominio="descricao_do_comportamento_de_dominio", diagrama_do_comportamento="C:\img\teste.jpg", visao_atual=self.descricao_visao_atual, apresentacao_behavioral=self.apresentacao)
		self.modulo_catalog = ModuloCatalog.objects.create(nome="nome", digrama_modulo="C:\img\teste.jpg", descricao_de_modulo = "descricao_de_modulo")
		self.apresentacao_modulo = ApresentacaoModulo.objects.create(modulos="modulo", relacionamento_dos_modulos="relacionamento_dos_modulos")
		self.diretriz = Diretriz.objects.create(diretriz="diretriz")    
		self.modelo_arquitetura = ModeloArquitetura.objects.create(nome="nome", introducao="introducao", drives_arquitetonicos="drives_arquitetonicos",  visao_comportamental = self.visao_comportamental, visao_de_implementacao=self.visao_de_implementacao, visao_atual=self.descricao_visao_atual, modulo_catalog=self.modulo_catalog, apresentacao_modulo=self.apresentacao_modulo, diretriz=self.diretriz, cliques=2) 
		return Estilo.objects.create(estilo="estilo", abordagem="abordagem", justificativa="justificativa", modeloArquitetura=self.modelo_arquitetura)
	def test_estilo_positivo(self):	
		self.assertTrue(len(self.create_estilo_positivo().estilo) <= 200)
	def test_abordagem_positivo(self):
		self.assertTrue(len(self.create_estilo_positivo().abordagem) <= 200)
	def test_justificativa_positivo(self):
		self.assertTrue(len(self.create_estilo_positivo().justificativa) <= 200)
		
#teste de campo em branco positivo
class DescricaoVisaoAtualTestePositivo(TestCase):
    def create_descricao_visao_atual(self):
        return DescricaoVisaoAtual.objects.create(visao_atual="visao_atual", tipo_de_elementos="tipo_de_elementos", relacao_de_elementos="relacao_de_elementos", propriedades="propriedades", restricoes="restricoes")         
    def test_visao_atual_positivo(self):
        self.assertTrue(len(self.create_descricao_visao_atual().visao_atual) != 0)
    def test_tipos_de_elementos_positivo(self):
        self.assertTrue(len(self.create_descricao_visao_atual().tipo_de_elementos) != 0)
    def test_relacao_de_elementos_positivo(self):
        self.assertTrue(len(self.create_descricao_visao_atual().relacao_de_elementos) != 0)
    def test_propriedades_positivo(self):
        self.assertTrue(len(self.create_descricao_visao_atual().propriedades) != 0)
    def test_restricoes_positivo(self):
        self.assertTrue(len(self.create_descricao_visao_atual().restricoes) != 0)

#teste de campo em branco negativo
class DescricaoVisaoAtualNegativo(TestCase):
    def create_descricao_visao_atual(self):
        return DescricaoVisaoAtual.objects.create(visao_atual="", tipo_de_elementos="", relacao_de_elementos="", propriedades="", restricoes="")
    def test_visao_atual_positivo(self):
        self.assertTrue(len(self.create_descricao_visao_atual().visao_atual) != 0)
    def test_tipos_de_elementos_positivo(self):
        self.assertTrue(len(self.create_descricao_visao_atual().tipo_de_elementos) != 0)
    def test_relacao_de_elementos_positivo(self):
        self.assertTrue(len(self.create_descricao_visao_atual().relacao_de_elementos) != 0)
    def test_propriedades_positivo(self):
        self.assertTrue(len(self.create_descricao_visao_atual().propriedades) != 0)
    def test_restricoes_positivo(self):
        self.assertTrue(len(self.create_descricao_visao_atual().restricoes) != 0) 

class VisaoBehavioralTestePositivo(TestCase):
	def create_visao_behavioral(self):
		self.apresentacao = Apresentacao.objects.create(diagrama_de_sequencia="C:\img\teste.jpg", descricao="descricao")
		self.descricao_visao_atual= DescricaoVisaoAtual.objects.create(visao_atual="visao_atual", tipo_de_elementos="tipo_de_elementos", relacao_de_elementos="relacao_de_elementos", propriedades="propriedades", restricoes="restricoes")			
		return VisaoBehavioral.objects.create(descricao_do_comportamento_de_dominio="descricao_do_comportamento_de_dominio", diagrama_do_comportamento="C:\img\teste.jpg", visao_atual=self.descricao_visao_atual, apresentacao_behavioral=self.apresentacao)
	def test_descricao_positivo(self):
		self.assertTrue(len(self.create_visao_behavioral().descricao_do_comportamento_de_dominio) != 0)

class VisaoBehavioralTesteNegativo(TestCase):
	def create_visao_behavioral(self):
		self.apresentacao = Apresentacao.objects.create(diagrama_de_sequencia="C:\img\teste.jpg", descricao="descricao")
		self.descricao_visao_atual= DescricaoVisaoAtual.objects.create(visao_atual="visao_atual", tipo_de_elementos="tipo_de_elementos", relacao_de_elementos="relacao_de_elementos", propriedades="propriedades", restricoes="restricoes")			
		return VisaoBehavioral.objects.create(descricao_do_comportamento_de_dominio="", diagrama_do_comportamento="C:\img\teste.jpg", visao_atual=self.descricao_visao_atual, apresentacao_behavioral=self.apresentacao)
	def test_descricao_negativo(self):
		self.assertTrue(len(self.create_visao_behavioral().descricao_do_comportamento_de_dominio) != 0)
	
class StakeHoldersBehavioralTestePositivo(TestCase):
	def create_stakeholders_behavioral(self):
		self.apresentacao = Apresentacao.objects.create(diagrama_de_sequencia="C:\img\teste.jpg", descricao="descricao")
		self.descricao_visao_atual= DescricaoVisaoAtual.objects.create(visao_atual="visao_atual", tipo_de_elementos="tipo_de_elementos", relacao_de_elementos="relacao_de_elementos", propriedades="propriedades", restricoes="restricoes")	
		self.visao_comportamental= VisaoBehavioral.objects.create(descricao_do_comportamento_de_dominio="descricao_do_comportamento_de_dominio", diagrama_do_comportamento="C:\img\teste.jpg", visao_atual=self.descricao_visao_atual, apresentacao_behavioral=self.apresentacao)
		return StakeHoldersBehavioral.objects.create(stakeholders="stakeholders", precupacoes="precupacoes", nivel_detalhe_da_visao="nivel_detalhe_da_visao", visao_behavioral=self.visao_comportamental)
	def test_stakeholders_positivo(self):
		self.assertTrue(len(self.create_stakeholders_behavioral().stakeholders) <= 150)
	def test_preocupacoes_positivo(self):
		self.assertTrue(len(self.create_stakeholders_behavioral().precupacoes) <= 300)
	def test_nivel_detalhe_positivo(self):
		self.assertTrue(len(self.create_stakeholders_behavioral().nivel_detalhe_da_visao) != 0)	

class StakeHoldersBehavioralTesteNegativo(TestCase):
	def create_stakeholders_behavioral(self):
		self.apresentacao = Apresentacao.objects.create(diagrama_de_sequencia="C:\img\teste.jpg", descricao="descricao")
		self.descricao_visao_atual= DescricaoVisaoAtual.objects.create(visao_atual="visao_atual", tipo_de_elementos="tipo_de_elementos", relacao_de_elementos="relacao_de_elementos", propriedades="propriedades", restricoes="restricoes")	
		self.visao_comportamental= VisaoBehavioral.objects.create(descricao_do_comportamento_de_dominio="descricao_do_comportamento_de_dominio", diagrama_do_comportamento="C:\img\teste.jpg", visao_atual=self.descricao_visao_atual, apresentacao_behavioral=self.apresentacao)
		return StakeHoldersBehavioral.objects.create(stakeholders="stakeholdersstakeholdersstakeholdersstakeholdersstakeholdersstakeholdersstakeholdersstakeholdersstakeholdersstakeholdersstakeholdersstakeholdersstakeholdersstakeholdersstakeholdersstakeholdersstakeholders", 
													precupacoes="precupacoesprecupacoesprecupacoesprecupacoesprecupacoesprecupacoesprecupacoesprecupacoesprecupacoesprecupacoesprecupacoesprecupacoesprecupacoesprecupacoesprecupacoesprecupacoesprecupacoesprecupacoesprecupacoesprecupacoesprecupacoesprecupacoesprecupacoesprecupacoesprecupacoesprecupacoesprecupacoesprecupacoes", 
													nivel_detalhe_da_visao="", 
													visao_behavioral=self.visao_comportamental)
	def test_stakeholders_negativo(self):
		self.assertTrue(len(self.create_stakeholders_behavioral().stakeholders) <= 150)
	def test_preocupacoes_negativo(self):
		self.assertTrue(len(self.create_stakeholders_behavioral().precupacoes) <= 300)
	def test_nivel_detalhe_negativo(self):
		self.assertTrue(len(self.create_stakeholders_behavioral().nivel_detalhe_da_visao) != 0)			
		
class ModuloCatalogTestePositivo(TestCase):
	def create_modulo_catalog(self):
		return ModuloCatalog.objects.create(nome="nome", digrama_modulo="C:\img\teste.jpg", descricao_de_modulo = "descricao_de_modulo")
	def test_modulo_nome_positivo(self):
		self.assertTrue(len(self.create_modulo_catalog().nome) <= 150)
	def test_descricao_modulo_positivo(self):
		self.assertTrue(len(self.create_modulo_catalog().descricao) != 0)
		
class ModuloCatalogTestePositivo(TestCase):
	def create_modulo_catalog(self):
		return ModuloCatalog.objects.create(nome="nomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenome",
											digrama_modulo="C:\img\teste.jpg", descricao_de_modulo = "")
	def test_modulo_nome_positivo(self):
		self.assertTrue(len(self.create_modulo_catalog().nome) <= 150)
	def test_descricao_modulo_positivo(self):
		self.assertTrue(len(self.create_modulo_catalog().descricao_de_modulo) != 0)

class ApresentacaoModuloTestePositivo(TestCase):
	def create_apresentacao_modulo(self):
		return ApresentacaoModulo.objects.create(modulos="modulo", relacionamento_dos_modulos="relacionamento_dos_modulos")
	def test_modulo_positivo(self):
		self.assertTrue(len(self.create_apresentacao_modulo().modulos) <= 150)
	def test_relacionamento_positivo(self):
		self.assertTrue(len(self.create_apresentacao_modulo().relacionamento_dos_modulos) != 0)
		
class ApresentacaoModuloTesteNegativo(TestCase):
	def create_apresentacao_modulo(self):
		return ApresentacaoModulo.objects.create(modulos="modulomodulomodulomodulomodulomodulomodulomodulomodulomodulomodulomodulomodulomodulomodulomodulomodulomodulomodulomodulomodulomodulomodulomodulomodulomodulo",
												relacionamento_dos_modulos="")
	def test_modulo_positivo(self):
		self.assertTrue(len(self.create_apresentacao_modulo().modulos) <= 150)
	def test_relacionamento_positivo(self):
		self.assertTrue(len(self.create_apresentacao_modulo().relacionamento_dos_modulos) != 0)

class ModeloArquiteturaTestePositivo(TestCase):
	def create_modelo_arquitetura(self):
		self.apresentacao = Apresentacao.objects.create(diagrama_de_sequencia="C:\img\teste.jpg", descricao="descricao")
		self.visao_de_implementacao = VisaoImplementacao.objects.create(visao_atual="visao_atual", apresentacao_de_implementacao=self.apresentacao)			
		self.descricao_visao_atual= DescricaoVisaoAtual.objects.create(visao_atual="visao_atual", tipo_de_elementos="tipo_de_elementos", relacao_de_elementos="relacao_de_elementos", propriedades="propriedades", restricoes="restricoes")			
		self.visao_comportamental = VisaoBehavioral.objects.create(descricao_do_comportamento_de_dominio="descricao_do_comportamento_de_dominio", diagrama_do_comportamento="C:\img\teste.jpg", visao_atual=self.descricao_visao_atual, apresentacao_behavioral=self.apresentacao)
		self.modulo_catalog = ModuloCatalog.objects.create(nome="nome", digrama_modulo="C:\img\teste.jpg", descricao_de_modulo = "descricao_de_modulo")
		self.apresentacao_modulo = ApresentacaoModulo.objects.create(modulos="modulo", relacionamento_dos_modulos="relacionamento_dos_modulos")
		self.diretriz = Diretriz.objects.create(diretriz="diretriz")	
		return ModeloArquitetura.objects.create(nome="nome", introducao="introducao", drives_arquitetonicos="drives_arquitetonicos",  visao_comportamental = self.visao_comportamental, visao_de_implementacao=self.visao_de_implementacao, visao_atual=self.descricao_visao_atual, modulo_catalog=self.modulo_catalog, apresentacao_modulo=self.apresentacao_modulo, diretriz=self.diretriz)
	def test_nome_arquitetura_positivo(self):
		self.assertTrue(len(self.create_modelo_arquitetura().nome) <= 150)
	def test_introducao_positivo(self):
		self.assertTrue(len(self.create_modelo_arquitetura().introducao) != 0)
	def test_drivers_arquitetonicos_positivo(self):
		self.assertTrue(len(self.create_modelo_arquitetura().drives_arquitetonicos) != 0)
		
class ModeloArquiteturaTesteNegativo(TestCase):
	def create_modelo_arquitetura(self):
		self.apresentacao = Apresentacao.objects.create(diagrama_de_sequencia="C:\img\teste.jpg", descricao="descricao")
		self.visao_de_implementacao = VisaoImplementacao.objects.create(visao_atual="visao_atual", apresentacao_de_implementacao=self.apresentacao)			
		self.descricao_visao_atual= DescricaoVisaoAtual.objects.create(visao_atual="visao_atual", tipo_de_elementos="tipo_de_elementos", relacao_de_elementos="relacao_de_elementos", propriedades="propriedades", restricoes="restricoes")			
		self.visao_comportamental = VisaoBehavioral.objects.create(descricao_do_comportamento_de_dominio="descricao_do_comportamento_de_dominio", diagrama_do_comportamento="C:\img\teste.jpg", visao_atual=self.descricao_visao_atual, apresentacao_behavioral=self.apresentacao)
		self.modulo_catalog = ModuloCatalog.objects.create(nome="nome", digrama_modulo="C:\img\teste.jpg", descricao_de_modulo = "descricao_de_modulo")
		self.apresentacao_modulo = ApresentacaoModulo.objects.create(modulos="modulo", relacionamento_dos_modulos="relacionamento_dos_modulos")
		self.diretriz = Diretriz.objects.create(diretriz="diretriz")	
		return ModeloArquitetura.objects.create(nome="nomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenome", 
												introducao="", drives_arquitetonicos="",  visao_comportamental = self.visao_comportamental, visao_de_implementacao=self.visao_de_implementacao, visao_atual=self.descricao_visao_atual, modulo_catalog=self.modulo_catalog, apresentacao_modulo=self.apresentacao_modulo, diretriz=self.diretriz)
	def test_nome_arquitetura_negativo(self):
		self.assertTrue(len(self.create_modelo_arquitetura().nome) <= 150)
	def test_introducao_negativo(self):
		self.assertTrue(len(self.create_modelo_arquitetura().introducao) != 0)
	def test_drivers_arquitetonicos_negativo(self):
		self.assertTrue(len(self.create_modelo_arquitetura().drives_arquitetonicos) != 0)
	
class ModeloArquiteturaAvaliacaoTestePositivo(TestCase):
	def create_modelo_arquitetura_avaliacao(self):
		self.apresentacao = Apresentacao.objects.create(diagrama_de_sequencia="C:\img\teste.jpg", descricao="descricao")
		self.visao_de_implementacao = VisaoImplementacao.objects.create(visao_atual="visao_atual", apresentacao_de_implementacao=self.apresentacao)			
		self.descricao_visao_atual= DescricaoVisaoAtual.objects.create(visao_atual="visao_atual", tipo_de_elementos="tipo_de_elementos", relacao_de_elementos="relacao_de_elementos", propriedades="propriedades", restricoes="restricoes")			
		self.visao_comportamental = VisaoBehavioral.objects.create(descricao_do_comportamento_de_dominio="descricao_do_comportamento_de_dominio", diagrama_do_comportamento="C:\img\teste.jpg", visao_atual=self.descricao_visao_atual, apresentacao_behavioral=self.apresentacao)
		self.modulo_catalog = ModuloCatalog.objects.create(nome="nome", digrama_modulo="C:\img\teste.jpg", descricao_de_modulo = "descricao_de_modulo")
		self.apresentacao_modulo = ApresentacaoModulo.objects.create(modulos="modulo", relacionamento_dos_modulos="relacionamento_dos_modulos")
		self.diretriz = Diretriz.objects.create(diretriz="diretriz")	
		self.modelo_arquitetura = ModeloArquitetura.objects.create(nome="nome", introducao="introducao", drives_arquitetonicos="drives_arquitetonicos",  visao_comportamental = self.visao_comportamental, visao_de_implementacao=self.visao_de_implementacao, visao_atual=self.descricao_visao_atual, modulo_catalog=self.modulo_catalog, apresentacao_modulo=self.apresentacao_modulo, diretriz=self.diretriz, cliques=2)
		return ModeloArquiteturaAvaliacao.objects.create(modeloArquitetura=self.modelo_arquitetura, nome="nome", descricao_da_qualidade="descricao_da_qualidade", descricao_de_nao_riscos="descricao_de_nao_riscos", descricao_de_riscos="descricao_de_riscos", diagrama_de_arquitetura="C:\img\teste.jpg", descricao_da_arquitetura="descricao_da_arquitetura", pricipais_abordagens_da_arquitetura="pricipais_abordagens_da_arquitetura", ponto_de_sensibilidade="ponto_de_sensibilidade", restricao_de_sensibilidade="restricao_de_sensibilidade")
	def test_nome_avaliacao_positivo(self):
		self.assertTrue(len(self.create_modelo_arquitetura_avaliacao().nome) <= 150)
	def test_descricao_qualidade_avaliacao_positivo(self):
		self.assertTrue(len(self.create_modelo_arquitetura_avaliacao().descricao_da_qualidade) != 0)
	def test_descricao_nriscos_avaliacao_positivo(self):
		self.assertTrue(len(self.create_modelo_arquitetura_avaliacao().descricao_de_nao_riscos)!= 0)
	def test_descricao_riscos_avaliacao_positivo(self):
		self.assertTrue(len(self.create_modelo_arquitetura_avaliacao().descricao_de_riscos) != 0)
	def test_descricao_arquitetura_avaliacao_positivo(self):
		self.assertTrue(len(self.create_modelo_arquitetura_avaliacao().descricao_da_arquitetura) != 0)
	def test_abordagem_avaliacao_positivo(self):
		self.assertTrue(len(self.create_modelo_arquitetura_avaliacao().pricipais_abordagens_da_arquitetura) != 0)
	def test_ponto_sensibilidade_avaliacao_positivo(self):
		self.assertTrue(len(self.create_modelo_arquitetura_avaliacao().ponto_de_sensibilidade) != 0)
	def test_restricao_sensibilidade_avaliacao_positivo(self):
		self.assertTrue(len(self.create_modelo_arquitetura_avaliacao().restricao_de_sensibilidade) != 0)
		
class ModeloArquiteturaAvaliacaoTesteNegativo(TestCase):
	def create_modelo_arquitetura_avaliacao(self):
		self.apresentacao = Apresentacao.objects.create(diagrama_de_sequencia="C:\img\teste.jpg", descricao="descricao")
		self.visao_de_implementacao = VisaoImplementacao.objects.create(visao_atual="visao_atual", apresentacao_de_implementacao=self.apresentacao)			
		self.descricao_visao_atual= DescricaoVisaoAtual.objects.create(visao_atual="visao_atual", tipo_de_elementos="tipo_de_elementos", relacao_de_elementos="relacao_de_elementos", propriedades="propriedades", restricoes="restricoes")			
		self.visao_comportamental = VisaoBehavioral.objects.create(descricao_do_comportamento_de_dominio="descricao_do_comportamento_de_dominio", diagrama_do_comportamento="C:\img\teste.jpg", visao_atual=self.descricao_visao_atual, apresentacao_behavioral=self.apresentacao)
		self.modulo_catalog = ModuloCatalog.objects.create(nome="nome", digrama_modulo="C:\img\teste.jpg", descricao_de_modulo = "descricao_de_modulo")
		self.apresentacao_modulo = ApresentacaoModulo.objects.create(modulos="modulo", relacionamento_dos_modulos="relacionamento_dos_modulos")
		self.diretriz = Diretriz.objects.create(diretriz="diretriz")	
		self.modelo_arquitetura = ModeloArquitetura.objects.create(nome="nome", introducao="introducao", drives_arquitetonicos="drives_arquitetonicos",  visao_comportamental = self.visao_comportamental, visao_de_implementacao=self.visao_de_implementacao, visao_atual=self.descricao_visao_atual, modulo_catalog=self.modulo_catalog, apresentacao_modulo=self.apresentacao_modulo, diretriz=self.diretriz, cliques=2)
		return ModeloArquiteturaAvaliacao.objects.create(modeloArquitetura=self.modelo_arquitetura, nome="nomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenome", 
														descricao_da_qualidade="", descricao_de_nao_riscos="", descricao_de_riscos="", diagrama_de_arquitetura="C:\img\teste.jpg", descricao_da_arquitetura="", pricipais_abordagens_da_arquitetura="", ponto_de_sensibilidade="", restricao_de_sensibilidade="")
	def test_nome_avaliacao_negativo(self):
		self.assertTrue(len(self.create_modelo_arquitetura_avaliacao().nome) <= 150)
	def test_descricao_qualidade_avaliacao_negativo(self):
		self.assertTrue(len(self.create_modelo_arquitetura_avaliacao().descricao_da_qualidade) != 0)
	def test_descricao_nriscos_avaliacao_negativo(self):
		self.assertTrue(len(self.create_modelo_arquitetura_avaliacao().descricao_de_nao_riscos)!= 0)
	def test_descricao_riscos_avaliacao_negativo(self):
		self.assertTrue(len(self.create_modelo_arquitetura_avaliacao().descricao_de_riscos) != 0)
	def test_descricao_arquitetura_avaliacao_negativo(self):
		self.assertTrue(len(self.create_modelo_arquitetura_avaliacao().descricao_da_arquitetura) != 0)
	def test_abordagem_avaliacao_negativo(self):
		self.assertTrue(len(self.create_modelo_arquitetura_avaliacao().pricipais_abordagens_da_arquitetura) != 0)
	def test_ponto_sensibilidade_avaliacao_negativo(self):
		self.assertTrue(len(self.create_modelo_arquitetura_avaliacao().ponto_de_sensibilidade) != 0)
	def test_restricao_sensibilidade_avaliacao_negativo(self):
		self.assertTrue(len(self.create_modelo_arquitetura_avaliacao().restricao_de_sensibilidade) != 0)
	
class TecnologiasTestePositivo(TestCase):
	def create_tecnologias(self):
		self.apresentacao = Apresentacao.objects.create(diagrama_de_sequencia="C:\img\teste.jpg", descricao="descricao")
		self.visao_de_implementacao = VisaoImplementacao.objects.create(visao_atual="visao_atual", apresentacao_de_implementacao=self.apresentacao)			
		self.descricao_visao_atual= DescricaoVisaoAtual.objects.create(visao_atual="visao_atual", tipo_de_elementos="tipo_de_elementos", relacao_de_elementos="relacao_de_elementos", propriedades="propriedades", restricoes="restricoes")			
		self.visao_comportamental = VisaoBehavioral.objects.create(descricao_do_comportamento_de_dominio="descricao_do_comportamento_de_dominio", diagrama_do_comportamento="C:\img\teste.jpg", visao_atual=self.descricao_visao_atual, apresentacao_behavioral=self.apresentacao)
		self.modulo_catalog = ModuloCatalog.objects.create(nome="nome", digrama_modulo="C:\img\teste.jpg", descricao_de_modulo = "descricao_de_modulo")
		self.apresentacao_modulo = ApresentacaoModulo.objects.create(modulos="modulo", relacionamento_dos_modulos="relacionamento_dos_modulos")
		self.diretriz = Diretriz.objects.create(diretriz="diretriz")	
		self.modelo_arquitetura = ModeloArquitetura.objects.create(nome="nome", introducao="introducao", drives_arquitetonicos="drives_arquitetonicos",  visao_comportamental = self.visao_comportamental, visao_de_implementacao=self.visao_de_implementacao, visao_atual=self.descricao_visao_atual, modulo_catalog=self.modulo_catalog, apresentacao_modulo=self.apresentacao_modulo, diretriz=self.diretriz)
		return Tecnologias.objects.create (tecnologia="tecnologia", justificativa="justificativa", modeloArquitetura=self.modelo_arquitetura)
	def test_tecnologia_positivo(self):
		self.assertTrue(len(self.create_tecnologias().tecnologia) <= 200)
	def test_justificativa_positivo(self):
		self.assertTrue(len(self.create_tecnologias().justificativa) != 0)
		
class TecnologiasTesteNegativo(TestCase):
	def create_tecnologias(self):
		self.apresentacao = Apresentacao.objects.create(diagrama_de_sequencia="C:\img\teste.jpg", descricao="descricao")
		self.visao_de_implementacao = VisaoImplementacao.objects.create(visao_atual="visao_atual", apresentacao_de_implementacao=self.apresentacao)			
		self.descricao_visao_atual= DescricaoVisaoAtual.objects.create(visao_atual="visao_atual", tipo_de_elementos="tipo_de_elementos", relacao_de_elementos="relacao_de_elementos", propriedades="propriedades", restricoes="restricoes")			
		self.visao_comportamental = VisaoBehavioral.objects.create(descricao_do_comportamento_de_dominio="descricao_do_comportamento_de_dominio", diagrama_do_comportamento="C:\img\teste.jpg", visao_atual=self.descricao_visao_atual, apresentacao_behavioral=self.apresentacao)
		self.modulo_catalog = ModuloCatalog.objects.create(nome="nome", digrama_modulo="C:\img\teste.jpg", descricao_de_modulo = "descricao_de_modulo")
		self.apresentacao_modulo = ApresentacaoModulo.objects.create(modulos="modulo", relacionamento_dos_modulos="relacionamento_dos_modulos")
		self.diretriz = Diretriz.objects.create(diretriz="diretriz")	
		self.modelo_arquitetura = ModeloArquitetura.objects.create(nome="nome", introducao="introducao", drives_arquitetonicos="drives_arquitetonicos",  visao_comportamental = self.visao_comportamental, visao_de_implementacao=self.visao_de_implementacao, visao_atual=self.descricao_visao_atual, modulo_catalog=self.modulo_catalog, apresentacao_modulo=self.apresentacao_modulo, diretriz=self.diretriz)
		return Tecnologias.objects.create (tecnologia="tecnologiatecnologiatecnologiatecnologiatecnologiatecnologiatecnologiatecnologiatecnologiatecnologiatecnologiatecnologiatecnologiatecnologiatecnologiatecnologiatecnologiatecnologiatecnologiatecnologiatecnologia",
											justificativa="", modeloArquitetura=self.modelo_arquitetura)
	def test_tecnologia_negativo(self):
		self.assertTrue(len(self.create_tecnologias().tecnologia) <= 200)
	def test_justificativa_negativo(self):
		self.assertTrue(len(self.create_tecnologias().justificativa) != 0)
		
class ComponenteModuloTestePositivo(TestCase):
	def create_componente_modulo(self):
		self.diretriz = Diretriz.objects.create(diretriz="diretriz")	
		self.modulo_catalog = ModuloCatalog.objects.create(nome="nome", digrama_modulo="C:\img\teste.jpg", descricao_de_modulo = "descricao_de_modulo")
		return ComponenteModulo.objects.create(diagrama_do_componente="C:\img\teste.jpg", descricao_do_componente="descricao_do_componente", funcionalidades_relacionadas="funcionalidades_relacionadas", diretriz=self.diretriz, moduloCatalog=self.modulo_catalog)
	def test_descricao_positivo(self):
		self.assertTrue(len(self.create_componente_modulo().descricao_do_componente) != 0)
	def test_funcionalidade_positivo(self):
		self.assertTrue(len(self.create_componente_modulo().funcionalidades_relacionadas) <= 300)
		
class ComponenteModuloTesteNegativo(TestCase):
	def create_componente_modulo(self):
		self.diretriz = Diretriz.objects.create(diretriz="diretriz")	
		self.modulo_catalog = ModuloCatalog.objects.create(nome="nome", digrama_modulo="C:\img\teste.jpg", descricao_de_modulo = "descricao_de_modulo")
		return ComponenteModulo.objects.create(diagrama_do_componente="C:\img\teste.jpg", 
											descricao_do_componente="", 
											funcionalidades_relacionadas="funcionalidades_relacionadasfuncionalidades_relacionadasfuncionalidades_relacionadasfuncionalidades_relacionadasfuncionalidades_relacionadasfuncionalidades_relacionadasfuncionalidades_relacionadasfuncionalidades_relacionadasfuncionalidades_relacionadasfuncionalidades_relacionadasfuncionalidades_relacionadas", 
											diretriz=self.diretriz, moduloCatalog=self.modulo_catalog)
	def test_descricao_negativo(self):
		self.assertTrue(len(self.create_componente_modulo().descricao_do_componente) != 0)
	def test_funcionalidade_negativo(self):
		self.assertTrue(len(self.create_componente_modulo().funcionalidades_relacionadas) <= 300)
		
class TradeOffTestePositivo(TestCase):
	def create_trade_off(self):
		self.apresentacao = Apresentacao.objects.create(diagrama_de_sequencia="C:\img\teste.jpg", descricao="descricao")
		self.visao_de_implementacao = VisaoImplementacao.objects.create(visao_atual="visao_atual", apresentacao_de_implementacao=self.apresentacao)			
		self.descricao_visao_atual= DescricaoVisaoAtual.objects.create(visao_atual="visao_atual", tipo_de_elementos="tipo_de_elementos", relacao_de_elementos="relacao_de_elementos", propriedades="propriedades", restricoes="restricoes")			
		self.visao_comportamental = VisaoBehavioral.objects.create(descricao_do_comportamento_de_dominio="descricao_do_comportamento_de_dominio", diagrama_do_comportamento="C:\img\teste.jpg", visao_atual=self.descricao_visao_atual, apresentacao_behavioral=self.apresentacao)
		self.modulo_catalog = ModuloCatalog.objects.create(nome="nome", digrama_modulo="C:\img\teste.jpg", descricao_de_modulo = "descricao_de_modulo")
		self.apresentacao_modulo = ApresentacaoModulo.objects.create(modulos="modulo", relacionamento_dos_modulos="relacionamento_dos_modulos")
		self.diretriz = Diretriz.objects.create(diretriz="diretriz")	
		self.modelo_arquitetura = ModeloArquitetura.objects.create(nome="nome", introducao="introducao", drives_arquitetonicos="drives_arquitetonicos",  visao_comportamental = self.visao_comportamental, visao_de_implementacao=self.visao_de_implementacao, visao_atual=self.descricao_visao_atual, modulo_catalog=self.modulo_catalog, apresentacao_modulo=self.apresentacao_modulo, diretriz=self.diretriz, cliques=2)
		self.modelo_arquitetura_avaliacao = ModeloArquiteturaAvaliacao.objects.create(modeloArquitetura=self.modelo_arquitetura, nome="nome", descricao_da_qualidade="descricao_da_qualidade", descricao_de_nao_riscos="descricao_de_nao_riscos", descricao_de_riscos="descricao_de_riscos", diagrama_de_arquitetura="C:\img\teste.jpg", descricao_da_arquitetura="descricao_da_arquitetura", pricipais_abordagens_da_arquitetura="pricipais_abordagens_da_arquitetura", ponto_de_sensibilidade="ponto_de_sensibilidade", restricao_de_sensibilidade="restricao_de_sensibilidade")		
		return TradeOff.objects.create(pontos_de_trade_off="pontos_de_trade_off", modeloArquitetura=self.modelo_arquitetura_avaliacao, diretriz=self.diretriz)
	def test_trade_off_positivo(self):
		self.assertTrue(len(self.create_trade_off().pontos_de_trade_off) !=0)
		
class TradeOffTesteNegativo(TestCase):
	def create_trade_off(self):
		self.apresentacao = Apresentacao.objects.create(diagrama_de_sequencia="C:\img\teste.jpg", descricao="descricao")
		self.visao_de_implementacao = VisaoImplementacao.objects.create(visao_atual="visao_atual", apresentacao_de_implementacao=self.apresentacao)			
		self.descricao_visao_atual= DescricaoVisaoAtual.objects.create(visao_atual="visao_atual", tipo_de_elementos="tipo_de_elementos", relacao_de_elementos="relacao_de_elementos", propriedades="propriedades", restricoes="restricoes")			
		self.visao_comportamental = VisaoBehavioral.objects.create(descricao_do_comportamento_de_dominio="descricao_do_comportamento_de_dominio", diagrama_do_comportamento="C:\img\teste.jpg", visao_atual=self.descricao_visao_atual, apresentacao_behavioral=self.apresentacao)
		self.modulo_catalog = ModuloCatalog.objects.create(nome="nome", digrama_modulo="C:\img\teste.jpg", descricao_de_modulo = "descricao_de_modulo")
		self.apresentacao_modulo = ApresentacaoModulo.objects.create(modulos="modulo", relacionamento_dos_modulos="relacionamento_dos_modulos")
		self.diretriz = Diretriz.objects.create(diretriz="diretriz")	
		self.modelo_arquitetura = ModeloArquitetura.objects.create(nome="nome", introducao="introducao", drives_arquitetonicos="drives_arquitetonicos",  visao_comportamental = self.visao_comportamental, visao_de_implementacao=self.visao_de_implementacao, visao_atual=self.descricao_visao_atual, modulo_catalog=self.modulo_catalog, apresentacao_modulo=self.apresentacao_modulo, diretriz=self.diretriz, cliques=2)
		self.modelo_arquitetura_avaliacao = ModeloArquiteturaAvaliacao.objects.create(modeloArquitetura=self.modelo_arquitetura, nome="nome", descricao_da_qualidade="descricao_da_qualidade", descricao_de_nao_riscos="descricao_de_nao_riscos", descricao_de_riscos="descricao_de_riscos", diagrama_de_arquitetura="C:\img\teste.jpg", descricao_da_arquitetura="descricao_da_arquitetura", pricipais_abordagens_da_arquitetura="pricipais_abordagens_da_arquitetura", ponto_de_sensibilidade="ponto_de_sensibilidade", restricao_de_sensibilidade="restricao_de_sensibilidade")		
		return TradeOff.objects.create(pontos_de_trade_off="", modeloArquitetura=self.modelo_arquitetura_avaliacao, diretriz=self.diretriz)
	def test_trade_off_negativo(self):
		self.assertTrue(len(self.create_trade_off().pontos_de_trade_off) !=0)

class ReferenciaTestePositivo(TestCase):
	def create_referencia(self):
		self.apresentacao = Apresentacao.objects.create(diagrama_de_sequencia="C:\img\teste.jpg", descricao="descricao")
		self.visao_de_implementacao = VisaoImplementacao.objects.create(visao_atual="visao_atual", apresentacao_de_implementacao=self.apresentacao)			
		self.descricao_visao_atual= DescricaoVisaoAtual.objects.create(visao_atual="visao_atual", tipo_de_elementos="tipo_de_elementos", relacao_de_elementos="relacao_de_elementos", propriedades="propriedades", restricoes="restricoes")			
		self.visao_comportamental = VisaoBehavioral.objects.create(descricao_do_comportamento_de_dominio="descricao_do_comportamento_de_dominio", diagrama_do_comportamento="C:\img\teste.jpg", visao_atual=self.descricao_visao_atual, apresentacao_behavioral=self.apresentacao)
		self.modulo_catalog = ModuloCatalog.objects.create(nome="nome", digrama_modulo="C:\img\teste.jpg", descricao_de_modulo = "descricao_de_modulo")
		self.apresentacao_modulo = ApresentacaoModulo.objects.create(modulos="modulo", relacionamento_dos_modulos="relacionamento_dos_modulos")
		self.diretriz = Diretriz.objects.create(diretriz="diretriz")	
		self.modelo_arquitetura = ModeloArquitetura.objects.create(nome="nome", introducao="introducao", drives_arquitetonicos="drives_arquitetonicos",  visao_comportamental = self.visao_comportamental, visao_de_implementacao=self.visao_de_implementacao, visao_atual=self.descricao_visao_atual, modulo_catalog=self.modulo_catalog, apresentacao_modulo=self.apresentacao_modulo, diretriz=self.diretriz)
		return Referencia.objects.create(referencia="referencia", modeloArquitetura=self.modelo_arquitetura)
	def test_referencia_positivo(self):
		self.assertTrue(len(self.create_referencia().referencia) <= 200)
		
class ReferenciaTesteNegativo(TestCase):
	def create_referencia(self):
		self.apresentacao = Apresentacao.objects.create(diagrama_de_sequencia="C:\img\teste.jpg", descricao="descricao")
		self.visao_de_implementacao = VisaoImplementacao.objects.create(visao_atual="visao_atual", apresentacao_de_implementacao=self.apresentacao)			
		self.descricao_visao_atual= DescricaoVisaoAtual.objects.create(visao_atual="visao_atual", tipo_de_elementos="tipo_de_elementos", relacao_de_elementos="relacao_de_elementos", propriedades="propriedades", restricoes="restricoes")			
		self.visao_comportamental = VisaoBehavioral.objects.create(descricao_do_comportamento_de_dominio="descricao_do_comportamento_de_dominio", diagrama_do_comportamento="C:\img\teste.jpg", visao_atual=self.descricao_visao_atual, apresentacao_behavioral=self.apresentacao)
		self.modulo_catalog = ModuloCatalog.objects.create(nome="nome", digrama_modulo="C:\img\teste.jpg", descricao_de_modulo = "descricao_de_modulo")
		self.apresentacao_modulo = ApresentacaoModulo.objects.create(modulos="modulo", relacionamento_dos_modulos="relacionamento_dos_modulos")
		self.diretriz = Diretriz.objects.create(diretriz="diretriz")	
		self.modelo_arquitetura = ModeloArquitetura.objects.create(nome="nome", introducao="introducao", drives_arquitetonicos="drives_arquitetonicos",  visao_comportamental = self.visao_comportamental, visao_de_implementacao=self.visao_de_implementacao, visao_atual=self.descricao_visao_atual, modulo_catalog=self.modulo_catalog, apresentacao_modulo=self.apresentacao_modulo, diretriz=self.diretriz)
		return Referencia.objects.create(referencia="referenciareferenciareferenciareferenciareferenciareferenciareferenciareferenciareferenciareferenciareferenciareferenciareferenciareferenciareferenciareferenciareferenciareferenciareferenciareferenciareferencia",
										modeloArquitetura=self.modelo_arquitetura)
	def test_referencia_negativo(self):
		self.assertTrue(len(self.create_referencia().referencia) <= 200)

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
class DiretrizTestePositivo(TestCase):
    def create_diretriz(self, diretriz="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam rutrum, nisl sed bibendum euismod, dui magna fringilla nibh, quis efficitur ante nunc nec augue. In sagittis ultrices felis id dapibus. Ae"):
        return Diretriz.objects.create(diretriz=diretriz)

    def test_diretriz_positivo(self):
        self.assertTrue(len(self.create_diretriz().diretriz) <= 200)

#teste de caracteres maximo negativo
class DiretrizTesteNegativo(TestCase):
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

###teste das urls###
class TestePaginaInicial(TestCase):			
	def test_url_admin(self):
		c = Client()
		response = c.get('/admin/')
		self.assertEqual(response.status_code, 200)

	def test_url_home(self):
		c = Client()
		response = c.get('/admin/sirius/')
		self.assertEqual(response.status_code, 200)
		
class TestePesquisa(TestCase):
	def test_url_pesquisa(self):
		c=Client()
		response = c.get('/pesquisa/')
		self.assertEqual(response.status_code, 200)
		
	def test_url_pesquisa_sirius(self):
		c=Client()
		response = c.get('/form_pesquisa_sirius/')
		self.assertEqual(response.status_code, 200)
		
		
class TesteUrlApresentacaoModulo(TestCase):
	def test_url_listagem(self):
		c = Client()
		response = c.get('/admin/sirius/apresentacaomodulo/')
		self.assertEqual(response.status_code, 200)
	
	def test_url_editar(self):
		self.apresentacao_modulo = ApresentacaoModulo.objects.create(modulos="modulo", relacionamento_dos_modulos="relacionamento_dos_modulos")
		c = Client()
		response = c.get('/admin/sirius/apresentacaomodulo/1/')
		self.assertEqual(response.status_code, 200)
		
	def test_url_criar(self):
		c = Client()
		response = c.get('/admin/sirius/apresentacaomodulo/add/')
		self.assertEqual(response.status_code, 200)
		
	def test_url_cadastrar(self):
		c = Client()
		response = c.post('/admin/sirius/apresentacaomodulo/add/', {'modulos': 'modulo', 'relacionamento_dos_modulos': 'relacionamento_dos_modulos'})
		self.assertEqual(response.status_code, 200)
	
class TesteUrlApresentacao(TestCase):
	def test_url_listagem(self):
		c = Client()
		response = c.get('/admin/sirius/apresentacao/')
		self.assertEqual(response.status_code, 200)
	
	def test_url_editar(self):
		self.apresentacao = Apresentacao.objects.create(diagrama_de_sequencia="C:\img\teste.jpg", descricao="descricao")
		c = Client()
		response = c.get('/admin/sirius/apresentacao/1/')
		self.assertEqual(response.status_code, 200)
		
	def test_url_criar(self):
		c = Client()
		response = c.get('/admin/sirius/apresentacao/add/')
		self.assertEqual(response.status_code, 200)

	def test_url_cadastrar(self):
		c = Client()
		response = c.post('/admin/sirius/apresentacao/add/', {'descricao':'descricao'})
		self.assertEqual(response.status_code, 200)

class TesteUrlDiretriz(TestCase):
	def test_url_listagem(self):
		c = Client()
		response = c.get('/admin/sirius/diretriz/')
		self.assertEqual(response.status_code, 200)
	
	def test_url_editar(self):
		self.diretriz = Diretriz.objects.create(diretriz="diretriz")	
		c = Client()
		response = c.get('/admin/sirius/diretriz/1/')
		self.assertEqual(response.status_code, 200)
		
	def test_url_criar(self):
		c = Client()
		response = c.get('/admin/sirius/diretriz/add/')
		self.assertEqual(response.status_code, 200)
		
	def test_url_cadastrar(self):
		c = Client()
		response = c.post('/admin/sirius/diretriz/add/', {'diretriz':'diretriz'})
		self.assertEqual(response.status_code, 200)
		
class TesteUrlModeloArquitetura(TestCase):
	def test_url_listagem(self):
		c = Client()
		response = c.get('/admin/sirius/modeloarquitetura/')
		self.assertEqual(response.status_code, 200)
	
	def test_url_editar(self):
		self.apresentacao = Apresentacao.objects.create(diagrama_de_sequencia="C:\img\teste.jpg", descricao="descricao")
		self.visao_de_implementacao = VisaoImplementacao.objects.create(visao_atual="visao_atual", apresentacao_de_implementacao=self.apresentacao)			
		self.descricao_visao_atual= DescricaoVisaoAtual.objects.create(visao_atual="visao_atual", tipo_de_elementos="tipo_de_elementos", relacao_de_elementos="relacao_de_elementos", propriedades="propriedades", restricoes="restricoes")			
		self.visao_comportamental = VisaoBehavioral.objects.create(descricao_do_comportamento_de_dominio="descricao_do_comportamento_de_dominio", diagrama_do_comportamento="C:\img\teste.jpg", visao_atual=self.descricao_visao_atual, apresentacao_behavioral=self.apresentacao)
		self.modulo_catalog = ModuloCatalog.objects.create(nome="nome", digrama_modulo="C:\img\teste.jpg", descricao_de_modulo = "descricao_de_modulo")
		self.apresentacao_modulo = ApresentacaoModulo.objects.create(modulos="modulo", relacionamento_dos_modulos="relacionamento_dos_modulos")
		self.diretriz = Diretriz.objects.create(diretriz="diretriz")	
		self.modelo_arquitetura = ModeloArquitetura.objects.create(nome="nome", introducao="introducao", drives_arquitetonicos="drives_arquitetonicos",  visao_comportamental = self.visao_comportamental, visao_de_implementacao=self.visao_de_implementacao, visao_atual=self.descricao_visao_atual, modulo_catalog=self.modulo_catalog, apresentacao_modulo=self.apresentacao_modulo, diretriz=self.diretriz, cliques=2)
		c = Client()
		response = c.get('/admin/sirius/modeloarquitetura/1/')
		self.assertEqual(response.status_code, 200)
		
	def test_url_criar(self):
		c = Client()
		response = c.get('/admin/sirius/modeloarquitetura/add/')
		self.assertEqual(response.status_code, 200)
	
	def test_url_cadastrar(self):
		self.apresentacao = Apresentacao.objects.create(diagrama_de_sequencia="C:\img\teste.jpg", descricao="descricao")
		self.visao_de_implementacao = VisaoImplementacao.objects.create(visao_atual="visao_atual", apresentacao_de_implementacao=self.apresentacao)			
		self.descricao_visao_atual= DescricaoVisaoAtual.objects.create(visao_atual="visao_atual", tipo_de_elementos="tipo_de_elementos", relacao_de_elementos="relacao_de_elementos", propriedades="propriedades", restricoes="restricoes")			
		self.visao_comportamental = VisaoBehavioral.objects.create(descricao_do_comportamento_de_dominio="descricao_do_comportamento_de_dominio", diagrama_do_comportamento="C:\img\teste.jpg", visao_atual=self.descricao_visao_atual, apresentacao_behavioral=self.apresentacao)
		self.modulo_catalog = ModuloCatalog.objects.create(nome="nome", digrama_modulo="C:\img\teste.jpg", descricao_de_modulo = "descricao_de_modulo")
		self.apresentacao_modulo = ApresentacaoModulo.objects.create(modulos="modulo", relacionamento_dos_modulos="relacionamento_dos_modulos")
		self.diretriz = Diretriz.objects.create(diretriz="diretriz")	
		c = Client()
		response = c.post('/admin/sirius/modeloarquitetura/add/', {'nome': 'nome', 'introducao': 'introducao', 'drives_arquitetonicos': 'drives_arquitetonicos', 'visao_comportamental': 1, 'visao_de_implementacao':1, 'visao_atual': 1, 'modulo_catalog': 1, 'apresentacao_modulo':1, 'diretriz':1})
		self.assertEqual(response.status_code, 200)
	
	def test_url_visualizacao(self):
		self.apresentacao = Apresentacao.objects.create(diagrama_de_sequencia="C:\img\teste.jpg", descricao="descricao")
		self.visao_de_implementacao = VisaoImplementacao.objects.create(visao_atual="visao_atual", apresentacao_de_implementacao=self.apresentacao)			
		self.descricao_visao_atual= DescricaoVisaoAtual.objects.create(visao_atual="visao_atual", tipo_de_elementos="tipo_de_elementos", relacao_de_elementos="relacao_de_elementos", propriedades="propriedades", restricoes="restricoes")			
		self.visao_comportamental = VisaoBehavioral.objects.create(descricao_do_comportamento_de_dominio="descricao_do_comportamento_de_dominio", diagrama_do_comportamento="C:\img\teste.jpg", visao_atual=self.descricao_visao_atual, apresentacao_behavioral=self.apresentacao)
		self.modulo_catalog = ModuloCatalog.objects.create(nome="nome", digrama_modulo="C:\img\teste.jpg", descricao_de_modulo = "descricao_de_modulo")
		self.apresentacao_modulo = ApresentacaoModulo.objects.create(modulos="modulo", relacionamento_dos_modulos="relacionamento_dos_modulos")
		self.diretriz = Diretriz.objects.create(diretriz="diretriz")	
		self.modelo_arquitetura = ModeloArquitetura.objects.create(nome="nome", introducao="introducao", drives_arquitetonicos="drives_arquitetonicos",  visao_comportamental = self.visao_comportamental, visao_de_implementacao=self.visao_de_implementacao, visao_atual=self.descricao_visao_atual, modulo_catalog=self.modulo_catalog, apresentacao_modulo=self.apresentacao_modulo, diretriz=self.diretriz, cliques=2)
		c = Client()
		response = c.get('/visualizar_documento/1/')
		self.assertEqual(response.status_code, 200)
	
	def test_url_geracao_pdf(self):
		self.apresentacao = Apresentacao.objects.create(diagrama_de_sequencia="C:\img\teste.jpg", descricao="descricao")
		self.visao_de_implementacao = VisaoImplementacao.objects.create(visao_atual="visao_atual", apresentacao_de_implementacao=self.apresentacao)			
		self.descricao_visao_atual= DescricaoVisaoAtual.objects.create(visao_atual="visao_atual", tipo_de_elementos="tipo_de_elementos", relacao_de_elementos="relacao_de_elementos", propriedades="propriedades", restricoes="restricoes")			
		self.visao_comportamental = VisaoBehavioral.objects.create(descricao_do_comportamento_de_dominio="descricao_do_comportamento_de_dominio", diagrama_do_comportamento="C:\img\teste.jpg", visao_atual=self.descricao_visao_atual, apresentacao_behavioral=self.apresentacao)
		self.modulo_catalog = ModuloCatalog.objects.create(nome="nome", digrama_modulo="C:\img\teste.jpg", descricao_de_modulo = "descricao_de_modulo")
		self.apresentacao_modulo = ApresentacaoModulo.objects.create(modulos="modulo", relacionamento_dos_modulos="relacionamento_dos_modulos")
		self.diretriz = Diretriz.objects.create(diretriz="diretriz")	
		self.modelo_arquitetura = ModeloArquitetura.objects.create(nome="nome", introducao="introducao", drives_arquitetonicos="drives_arquitetonicos",  visao_comportamental = self.visao_comportamental, visao_de_implementacao=self.visao_de_implementacao, visao_atual=self.descricao_visao_atual, modulo_catalog=self.modulo_catalog, apresentacao_modulo=self.apresentacao_modulo, diretriz=self.diretriz, cliques=2)	
		c = Client()
		response = c.get('/pdf/1/')
		self.assertEqual(response.status_code, 200)
		
		
class TesteUrlModeloArquiteturaAvaliacao(TestCase):
	def test_url_listagem(self):
		c = Client()
		response = c.get('/admin/sirius/modeloarquiteturaavaliacao/')
		self.assertEqual(response.status_code, 200)
	
	def test_url_editar(self):
		self.apresentacao = Apresentacao.objects.create(diagrama_de_sequencia="C:\img\teste.jpg", descricao="descricao")
		self.visao_de_implementacao = VisaoImplementacao.objects.create(visao_atual="visao_atual", apresentacao_de_implementacao=self.apresentacao)			
		self.descricao_visao_atual= DescricaoVisaoAtual.objects.create(visao_atual="visao_atual", tipo_de_elementos="tipo_de_elementos", relacao_de_elementos="relacao_de_elementos", propriedades="propriedades", restricoes="restricoes")			
		self.visao_comportamental = VisaoBehavioral.objects.create(descricao_do_comportamento_de_dominio="descricao_do_comportamento_de_dominio", diagrama_do_comportamento="C:\img\teste.jpg", visao_atual=self.descricao_visao_atual, apresentacao_behavioral=self.apresentacao)
		self.modulo_catalog = ModuloCatalog.objects.create(nome="nome", digrama_modulo="C:\img\teste.jpg", descricao_de_modulo = "descricao_de_modulo")
		self.apresentacao_modulo = ApresentacaoModulo.objects.create(modulos="modulo", relacionamento_dos_modulos="relacionamento_dos_modulos")
		self.diretriz = Diretriz.objects.create(diretriz="diretriz")	
		self.modelo_arquitetura = ModeloArquitetura.objects.create(nome="nome", introducao="introducao", drives_arquitetonicos="drives_arquitetonicos",  visao_comportamental = self.visao_comportamental, visao_de_implementacao=self.visao_de_implementacao, visao_atual=self.descricao_visao_atual, modulo_catalog=self.modulo_catalog, apresentacao_modulo=self.apresentacao_modulo, diretriz=self.diretriz, cliques=2)
		self.modelo_arquitetura_avaliacao = ModeloArquiteturaAvaliacao.objects.create(modeloArquitetura=self.modelo_arquitetura, nome="nome", descricao_da_qualidade="descricao_da_qualidade", descricao_de_nao_riscos="descricao_de_nao_riscos", descricao_de_riscos="descricao_de_riscos", diagrama_de_arquitetura="C:\img\teste.jpg", descricao_da_arquitetura="descricao_da_arquitetura", pricipais_abordagens_da_arquitetura="pricipais_abordagens_da_arquitetura", ponto_de_sensibilidade="ponto_de_sensibilidade", restricao_de_sensibilidade="restricao_de_sensibilidade", cliques=3)
		c = Client()
		response = c.get('/admin/sirius/modeloarquiteturaavaliacao/1/')
		self.assertEqual(response.status_code, 200)
		
	def test_url_criar(self):
		c = Client()
		response = c.get('/admin/sirius/modeloarquiteturaavaliacao/add/')
		self.assertEqual(response.status_code, 200)
		
	def test_url_cadastrar(self):
		self.apresentacao = Apresentacao.objects.create(diagrama_de_sequencia="C:\img\teste.jpg", descricao="descricao")
		self.visao_de_implementacao = VisaoImplementacao.objects.create(visao_atual="visao_atual", apresentacao_de_implementacao=self.apresentacao)			
		self.descricao_visao_atual= DescricaoVisaoAtual.objects.create(visao_atual="visao_atual", tipo_de_elementos="tipo_de_elementos", relacao_de_elementos="relacao_de_elementos", propriedades="propriedades", restricoes="restricoes")			
		self.visao_comportamental = VisaoBehavioral.objects.create(descricao_do_comportamento_de_dominio="descricao_do_comportamento_de_dominio", diagrama_do_comportamento="C:\img\teste.jpg", visao_atual=self.descricao_visao_atual, apresentacao_behavioral=self.apresentacao)
		self.modulo_catalog = ModuloCatalog.objects.create(nome="nome", digrama_modulo="C:\img\teste.jpg", descricao_de_modulo = "descricao_de_modulo")
		self.apresentacao_modulo = ApresentacaoModulo.objects.create(modulos="modulo", relacionamento_dos_modulos="relacionamento_dos_modulos")
		self.diretriz = Diretriz.objects.create(diretriz="diretriz")	
		self.modelo_arquitetura = ModeloArquitetura.objects.create(nome="nome", introducao="introducao", drives_arquitetonicos="drives_arquitetonicos",  visao_comportamental = self.visao_comportamental, visao_de_implementacao=self.visao_de_implementacao, visao_atual=self.descricao_visao_atual, modulo_catalog=self.modulo_catalog, apresentacao_modulo=self.apresentacao_modulo, diretriz=self.diretriz, cliques=2)
		c = Client()
		response = c.post('/admin/sirius/modeloarquiteturaavaliacao/add/', {'nome':'nome', 'introducao':'introducao', 'drives_arquitetonicos': 'drives_arquitetonicos', 'visao_comportamental':1, 'visao_de_implementacao':1, 'visao_atual':1, 'modulo_catalog':1, 'apresentacao_modulo':1, 'diretriz':1})
		self.assertEqual(response.status_code, 200)
		
	def test_url_visualizacao_avaliacao(self):
		self.apresentacao = Apresentacao.objects.create(diagrama_de_sequencia="C:\img\teste.jpg", descricao="descricao")
		self.visao_de_implementacao = VisaoImplementacao.objects.create(visao_atual="visao_atual", apresentacao_de_implementacao=self.apresentacao)			
		self.descricao_visao_atual= DescricaoVisaoAtual.objects.create(visao_atual="visao_atual", tipo_de_elementos="tipo_de_elementos", relacao_de_elementos="relacao_de_elementos", propriedades="propriedades", restricoes="restricoes")			
		self.visao_comportamental = VisaoBehavioral.objects.create(descricao_do_comportamento_de_dominio="descricao_do_comportamento_de_dominio", diagrama_do_comportamento="C:\img\teste.jpg", visao_atual=self.descricao_visao_atual, apresentacao_behavioral=self.apresentacao)
		self.modulo_catalog = ModuloCatalog.objects.create(nome="nome", digrama_modulo="C:\img\teste.jpg", descricao_de_modulo = "descricao_de_modulo")
		self.apresentacao_modulo = ApresentacaoModulo.objects.create(modulos="modulo", relacionamento_dos_modulos="relacionamento_dos_modulos")
		self.diretriz = Diretriz.objects.create(diretriz="diretriz")	
		self.modelo_arquitetura = ModeloArquitetura.objects.create(nome="nome", introducao="introducao", drives_arquitetonicos="drives_arquitetonicos",  visao_comportamental = self.visao_comportamental, visao_de_implementacao=self.visao_de_implementacao, visao_atual=self.descricao_visao_atual, modulo_catalog=self.modulo_catalog, apresentacao_modulo=self.apresentacao_modulo, diretriz=self.diretriz, cliques=2)
		self.modelo_arquitetura_avaliacao = ModeloArquiteturaAvaliacao.objects.create(modeloArquitetura=self.modelo_arquitetura, nome="nome", descricao_da_qualidade="descricao_da_qualidade", descricao_de_nao_riscos="descricao_de_nao_riscos", descricao_de_riscos="descricao_de_riscos", diagrama_de_arquitetura="C:\img\teste.jpg", descricao_da_arquitetura="descricao_da_arquitetura", pricipais_abordagens_da_arquitetura="pricipais_abordagens_da_arquitetura", ponto_de_sensibilidade="ponto_de_sensibilidade", restricao_de_sensibilidade="restricao_de_sensibilidade", cliques=3)
		c = Client()
		response = c.get('/visualizar_documento2/1/')
		self.assertEqual(response.status_code, 200)
		
class TesteUrlModuloCatalog(TestCase):
	def test_url_listagem(self):
		c = Client()
		response = c.get('/admin/sirius/modulocatalog/')
		self.assertEqual(response.status_code, 200)
	
	def test_url_editar(self):
		self.modulo_catalog = ModuloCatalog.objects.create(nome="nome", digrama_modulo="C:\img\teste.jpg", descricao_de_modulo = "descricao_de_modulo")
		c = Client()
		response = c.get('/admin/sirius/modulocatalog/1/')
		self.assertEqual(response.status_code, 200)
		
	def test_url_criar(self):
		c = Client()
		response = c.get('/admin/sirius/modulocatalog/add/')
		self.assertEqual(response.status_code, 200)
		
	def test_url_cadastrar(self):
		c = Client()
		response = c.post('/admin/sirius/modulocatalog/add/', {'nome': 'nome', 'descricao_de_modulo': 'descricao_de_modulo'})
		self.assertEqual(response.status_code, 200)
		
class TesteUrlVisaoAtual(TestCase):
	def test_url_listagem(self):
		c = Client()
		response = c.get('/admin/sirius/descricaovisaoatual/')
		self.assertEqual(response.status_code, 200)
	
	def test_url_editar(self):
		self.descricao_visao_atual= DescricaoVisaoAtual.objects.create(visao_atual="visao_atual", tipo_de_elementos="tipo_de_elementos", relacao_de_elementos="relacao_de_elementos", propriedades="propriedades", restricoes="restricoes")			
		c = Client()
		response = c.get('/admin/sirius/descricaovisaoatual/1/')
		self.assertEqual(response.status_code, 200)
		
	def test_url_criar(self):
		c = Client()
		response = c.get('/admin/sirius/descricaovisaoatual/add/')
		self.assertEqual(response.status_code, 200)
		
	def test_url_cadastrar(self):
		c = Client()
		response = c.post('/admin/sirius/descricaovisaoatual/add/', {'visao_atual': 'visao_atual', 'tipo_de_elementos': 'tipo_de_elementos', 'relacao_de_elementos': 'relacao_de_elementos', 'propriedades': 'propriedades', 'restricoes': 'restricoes'})
		self.assertEqual(response.status_code, 200)
		
class TestUrlVisaoBehavioral(TestCase):
	def test_url_listagem(self):
		c = Client()
		response = c.get('/admin/sirius/visaobehavioral/')
		self.assertEqual(response.status_code, 200)
	
	def test_url_editar(self):
		self.apresentacao = Apresentacao.objects.create(diagrama_de_sequencia="C:\img\teste.jpg", descricao="descricao")
		self.descricao_visao_atual= DescricaoVisaoAtual.objects.create(visao_atual="visao_atual", tipo_de_elementos="tipo_de_elementos", relacao_de_elementos="relacao_de_elementos", propriedades="propriedades", restricoes="restricoes")			
		self.visao_comportamental = VisaoBehavioral.objects.create(descricao_do_comportamento_de_dominio="descricao_do_comportamento_de_dominio", diagrama_do_comportamento="C:\img\teste.jpg", visao_atual=self.descricao_visao_atual, apresentacao_behavioral=self.apresentacao)		
		c = Client()
		response = c.get('/admin/sirius/visaobehavioral/1/')
		self.assertEqual(response.status_code, 200)
		
	def test_url_criar(self):
		c = Client()
		response = c.get('/admin/sirius/visaobehavioral/add/')
		self.assertEqual(response.status_code, 200)
		
	def test_url_cadastrar(self):
		self.apresentacao = Apresentacao.objects.create(diagrama_de_sequencia="C:\img\teste.jpg", descricao="descricao")
		self.descricao_visao_atual= DescricaoVisaoAtual.objects.create(visao_atual="visao_atual", tipo_de_elementos="tipo_de_elementos", relacao_de_elementos="relacao_de_elementos", propriedades="propriedades", restricoes="restricoes")
		c = Client()
		response = c.post('/admin/sirius/visaobehavioral/add/', {'descricao_do_comportamento_de_dominio':'descricao_do_comportamento_de_dominio', 'visao_atual':1, 'apresentacao_behavioral':1})
		self.assertEqual(response.status_code, 200)
		
class TesteUrlVisaoImplementacao(TestCase):
	def test_url_listagem(self):
		c = Client()
		response = c.get('/admin/sirius/visaoimplementacao/')
		self.assertEqual(response.status_code, 200)

	
	def test_url_editar(self):
		self.apresentacao = Apresentacao.objects.create(diagrama_de_sequencia="C:\img\teste.jpg", descricao="descricao")
		self.visao_de_implementacao = VisaoImplementacao.objects.create(visao_atual="visao_atual", apresentacao_de_implementacao=self.apresentacao)	
		c = Client()
		response = c.get('/admin/sirius/visaoimplementacao/1/')
		self.assertEqual(response.status_code, 200)
		
	def test_url_criar(self):
		c = Client()
		response = c.get('/admin/sirius/visaoimplementacao/add/')
		self.assertEqual(response.status_code, 200)
		
	def test_url_cadastrar(self):
		self.apresentacao = Apresentacao.objects.create(diagrama_de_sequencia="C:\img\teste.jpg", descricao="descricao")
		c = Client()
		response = c.post('/admin/sirius/visaoimplementacao/add/', {'visao_atual':'visao_atual', 'apresentacao_de_implementacao':1})
		self.assertEqual(response.status_code, 200)