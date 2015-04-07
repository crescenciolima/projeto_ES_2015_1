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


class VerDescricao(models.Model):
    id = models.AutoField(primary_key=True)
    desc_visao_atual = models.TextField(blank=False)
    desc_tipo_elementos = models.TextField(blank=False)
    desc_relacao_elementos = models.TextField(blank=False)
    desc_propriedades = models.TextField(blank=False)
    desc_restricoes = models.TextField(blank=False)

    def __unicode__(self):
        return '%s' % self.desc_tipo_elementos

    class Meta:
		verbose_name = 'Ver Descricao'
		verbose_name_plural = 'Ver Descricoes'
		ordering = ['desc_visao_atual']

class StakeHolders(models.Model):
    desc_stakeholders = models.CharField(max_length=150, blank=False)
    desc_precupacoes = models.CharField(max_length=300, blank=False)
    desc_nivel_detalhe = models.TextField(blank=False)
    verdescricao = models.ForeignKey(VerDescricao)

    def __unicode__(self):
        return '%s' % self.desc_precupacoes

class ApresentacaoBehavioral(models.Model):
    id = models.AutoField(primary_key=True)
    diagrama_sequencia_interacao = models.ImageField(upload_to="destino")
    nome = models.CharField(max_length= 150, blank=False)

    def __unicode__(self):
        return '%s' % self.nome

    class Meta:
		verbose_name = 'Apresentacao Behavioral'
		verbose_name_plural = 'Apresentacoes Behaviorais'
		ordering = ['nome']

class VistaBehavioral(models.Model):
    id = models.AutoField(primary_key=True)
    desc_comportamento_dominio = models.TextField(blank=False)
    desc_comportamento = models.ImageField(upload_to="destino")
    verdescricao = models.ForeignKey(VerDescricao)
    apresentacaobehavioral = models.ForeignKey(ApresentacaoBehavioral)

    def __unicode__(self):
        return '%s' % self.desc_comportamento_dominio

    class Meta:
		verbose_name = 'Vista Behavioral'
		verbose_name_plural = 'Vistas Behaviorais'
		ordering = ['desc_comportamento_dominio']

class DiretrizesVariabilidade(models.Model):
    id = models.AutoField(primary_key=True)
    apresentacaobehavioral = models.ForeignKey(ApresentacaoBehavioral)
    mensagem = models.TextField(blank=False)

    def __unicode__(self):
        return '%s' % self.mensagem

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
    desc_vista_behavioral = models.ForeignKey(VistaBehavioral)

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

class ModuloCatalog (models.Model):
        id = models.AutoField(primary_key=True)
        nome = models.CharField(max_length= 150, blank=False)
        digrama_modulo = models.ImageField(upload_to="destino", blank=True)
        descricao_modulo = models.TextField(blank=False)
        modeloArquitetura = models.ForeignKey(ModeloArquitetura, blank=True, null=False)


        def __unicode__(self):
            return '%s' % self.descricao_modulo

        class Meta:
		verbose_name = 'Modulo Catalog'
		verbose_name_plural = 'Modulos Catalog'
        ordering = ['nome']

class ComponenteModulo(models.Model):
        id = models.AutoField(primary_key=True)
        diagrama_componente = models.ImageField(upload_to="destino", blank=True)
        descricao_componente = models.TextField(blank=False)
        funcionalidades_relacionadas = models.CharField(max_length=300)
        diretriz = models.ForeignKey(Diretriz)
        moduloCatalog = models.ForeignKey(ModuloCatalog)

        def __unicode__(self):
            return '%s' % self.descricao_componente

        class Meta:
		verbose_name = 'Componente'
		verbose_name_plural = 'Componentes'
        ordering = ['diagrama_componente']


class ApresentacaoModulo(models.Model):
    id = models.AutoField(primary_key=True)
    modulo = models.ForeignKey(ModuloCatalog)
    descricao_relacionamento = models.TextField(blank=False)
    #modeloArquitetura = models.ForeignKey(ModeloArquitetura, blank=True, null=False)

    def __unicode__(self):
            return '%s' % self.modulo

    class Meta:
        verbose_name = 'Apresentacao dos modulo'
        ordering = ['modulo']

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

class VerDescricao(models.Model):
    id = models.AutoField(primary_key=True)
    desc_visao_atual = models.TextField(blank=False)
    desc_tipo_elementos = models.TextField(blank=False)
    desc_relacao_elementos = models.TextField(blank=False)
    desc_propriedades = models.TextField(blank=False)
    desc_restricoes = models.TextField(blank=False)

    def __unicode__(self):
        return '%s' % self.desc_tipo_elementos

    class Meta:
		verbose_name = 'Ver Descricao'
		verbose_name_plural = 'Ver Descricoes'
		ordering = ['desc_visao_atual']

class StakeHolders(models.Model):
    desc_stakeholders = models.CharField(max_length=150, blank=False)
    desc_precupacoes = models.CharField(max_length=300, blank=False)
    desc_nivel_detalhe = models.TextField(blank=False)
    verdescricao = models.ForeignKey(VerDescricao)

    def __unicode__(self):
        return '%s' % self.desc_precupacoes

class ApresentacaoBehavioral(models.Model):
    id = models.AutoField(primary_key=True)
    diagrama_sequencia_interacao = models.ImageField(upload_to="destino")
    nome = models.CharField(max_length= 150, blank=False)

    def __unicode__(self):
        return '%s' % self.nome

    class Meta:
		verbose_name = 'Apresentacao Behavioral'
		verbose_name_plural = 'Apresentacoes Behaviorais'
		ordering = ['nome']

class VistaBehavioral(models.Model):
    id = models.AutoField(primary_key=True)
    desc_comportamento_dominio = models.TextField(blank=False)
    desc_comportamento = models.ImageField(upload_to="destino")
    verdescricao = models.ForeignKey(VerDescricao)
    apresentacaobehavioral = models.ForeignKey(ApresentacaoBehavioral)

    def __unicode__(self):
        return '%s' % self.desc_comportamento_dominio

    class Meta:
		verbose_name = 'Vista Behavioral'
		verbose_name_plural = 'Vistas Behaviorais'
		ordering = ['desc_comportamento_dominio']

class DiretrizesVariabilidade(models.Model):
    id = models.AutoField(primary_key=True)
    apresentacaobehavioral = models.ForeignKey(ApresentacaoBehavioral)
    mensagem = models.TextField(blank=False)

    def __unicode__(self):
        return '%s' % self.mensagem


class DescricaoView(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.TextField(blank=False)

    def __unicode__(self):
        return '%s' % self.descricao

    class Meta:
        verbose_name = 'Descricao da view'
        verbose_name_plural = 'Descricao das views'
        ordering = ['id']
