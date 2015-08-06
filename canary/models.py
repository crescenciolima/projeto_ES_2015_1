# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db.models import permalink
from django.template.defaulttags import verbatim

escolha = (
			('funcionamento', 'Funcionamento'),
			('confiabilidade', 'Confiabilidade'),
            ('usabilidade', 'Usabilidade'),
            ('eficiencia', 'Eficiência'),
            ('manutenibilidade', 'Manutenibilidade'),
            ('portabilidade', 'Portabilidade')
)

fator = (
					('1', 'Fator 1: 4 - 3'),
                    ('2', 'Fator 2: 4 - 2'),
                    ('3', 'Fator 3: 4 - 1'),
                    ('4', 'Fator 4: 4 - 0')
)

qtdrelacoes = (
    ('1', '1 relação'),
    ('2', '2 relações'),
    ('3', '3 relações')

)

class Arquitetura(models.Model):
    nome = models.CharField(max_length=200, verbose_name="nome")
    descricao = models.TextField(verbose_name="descrição")
    introducao = models.TextField(verbose_name="introdução")
    objetivo = models.TextField(verbose_name="objetivo")
    autores = models.ManyToManyField(User)
    tecnologias = models.ManyToManyField('Tecnologia')
    introducao_qualidade = models.TextField(verbose_name="introdução aos cenários de qualidade")
    referencias_qualidade = models.TextField(verbose_name="referências aos cenários de qualidade")
    qtdrelacoes = models.CharField(max_length=2, choices=qtdrelacoes, verbose_name="quantidade de relações entre atributos")

    def __unicode__(self):
        return '%s' % self.nome

    def preview(self):
        return '<a href="/canary/arquitetura/%s">Pré visualização</a>' % (self.pk)

    preview.allow_tags = True

# class Autor(models.Model):
#     nome = models.CharField(max_length=90)
#
#     def __unicode__(self):
#         return '%s' % self.nome

class Referencia(models.Model):
    arquitetura = models.ForeignKey(Arquitetura)
    titulo = models.CharField(max_length=90, verbose_name="título")
    autores = models.CharField(max_length=150)
    descricao = models.TextField(blank=True, verbose_name="descrição")

    def __unicode__(self):
        return '%s' % self.titulo

    class Meta:
        verbose_name="Referência"

class Tecnologia(models.Model):
    api = models.ManyToManyField('API', verbose_name="API")
    descricao = models.CharField(max_length=100, verbose_name="descrição")
    razaoUso = models.CharField(max_length=100, verbose_name="razão de uso")

    def __unicode__(self):
        return '%s' % self.descricao

class API(models.Model):
    nome = models.CharField(max_length=50)
    versao = models.CharField(max_length=10, verbose_name="versão")
    especificacao = models.TextField(verbose_name="especificação")

    def __unicode__(self):
        return '%s' % self.nome

    class Meta:
        verbose_name="API"
        verbose_name_plural="APIs"

classificacao = (
                    ('0', '0'),
                    ('1', '1'),
                    ('2', '2'),
                    ('3', '3'),
                    ('4', '4')
)

class AtributoDeQualidade(models.Model):
    arquitetura = models.OneToOneField(Arquitetura, related_name='attrQualidade')
    funcionamento = models.CharField(max_length=2, choices=classificacao)
    confiabilidade = models.CharField(max_length=2, choices=classificacao)
    usabilidade = models.CharField(max_length=2, choices=classificacao)
    eficiencia = models.CharField(max_length=2, choices=classificacao, verbose_name="eficiência")
    manutenibilidade = models.CharField(max_length=2, choices=classificacao)
    portabilidade = models.CharField(max_length=2, choices=classificacao)

    class Meta:
        verbose_name="Atributo de qualidade"
        verbose_name_plural="Atributos de qualidade"

    def __unicode__(self):
        return '%s' % self.arquitetura

class Feature(models.Model):
    class Meta:
        abstract = True

    arquitetura = models.ForeignKey(Arquitetura)
    nome = models.CharField(max_length=50)
    descricao = models.TextField(verbose_name="descrição")

    def __unicode__(self):
        return '%s, %s' % self.nome, self.descricao

class NaoFuncional(Feature):
    fonte = models.TextField()
    estimulo = models.TextField(verbose_name="estímulo")
    ambiente = models.TextField()
    artefato = models.TextField()
    resposta = models.TextField()
    medicao = models.TextField(verbose_name="medição")

    def __unicode__(self):
        return '%s' % self.nome

    class Meta:
        verbose_name="Requisito não funcional"
        verbose_name_plural="Requisitos não funcionais"

class Funcional(Feature):

    def __unicode__(self):
        return '%s' % self.nome, self.descricao

    class Meta:
        verbose_name="Requisito funcional"
        verbose_name_plural="Requisitos funcionais"

optVisaoEstrutural = (
                    (1, 'Baixo'),
                    (2, 'Medio'),
                    (3, 'Alto')
)
VisaoComportamental = (
                    (1, 'Baixo'),
                    (2, 'Alto')
)

class PontoDeVista(models.Model):
    arquitetura = models.ForeignKey(Arquitetura)
    resumo = models.TextField()
    stakeholders = models.TextField()
    preocupacao = models.TextField(verbose_name="preocupação")
    detalheVisaoEstrutural = models.IntegerField(choices=optVisaoEstrutural, verbose_name="Detalhamento da visão estrutural")
    detalheVisaoComportamental = models.IntegerField(choices=VisaoComportamental, verbose_name="Detalhamento da visão comportamental")

    def __unicode__(self):
        return '%s' % self.resumo

    class Meta:
        verbose_name="Ponto de vista"
        verbose_name_plural="Pontos de vista"

class Elemento(models.Model):
    nome = models.CharField(max_length=40)
    pontoDeVista = models.ForeignKey(PontoDeVista, blank=True, null=True, verbose_name="ponto de vista")
    elementosRelacionados = models.ManyToManyField('self', blank=True, null=True, verbose_name="elementos relacionados")
    propriedades = models.TextField()
    restricoes = models.TextField(verbose_name="restrições")

    def __unicode__(self):
        return '%s' % self.nome

class Componente(models.Model):
    descricao = models.TextField(verbose_name="descrição")
    featuresRelacionadas = models.TextField(verbose_name="features relacionadas")
    padraoDesing = models.TextField(verbose_name="padrão de design")

    def __unicode__(self):
        return '%s' % self.descricao

class Modulo(models.Model):
    descricao = models.TextField(verbose_name="descrição")
    featuresRelacionadas = models.TextField(verbose_name="features relacionadas")
    componentes = models.ManyToManyField('componente')

    def __unicode__(self):
        return '%s' % self.descricao

    class Meta:
        verbose_name="módulo"
        verbose_name_plural="módulos"

class VisaoEstrutural(models.Model):
    apresentacao = models.TextField(verbose_name="apresentação")
    estilosArquitetura = models.TextField(verbose_name="estilos de arquitetura")
    modulos = models.ManyToManyField('Modulo', verbose_name="módulos")

    def __unicode__(self):
        return '%s' % self.apresentacao

    class Meta:
        verbose_name="visão estrutural"
        verbose_name_plural="visões estruturais"

class VisaoComportamental(models.Model):
    diagrama = models.ImageField(upload_to="fotos")
    feature = models.CharField(max_length=150)
    variavelID = models.CharField(max_length=150, verbose_name="ID da variável")
    featureRelacionadas = models.TextField(verbose_name="features relacionadas")

    def __unicode__(self):
        return '%s' % self.feature

    class Meta:
        verbose_name="visão comportamental"
        verbose_name_plural="visões comportamentais"
        
class Relacionamento2(models.Model):
    projeto = models.OneToOneField(Arquitetura, blank=True)
    relacao1 = models.CharField(max_length=250, choices = escolha, verbose_name="atributo 1")
    relacao2 = models.CharField(max_length=250, choices = escolha, verbose_name="atributo 2")
    fator = models.CharField(max_length=2, choices=fator, verbose_name="fator de impacto")

    class Meta:
        verbose_name="Atributos de Qualidade - 1 Relacionamento"
        verbose_name_plural="Atributos de Qualidade - 1 Relacionamento"

class Relacionamento4(models.Model):
    projeto = models.OneToOneField(Arquitetura, blank=True)
    relacao1 = models.CharField(max_length=250, choices = escolha, verbose_name="atributo 1")
    relacao2 = models.CharField(max_length=250, choices = escolha, verbose_name="atributo 2")
    fator1 = models.CharField(max_length=2, choices=fator, verbose_name="fator de impacto")
    relacao3 = models.CharField(max_length=250, choices = escolha, verbose_name="atributo 3")
    relacao4 = models.CharField(max_length=250, choices = escolha, verbose_name="atributo 4")
    fator2 = models.CharField(max_length=2, choices=fator, verbose_name="fator de impacto")

    class Meta:
        verbose_name="Atributos de Qualidade - 2 Relacionamentos"
        verbose_name_plural="Atributos de Qualidade - 2 Relacionamentos"

class Relacionamento6(models.Model):
    projeto = models.OneToOneField(Arquitetura, blank=True)
    relacao1 = models.CharField(max_length=250, choices = escolha, verbose_name="atributo 1")
    relacao2 = models.CharField(max_length=250, choices = escolha, verbose_name="atributo 2")
    fator1 = models.CharField(max_length=2, choices=fator, verbose_name="fator de impacto")
    relacao3 = models.CharField(max_length=250, choices = escolha, verbose_name="atributo 3")
    relacao4 = models.CharField(max_length=250, choices = escolha, verbose_name="atributo 4")
    fator2 = models.CharField(max_length=2, choices=fator, verbose_name="fator de impacto")
    relacao5 = models.CharField(max_length=250, choices = escolha, verbose_name="atributo 5")
    relacao6 = models.CharField(max_length=250, choices = escolha, verbose_name="atributo 6")
    fator3 = models.CharField(max_length=2, choices=fator, verbose_name="fator de impacto")

    class Meta:
        verbose_name="Atributos de Qualidade - 3 Relacionamentos"
        verbose_name_plural="Atributos de Qualidade - 3 Relacionamentos"


    #################APÊNDICE B SIRIUS################
class ClassificacaoMetricaAvaliacao(models.Model):
    id = models.AutoField(primary_key=True)
    metodoAvaliacao = models.CharField(max_length=300, blank=True)
    objetivo = models.TextField(blank=True)
    tiposAtributo = models.CharField(max_length=300, blank=True)
    faseAvaliacao = models.CharField(max_length=300, blank=True)
    tecnicaAvaliacao = models.TextField(blank=True)
    descricaoProcesso = models.TextField(blank=True)
    validacaoMetodo = models.TextField(blank=True)
    relacaoMetodo = models.CharField(max_length=300, blank=True)


    def __unicode__(self):
        return '%s' % self.metodoAvaliacao

class ModeloArquiteturaAvaliacao(models.Model):
    id = models.AutoField(primary_key=True)
    arquitetura = models.ForeignKey(Arquitetura, blank=True, null=False)
    nome = models.CharField(max_length=150, blank=False)
    descricao_da_qualidade = models.TextField(blank=False)
    descricao_de_nao_riscos = models.TextField(blank=False)
    descricao_de_riscos = models.TextField(blank=False)
    diagrama_de_arquitetura = models.ImageField(upload_to="fotos")
    descricao_da_arquitetura = models.TextField(blank=False)
    pricipais_abordagens_da_arquitetura = models.TextField(blank=False)
    ponto_de_sensibilidade = models.TextField(blank=False)
    restricao_de_sensibilidade = models.TextField(blank=True)
    cliques = models.IntegerField(editable=False, default=0)
    classificacao_metrica_avaliacao = models.ForeignKey(ClassificacaoMetricaAvaliacao,blank=True, null=False)
    # informacao_arquitetural = models.ForeignKey(InformacaoArquitetural,blank=True, null=False)

    class Meta:
        verbose_name="Avaliação"
        verbose_name_plural="Avaliações"

    def pesquisaModeloArquiteturaAvaliacao(pesquisa):
        modeloArquiteturaAvaliacao = models.ModeloArquiteturaAvaliacao.objects.all(headline_contains=pesquisa);
        return modeloArquiteturaAvaliacao

    def __unicode__(self):
        return '%s' % self.nome

