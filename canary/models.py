# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db.models import permalink
from django.template.defaulttags import verbatim


class Arquitetura(models.Model):
    nome = models.CharField(max_length=200, verbose_name="nome")
    descricao = models.TextField(verbose_name="descrição")
    introducao = models.TextField(verbose_name="introdução")
    objetivo = models.TextField(verbose_name="objetivo")
    autores = models.ManyToManyField(User)
    tecnologias = models.ManyToManyField('Tecnologia')
    introducao_qualidade = models.TextField(verbose_name="introdução aos cenários de qualidade")
    referencias_qualidade = models.TextField(verbose_name="referências aos cenários de qualidade")

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
    arquitetura = models.OneToOneField(Arquitetura)
    funcionamento = models.CharField(max_length=2, choices=classificacao)
    confiabilidade = models.CharField(max_length=2, choices=classificacao)
    usabilidade = models.CharField(max_length=2, choices=classificacao)
    eficiencia = models.CharField(max_length=2, choices=classificacao, verbose_name="eficiência")
    manutenibilidade = models.CharField(max_length=2, choices=classificacao)
    portabilidade = models.CharField(max_length=2, choices=classificacao)

    class Meta:
        verbose_name="Atributo de qualidade"
        verbose_name_plural="Atributos de qualidade"

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
optVisaoComportamental = (
                    (1, 'Baixo'),
                    (2, 'Alto')
)

class PontoDeVista(models.Model):
    arquitetura = models.ForeignKey(Arquitetura)
    resumo = models.TextField()
    stakeholders = models.TextField()
    preocupacao = models.TextField(verbose_name="preocupação")
    #elemento = models.ManyToManyField('Elemento')
    detalheVisaoEstrutural = models.IntegerField(choices=optVisaoEstrutural, verbose_name="Detalhamento da visão estrutural")
    detalheVisaoComportamental = models.IntegerField(choices=optVisaoComportamental, verbose_name="Detalhamento da visão comportamental")
    visaoEstrutural = models.ManyToManyField('VisaoEstrutural', verbose_name="visão estrutural")
    visaoComportamental = models.ManyToManyField('VisaoComportamental', verbose_name="visão comportamental")

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

    class Meta:
        verbose_name="visão comportamental"
        verbose_name_plural="visões comportamentais"








