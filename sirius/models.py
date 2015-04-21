from django.db import models

BOOL_CHOICES = ((True, 'Sim'), (False, 'Nao'))


class DescricaoVisaoAtual(models.Model):
    id = models.AutoField(primary_key=True)
    visao_atual = models.TextField(blank=False)
    tipo_de_elementos = models.TextField(blank=False)
    relacao_de_elementos = models.TextField(blank=False)
    propriedades = models.TextField(blank=False)
    restricoes = models.TextField(blank=False)

    def __unicode__(self):
        return '%s' % self.visao_atual

    class Meta:
        verbose_name = 'Visao Atual Comportamental'
        verbose_name_plural = 'Visoes Atuais Comportamentais'
        ordering = ['visao_atual']

#filipe
class Apresentacao(models.Model):
    id = models.AutoField(primary_key=True)
    diagrama_de_sequencia = models.ImageField(upload_to="fotos")
    descricao = models.CharField(max_length=150, blank=False)

    def __unicode__(self):
        return '%s' % self.descricao

    class Meta:
        verbose_name = 'Apresentacao'
        verbose_name_plural = 'Apresentacoes'
        ordering = ['descricao']

#saionara
class VisaoImplementacao(models.Model):
    id = models.AutoField(primary_key=True)
    visao_atual = models.TextField(blank=False)
    apresentacao_de_implementacao = models.ForeignKey(Apresentacao)

    def __unicode__(self):
        return '%s' % self.visao_atual

    class Meta:
        verbose_name = 'Visao de Implementacao'
        verbose_name_plural = 'Visoes de Implementacao'
        ordering = ['visao_atual']

#talita
class VisaoBehavioral(models.Model):
    id = models.AutoField(primary_key=True)
    descricao_do_comportamento_de_dominio = models.TextField(blank=False)
    diagrama_do_comportamento = models.ImageField(upload_to="fotos")
    visao_atual = models.ForeignKey(DescricaoVisaoAtual)
    apresentacao_behavioral = models.ForeignKey(Apresentacao)

    def __unicode__(self):
        return '%s' % self.descricao_do_comportamento_de_dominio

    class Meta:
        verbose_name = 'Visao Comportamental'
        verbose_name_plural = 'Visoes Comportamentais'
        ordering = ['descricao_do_comportamento_de_dominio']

#socrates
class StakeHoldersImplementacao(models.Model):
    stakeholders = models.CharField(max_length=150, blank=False)
    precupacoes = models.CharField(max_length=300, blank=False)
    nivel_detalhe_da_visao = models.TextField(blank=False)
    visao_de_implementacao = models.ForeignKey(VisaoImplementacao)

    def __unicode__(self):
        return '%s' % self.stakeholders

#abner
class StakeHoldersBehavioral(models.Model):
    stakeholders = models.CharField(max_length=150, blank=False)
    precupacoes = models.CharField(max_length=300, blank=False) #corrigir nome de variavel
    nivel_detalhe_da_visao = models.TextField(blank=False)
    visao_behavioral = models.ForeignKey(VisaoBehavioral)

    def __unicode__(self):
        return '%s' % self.stakeholders

#filipe
class DiretrizesVariabilidade(models.Model):
    id = models.AutoField(primary_key=True)
    mensagem = models.TextField(blank=False)
    apresentacao_behavioral = models.ForeignKey(Apresentacao)

    def __unicode__(self):
        return '%s' % self.mensagem

#saionara
class ApresentacaoModulo(models.Model):
    id = models.AutoField(primary_key=True)
    relacionamento_dos_modulos = models.TextField(blank=False)

    def __unicode__(self):
        return '%s' % self.relacionamento_dos_modulos

    class Meta:
        verbose_name = 'Apresentacao dos modulo'
        ordering = ['relacionamento_dos_modulos']

#talita
class ModeloArquitetura(models.Model):
    nome = models.CharField(max_length=150, blank=False)
    introducao = models.TextField(blank=False)
    referencia_escolha = models.BooleanField(choices=BOOL_CHOICES)
    drives_arquitetonicos = models.TextField(blank=False)
    visao_comportamental = models.ForeignKey(VisaoBehavioral)
    visao_de_implementacao = models.ForeignKey(VisaoImplementacao)
    visao_atual = models.ForeignKey(DescricaoVisaoAtual)
    modulo_catalog = models.ForeignKey(ApresentacaoModulo)

    def __unicode__(self):
        return '%s' % self.nome

    class Meta:
        verbose_name = 'Modelo de Arquitetura'
        verbose_name_plural = 'Modelos de Arquitetura'
        ordering = ['nome']

#socrates
class ModeloArquiteturaAvaliacao(models.Model):
    id = models.AutoField(primary_key=True)
    modeloArquitetura = models.ForeignKey(ModeloArquitetura, blank=True, null=False)
    descricao_da_qualidade = models.TextField(blank=False)
    descricao_de_nao_riscos = models.TextField(blank=False)
    descricao_de_riscos = models.TextField(blank=False)
    diagrama_de_arquitetura = models.ImageField(upload_to="fotos")
    descricao_da_arquitetura = models.TextField(blank=False)
    pricipais_abordagens_da_arquitetura = models.TextField(blank=False)
    ponto_de_sensibilidade = models.TextField(blank=False)
    restricao_de_sensibilidade = models.TextField(blank=True)

    def __unicode__(self):
        return '%s' % self.modeloArquitetura

    class Meta:
        verbose_name = 'Modelo de Arquitetura Avaliacao'
        verbose_name_plural = 'Modelos de Arquitetura Avaliacao'
        ordering = ['modeloArquitetura']

#abner
class Tecnologias(models.Model):
    id = models.AutoField(primary_key=True)
    tecnologia = models.CharField(max_length=200)
    justificativa = models.TextField(blank=False)
    modeloArquitetura = models.ForeignKey(ModeloArquitetura, blank=True, null=False)

    def __unicode__(self):
        return '%s' % self.tecnologia

#/filipe
class Diretriz(models.Model):
    id = models.AutoField(primary_key=True)
    diretriz = models.CharField(max_length=200)

    def __unicode__(self):
        return '%s' % self.diretriz

    class Meta:
        verbose_name = 'Diretriz'
        verbose_name_plural = 'Diretrizes'
        ordering = ['diretriz']

#saionara
class AtributoDiretriz(models.Model):
    id = models.AutoField(primary_key=True)
    atributos_de_qualidade_afetado = models.CharField(max_length=200)
    estimulo = models.CharField(max_length=200)
    resposta = models.CharField(max_length=200)
    estrategia = models.CharField(max_length=200)
    diretriz = models.ForeignKey(Diretriz)

    def __unicode__(self):
        return '%s' % self.atributos_de_qualidade_afetado

    class Meta:
        verbose_name = 'Atributos da Diretriz'
        verbose_name_plural = 'Atributos das Diretrizes'
        ordering = ['atributos_de_qualidade_afetado']

#talita
class ModuloCatalog(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150, blank=False)
    digrama_modulo = models.ImageField(upload_to="fotos", blank=True)
    descricao_de_modulo = models.TextField(blank=False)
    apresentacaoModulo = models.ForeignKey(ApresentacaoModulo)

    def __unicode__(self):
        return '%s' % self.descricao_de_modulo

    class Meta:
        verbose_name = 'Modulo Catalog'
        verbose_name_plural = 'Modulos Catalog'
        ordering = ['nome']


#socrates
class ComponenteModulo(models.Model):
    id = models.AutoField(primary_key=True)
    diagrama_do_componente = models.ImageField(upload_to="fotos", blank=True)
    descricao_do_componente = models.TextField(blank=False)
    funcionalidades_relacionadas = models.CharField(max_length=300)
    diretriz = models.ForeignKey(Diretriz)
    moduloCatalog = models.ForeignKey(ModuloCatalog)

    def __unicode__(self):
        return '%s' % self.descricao_componente

    class Meta:
        verbose_name = 'Componente'
        verbose_name_plural = 'Componentes'

    ordering = ['descricao_do_componente']

#abner
class TradeOff(models.Model):
    id = models.AutoField(primary_key=True)
    pontos_de_trade_off = models.TextField(blank=False)
    modeloArquitetura = models.ForeignKey(ModeloArquiteturaAvaliacao, blank=True, null=False)
    diretriz = models.ForeignKey(Diretriz)

    def __unicode__(self):
        return '%s' % self.pontos_de_trade_off

#filipe
class Referencia(models.Model):
    id = models.AutoField(primary_key=True)
    referencia = models.CharField(max_length=200)
    modeloArquitetura = models.ForeignKey(ModeloArquitetura, blank=True, null=False)

    def __unicode__(self):
        return '%s' % self.referencia

#saionara
class Estilo(models.Model):
    id = models.AutoField(primary_key=True)
    estilo = models.CharField(max_length=200, blank=False)
    abordagem = models.CharField(max_length=200, blank=False)
    justificativa = models.CharField(max_length=400, blank=False)
    modeloArquitetura = models.ForeignKey(ModeloArquitetura, blank=True, null=False)

    def __unicode__(self):
        return '%s' % self.estilo
