from django.db import models

BOOL_CHOICES = ((True, 'Sim'), (False, 'Nao'))


class ModeloArquitetura(models.Model):
    nome = models.CharField(max_length=150, blank=False)
    introducao = models.TextField(blank=False)
    referencia_escolha = models.BooleanField(choices=BOOL_CHOICES)

    def __unicode__(self):
        return '%s' % self.nome

    class Meta:
		verbose_name = 'Modelo de Arquitetura'
		verbose_name_plural = 'Modelos de Arquitetura'
		ordering = ['introducao']


class ModeloArquiteturaAvaliacao(models.Model):
    id = models.AutoField(primary_key=True)
    modeloArquitetura = models.ForeignKey(ModeloArquitetura, blank=True, null=False)
    desc_drivesarquitetonicos = models.TextField(blank=False)
    desc_qualidade = models.TextField(blank=False)
    desc_ponto_sensibilidade = models.TextField(blank=False)
    desc_nao_riscos = models.TextField(blank=False)
    desc_riscos = models.TextField(blank=False)
    desc_arquitetura_texto = models.TextField(blank=False)
    desc_arquitetura = models.ImageField(upload_to="destino")
    desc_pricipais_abordagens_arquitetura = models.TextField(blank=False)
    desc_restricao_sensibilidade = models.TextField(blank=True)

    def __unicode__(self):
        return '%s' % self.modeloArquitetura

    class Meta:
		verbose_name = 'Modelo de Arquitetura Avaliacao'
		verbose_name_plural = 'Modelos de Arquitetura Avaliacao'
		ordering = ['modeloArquitetura']


class Tecnologias(models.Model):
    id = models.AutoField(primary_key=True)
    tecnologia = models.CharField(max_length=200)
    justificativa = models.TextField(blank=False)
    modeloArquitetura = models.ForeignKey(ModeloArquitetura, blank=True, null=False)

    def __unicode__(self):
        return '%s' % self.tecnologia

class Diretriz(models.Model):
    id = models.AutoField(primary_key=True)
    # variaveis da tabela diretriz
    diretriz = models.CharField(max_length=200)
    atributo_qualidade_afetado = models.CharField(max_length=200)
    estimulo = models.CharField(max_length=200)
    resposta = models.CharField(max_length=200)
    estrategia = models.CharField(max_length=200)

    def __unicode__(self):
        return '%s' % self.diretriz

    class Meta:
	    verbose_name = 'Diretriz'
	    verbose_name_plural = 'Diretrizes'
	    ordering = ['diretriz']

class TradeOff(models.Model):
    id = models.AutoField(primary_key=True)
    desc_ponto_trade_off = models.TextField(blank=False)
    # um doc tem muitos um ou mais tradeoff#
    modeloArquitetura = models.ForeignKey(ModeloArquiteturaAvaliacao, blank=True, null=False)
    diretriz = models.ForeignKey(Diretriz)

    def __unicode__(self):
        return '%s' % self.desc_ponto_trade_off

class Referencia(models.Model):
    id = models.AutoField(primary_key=True)
    referencia = models.CharField(max_length=200)
    modeloArquitetura = models.ForeignKey(ModeloArquitetura, blank=True, null=False)

    def __unicode__(self):
        return '%s' % self.referencia

class Estilo(models.Model):
    id = models.AutoField(primary_key=True)
    estilo = models.CharField(max_length=200, blank=False)
    abordagem = models.CharField(max_length=200, blank=False)
    justificativa = models.CharField(max_length=400, blank=False)
    modeloArquiteturaAvaliacao = models.ForeignKey(ModeloArquiteturaAvaliacao, blank=True, null=False)

    def __unicode__(self):
        return '%s' % self.estilo
