from django.db import models

BOOL_CHOICES = ((True, 'Sim'), (False, 'Nao'))


class ModeloArquitetura(models.Model):
    nome = models.CharField(max_length=150, blank=False)
    introducao = models.TextField(blank=False)
    referencia_escolha = models.BooleanField(choices=BOOL_CHOICES)

    def __unicode__(self):
        return '%s' % self.nome


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
    atributo_qualidade_afetado1 = models.CharField(max_length=200)
    atributo_qualidade_afetado2 = models.CharField(max_length=200)
    estimulo1 = models.CharField(max_length=200)
    estimulo2 = models.CharField(max_length=200)
    resposta1 = models.CharField(max_length=200)
    resposta2 = models.CharField(max_length=200)
    estrategia1 = models.CharField(max_length=200)
    estrategia2 = models.CharField(max_length=200)
    # fim da tabela

    def __unicode__(self):
        return '%s' % self.diretriz


class TradeOff(models.Model):
    id = models.AutoField(primary_key=True)
    desc_ponto_trade_off = models.TextField(blank=False)
    # um doc tem muitos um ou mais tradeoff#
    modeloArquitetura = models.ForeignKey(ModeloArquiteturaAvaliacao, blank=True, null=False)
    # um tradeoff tem uma diretriz#
    diretriz = models.ForeignKey(Diretriz)

    def __unicode__(self):
        return '%s' % self.desc_ponto_trade_off


class Referencia(models.Model):
    id = models.AutoField(primary_key=True)
    referencia = models.CharField(max_length=200)
    modeloArquitetura = models.ForeignKey(ModeloArquitetura, blank=True, null=False)

    def __unicode__(self):
        return '%s' % self.referencia
