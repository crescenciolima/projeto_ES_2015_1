from django.db import models

class TipoPadrao(models.Model):
    nome = models.CharField(max_length=255)

    def __unicode__(self):
        return '%s' % self.nome

       # @permalink
       # def get_absolute_url(self):
       #     return ('view_nome', None, { 'nome': self.id })


# --------------------------------------------------------------------------------------

class TipoDecisao(models.Model):
    nome = models.CharField(max_length=255)

    def __unicode__(self):
        return '%s' % self.nome

        #@permalink
        #def get_absolute_url(self):
        #    return ('view_contato', None, { 'nome': self.id })

# --------------------------------------------------------------------------------------

class Padrao(models.Model):
    nome = models.CharField(max_length=255)
    aliase = models.TextField()
    contexto = models.TextField()
    problema = models.TextField()
    vantagens = models.TextField()
    desvantagens = models.TextField()
    aplicabilidade = models.TextField()
    referencias = models.TextField()
    padroesRelacionados = models.ManyToManyField("self", blank=True, related_name='padroes')
    tipoDePadrao = models.ForeignKey(TipoPadrao, related_name='tipoDePadrao_set')
    imagem = models.ImageField(upload_to="fotos")


    def __unicode__(self):
        return '%s' % self.nome

        #@permalink
        #def get_absolute_url(self):
        #    return ('view_nome', None, { 'nome': self.id })


# --------------------------------------------------------------------------------------

TIPO_ESTADO = (
            ('Sugerido', 'Sugerido'),
            ('Revisado', 'Revisado'),
            ('Aprovado', 'Aprovado'),
            ('Rejeitado', 'Rejeitado')
)

class Decisao(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    objetivo = models.TextField()
    motivacao = models.TextField()
    tipoDeDecisao = models.ForeignKey(TipoDecisao, related_name='tipoDeDecisao_set')
    escopo = models.TextField()
    hipoteses = models.TextField()
    restricoes = models.TextField()
    alternativas = models.TextField()
    implicacoes = models.TextField()
    decisaoRelacionada = models.ManyToManyField("self", blank=True, related_name='decisoesRelacionadas_set')
    necessidades = models.TextField()
    notas = models.TextField()
    #historico = manualmente?
    estado = models.CharField(max_length=20, choices=TIPO_ESTADO)
    categoria = models.TextField()
    padraoUtilizado = models.ManyToManyField("Padrao", blank=True, related_name='padraoUtilizado_set')

    def __unicode__(self):
        return '%s' % self.id

       # @permalink
       # def get_absolute_url(self):
       #     return ('view_nome', None, { 'nome': self.nome })