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

    def __unicode__(self):
        return '%s' % self.nome

class Introducao(models.Model):
    projeto = models.OneToOneField(Projeto, primary_key=True)
    introducao = models.TextField()
    objetivo = models.TextField()

    def __unicode__(self):
        return '%s %s' % self.introducao, self.objetivo

class Referencia(models.Model):
    titulo = models.CharField(max_length=90)
    autores = models.CharField(max_length=150)
    descricao = models.TextField()
    projeto = models.ManyToManyField(Projeto)

    def __unicode__(self):
        return '%s, %s, %s' % self.titulo, self.autores, self.descricao

class Tecnologia(models.Model):
    api = models.ManyToManyField(API)
    razaoUso = models.CharField(max_length=100)
    projeto = models.ManyToManyField(Projeto)

    def __unicode__(self):
        return '%s , %s, %s' % self.api, self.razaoUso, self.projeto

class API(models.Model):
    tecnologia = models.OneToOneField(Projeto, primary_key=True)
    nome = models.CharField(max_length=50)
    versao = models.CharField(max_length=10)
    especificacao = models.TextField()

    def __unicode__(self):
        return '%s, %s, %s' % self.nome, self.versao, self.especificacao

classificacao = (
                    ('0', '0'),
                    ('1', '1'),
                    ('2', '2'),
                    ('3', '3'),
                    ('4', '4')
)

class AtributodeQualidade(models.Model):
    projeto = models.ForeignKey(Projeto)
    funcionamento = models.CharField(max_length=2, choices=classificacao)
    confiabilidade = models.CharField(max_length=2, choices=classificacao)
    usabilidade = models.CharField(max_length=2, choices=classificacao)
    eficiencia = models.CharField(max_length=2, choices=classificacao)
    manutenibilidade = models.CharField(max_length=2, choices=classificacao)
    portabilidade = models.CharField(max_length=2, choices=classificacao)

class Feature(models.Model):
    projeto = models.OneToOneField(Projeto, primary_key=True)
    nome = models.CharField(max_length=50)
    descricao = models.TextField()

     def __unicode__(self):
        return '%s, %s' % self.nome, self.descricao

class NaoFuncional(models.Model.Feature):
    fonte = models.CharField(300)
    estimulo = models.CharField(300)
    ambiente = models.CharField(300)
    artefato = models.CharField(300)
    resposta = models.CharField(300)
    medicao = models.CharField(300)

     def __unicode__(self):
        return '%s, %s, %s, %s, %s, %s' % self.fonte, self.estimulo, self.ambiente, self.artefato, self.resposta, self.medicao


class Funcional(models.Model.Feature):
    nome = models.CharField()
    descricao = models.CharField()

    def __unicode__(self):
        return '%s, %s' % self.nome, self.descricao