#coding:utf-8
from django.db import models
from django.db.models import permalink

class TipoPadrao(models.Model):
    nome = models.CharField(max_length=255)
    cliques = models.IntegerField(editable=False, default=0)

    class Meta:
        verbose_name = 'Tipo de Padrão'
        verbose_name_plural = 'Tipos de Padrões'

    def __unicode__(self):
        return '%s' % self.nome

    @permalink
    def get_absolute_url(self):
        return ('view_tipo_padrao', None, { 'id': self.id })


# --------------------------------------------------------------------------------------

class TipoDecisao(models.Model):
    nome = models.CharField(max_length=255)
    cliques = models.IntegerField(editable=False, default=0)

    class Meta:
        verbose_name = 'Tipo de Decisão'
        verbose_name_plural = 'Tipos de Decisões'

    def __unicode__(self):
        return '%s' % self.nome

    @permalink
    def get_absolute_url(self):
        return ('view_tipo_decisao', None, { 'id': self.id })

# --------------------------------------------------------------------------------------

class Padrao(models.Model):

    class Meta:
        verbose_name = 'Padrão'
        verbose_name_plural = 'Padrões'

    nome = models.CharField(max_length=255)
    aliase = models.TextField()
    contexto = models.TextField()
    problema = models.TextField()
    vantagens = models.TextField()
    desvantagens = models.TextField()
    aplicabilidade = models.TextField()
    referencias = models.TextField(verbose_name='referências')
    padroesRelacionados = models.ManyToManyField("self", blank=True, related_name='padroes', verbose_name='padrões relacionados')
    tipoDePadrao = models.ForeignKey(TipoPadrao, related_name='tipoDePadrao_set', verbose_name='tipo de padrão')
    imagem = models.ImageField(upload_to="fotos", blank=True)
    cliques = models.IntegerField(editable=False, default=0)
    categorias = models.ManyToManyField("TagPadrao", blank=False, related_name='tags')

    def __unicode__(self):
        return '%s' % self.nome

        #@permalink
        #def get_absolute_url(self):
        #    return ('view_nome', None, { 'nome': self.id })

    @permalink
    def get_absolute_url(self):
        return ('view_padrao', None, { 'id': self.id })


# --------------------------------------------------------------------------------------

TIPO_ESTADO = (
            ('Sugerido', 'Sugerido'),
            ('Revisado', 'Revisado'),
            ('Aprovado', 'Aprovado'),
            ('Rejeitado', 'Rejeitado')
)

class Decisao(models.Model):

    class Meta:
        verbose_name = 'Decisão'
        verbose_name_plural = 'Decisões'

    nome = models.CharField(max_length=255)
    descricao = models.TextField(verbose_name='descrição')
    objetivo = models.TextField()
    motivacao = models.TextField(verbose_name='motivação')
    tipoDeDecisao = models.ForeignKey(TipoDecisao, related_name='tipoDeDecisao_set', verbose_name='tipo de decisão')
    escopo = models.TextField()
    hipoteses = models.TextField(verbose_name='hipóteses')
    restricoes = models.TextField(verbose_name='restrições')
    alternativas = models.TextField()
    implicacoes = models.TextField(verbose_name='implicações')
    decisaoRelacionada = models.ManyToManyField("self", blank=True, related_name='decisoes', verbose_name='decisões relacionadas')
    necessidades = models.TextField()
    notas = models.TextField()
    estado = models.CharField(max_length=20, choices=TIPO_ESTADO)
    categorias = models.ManyToManyField("TagDecisao", blank=False, related_name='tag_set')
    padraoUtilizado = models.ManyToManyField("Padrao", blank=True, related_name='padroes', verbose_name='padrão utilizado')
    cliques = models.IntegerField(editable=False, default=0)

    def pesquisaDecisao(pesquisa):
        decisoes = models.Decisao.objects.all(headline_contains=pesquisa);
        return decisoes

    def __unicode__(self):
        return '%s' % self.nome

    @permalink
    def get_absolute_url(self):
        return ('view_decisao', None, { 'id': self.id })

class TagDecisao(models.Model):

    class Meta:
        verbose_name = 'Tag de decisão'
        verbose_name_plural = 'Tags de decisão'

    nome = models.CharField(max_length=255)

    def __unicode__(self):
        return '%s' % self.nome

class TagPadrao(models.Model):

    class Meta:
        verbose_name = 'Tag de padrão'
        verbose_name_plural = 'Tags de padrão'

    nome = models.CharField(max_length=255)

    def __unicode__(self):
        return '%s' % self.nome