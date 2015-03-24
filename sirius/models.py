from django.db import models

class ModeloArquitetura(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150, blank=False)
    introducao = models.TextField(blank=False)
    referencia_escolha = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s' % self.nome

class ModeloArquiteturaAvaliacao(models.Model):

    id = models.AutoField(primary_key=True)
    desc_qualidade = models.TextField(blank=False)
    desc_ponto_sensibilidade = models.TextField(blank=False)
    desc_nao_riscos = models.TextField(blank=False)
    desc_riscos = models.TextField(blank=False)
    desc_arquitetura_texto = models.TextField(blank=False)
    desc_arquitetura = models.ImageField(upload_to="destino")
    desc_pricipais_abordagens_arquitetura = models.TextField(blank=False)
    desc_restricao_sensibilidade = models.TextField(blank=True)
    modeloArquitetura = models.ForeignKey(ModeloArquitetura)

    def __unicode__(self):
        return '%s' % self.modeloArquitetura

class Tecnologias(models.Model):
    id = models.AutoField(primary_key=True)
    tecnologia = models.CharField(max_length=200)
    justificativa = models.TextField(blank=False)
    modeloArquitetura = models.ForeignKey(ModeloArquitetura)

    def __unicode__(self):
        return '%s' % self.tecnologia

class TradeOff(models.Model):
    id = models.AutoField(primary_key=True)
    desc_ponto_trade_off = models.TextField(blank=False)
    # um doc tem muitos um ou mais tradeoff#
    modeloArquitetura = models.ForeignKey(ModeloArquitetura)
    #um tradeoff tem uma diretriz#
    diretriz = models.ForeignKey(Diretriz)

    def __unicode__(self):
        return '%s' % self.tradeoff

class Diretriz(models.Model):
    id = models.AutoField(primary_key=True)
    # variaveis da tabela diretriz
    atributo_qualidade_afetado1 = models.CharField(max_length=200)
    atributo_qualidade_afetado2 = models.CharField(max_length=200)
    estimulo1 = models.CharField(max_length=200)
    estimulo2 = models.CharField(max_length=200)
    resposta1 = models.CharField(max_length=200)
    resposta2 = models.CharField(max_length=200)
    estrategia1 = models.CharField(max_length=200)
    estrategia2 = models.CharField(max_length=200)
    #fim da tabela

    def __unicode__(self):
        return '%s' % self.diretriz

class Referencia(models.Model):
    id = models.AutoField(primary_key=True)
    referencia = models.CharField(max_length=200)

    def __unicode__(self):
        return '%s' % self.referencia
