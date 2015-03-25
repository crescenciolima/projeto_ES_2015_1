from django.db import models

# Create your models here.

class Projeto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    autores = models.ManyToManyField(Autores)
    introducao = models.ManyToManyField(Introducao)
    referencia = models.ManyToManyField(Referencia)
    tecnologia = models.ManyToManyField(Tecnologia)
    atributosQualidade = models.ManyToManyField(AtributodeQualidade)
    condutoresArquiteturais = models.ManyToManyField(Feature)

class Autores(models.Model):
    projeto = models.OneToOneField(Projeto)
    nome = models.CharField(max_length=90)


class Introducao(models.Model):
    projeto = models.OneToOneField(Projeto, primary_key=True)
    introducao = models.TextField()
    objetivo = models.TextField()

class Referencia(models.Model):
    titulo = models.CharField(max_length=90)
    autores = models.CharField(max_length=150)
    descricao = models.TextField()
    projeto = models.ManyToManyField(Projeto)


class Tecnologia(models.Model):
    api = models.ManyToManyField(API)
    razaoUso = models.CharField(max_length=100)
    projeto = models.ManyToManyField(Projeto)


class API(models.Model):
    tecnologia = models.OneToOneField(Projeto, primary_key=True)
    nome = models.CharField(max_length=50)
    versao = models.CharField(max_length=10)
    especificacao = models.TextField()

class AtributodeQualidade(models.Model):
    projeto = models.ForeignKey(Projeto)
    nome = models.CharField(max_length=80)
    prioridade = models.IntegerField

class Feature(models.Model):
    projeto = models.OneToOneField(Projeto, primary_key=True)
    nome = models.CharField(max_length=50)
    descricao = models.TextField()

class NaoFuncional(models.Model.Feature):
    fonte = models.CharField(300)
    estimulo = models.CharField(300)
    ambiente = models.CharField(300)
    artefato = models.CharField(300)
    resposta = models.CharField(300)
    medicao = models.CharField(300)

class Funcional(models.Model.Feature):
    nome1 = models.CharField()
