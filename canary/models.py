from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Projeto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    introducao = models.TextField()
    objetivo = models.TextField()
    autores = models.ManyToManyField(User)
    tecnologia = models.ManyToManyField('Tecnologia')
    atributosQualidade = models.OneToOneField('AtributoDeQualidade')

    def __unicode__(self):
        return '%s' % self.nome

# class Autor(models.Model):
#     nome = models.CharField(max_length=90)
#
#     def __unicode__(self):
#         return '%s' % self.nome

class Referencia(models.Model):
    projeto = models.OneToOneField('Projeto')
    titulo = models.CharField(max_length=90)
    autores = models.CharField(max_length=150)
    descricao = models.TextField(blank=True)

    def __unicode__(self):
        return '%s' % self.titulo
#
class Tecnologia(models.Model):
    api = models.ManyToManyField('API')
    descricao = models.CharField(max_length=100)
    razaoUso = models.CharField(max_length=100)

    def __unicode__(self):
        return '%s' % self.descricao

class API(models.Model):
    nome = models.CharField(max_length=50)
    versao = models.CharField(max_length=10)
    especificacao = models.TextField()

    def __unicode__(self):
        return '%s' % self.nome

classificacao = (
                    ('0', '0'),
                    ('1', '1'),
                    ('2', '2'),
                    ('3', '3'),
                    ('4', '4')
)

class AtributoDeQualidade(models.Model):
    funcionamento = models.CharField(max_length=2, choices=classificacao)
    confiabilidade = models.CharField(max_length=2, choices=classificacao)
    usabilidade = models.CharField(max_length=2, choices=classificacao)
    eficiencia = models.CharField(max_length=2, choices=classificacao)
    manutenibilidade = models.CharField(max_length=2, choices=classificacao)
    portabilidade = models.CharField(max_length=2, choices=classificacao)

class Feature(models.Model):
    class Meta:
        abstract = True

    projeto = models.OneToOneField(Projeto)
    nome = models.CharField(max_length=50)
    descricao = models.TextField()

    def __unicode__(self):
        return '%s, %s' % self.nome, self.descricao

class NaoFuncional(Feature):
    fonte = models.TextField()
    estimulo = models.TextField()
    ambiente = models.TextField()
    artefato = models.TextField()
    resposta = models.TextField()
    medicao = models.TextField()

    def __unicode__(self):
        return '%s' % self.nome


class Funcional(Feature):

    def __unicode__(self):
        return '%s' % self.nome, self.descricao