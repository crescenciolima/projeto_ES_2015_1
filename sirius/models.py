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


class Apresentacao(models.Model):
    id = models.AutoField(primary_key=True)
    diagrama_de_sequencia = models.ImageField(upload_to="fotos", blank=True)
    descricao = models.CharField(max_length=150, blank=False)

    def __unicode__(self):
        return '%s' % self.descricao

    class Meta:
        verbose_name = 'Apresentacao'
        verbose_name_plural = 'Apresentacoes'
        ordering = ['descricao']


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


class VisaoBehavioral(models.Model):
    id = models.AutoField(primary_key=True)
    descricao_do_comportamento_de_dominio = models.TextField(blank=False)
    diagrama_do_comportamento = models.ImageField(blank=True, upload_to="fotos")
    visao_atual = models.ForeignKey(DescricaoVisaoAtual)
    apresentacao_behavioral = models.ForeignKey(Apresentacao)

    def __unicode__(self):
        return '%s' % self.descricao_do_comportamento_de_dominio

    class Meta:
        verbose_name = 'Visao Comportamental'
        verbose_name_plural = 'Visoes Comportamentais'
        ordering = ['descricao_do_comportamento_de_dominio']


class StakeHoldersImplementacao(models.Model):
    stakeholders = models.CharField(max_length=150, blank=False)
    precupacoes = models.CharField(max_length=300, blank=False)
    nivel_detalhe_da_visao = models.TextField(blank=False)
    visao_de_implementacao = models.ForeignKey(VisaoImplementacao)

    def __unicode__(self):
        return '%s' % self.stakeholders


class StakeHoldersBehavioral(models.Model):
    id = models.AutoField(primary_key=True)
    stakeholders = models.CharField(max_length=150, blank=False)
    precupacoes = models.CharField(max_length=300, blank=False)  #corrigir nome de variavel
    nivel_detalhe_da_visao = models.TextField(blank=False)
    visao_behavioral = models.ForeignKey(VisaoBehavioral)

    def __unicode__(self):
        return '%s' % self.stakeholders


class DiretrizesVariabilidade(models.Model):
    id = models.AutoField(primary_key=True)
    mensagem = models.TextField(blank=False)
    apresentacao_behavioral = models.ForeignKey(Apresentacao)

    def __unicode__(self):
        return '%s' % self.mensagem


class Diretriz(models.Model):
    id = models.AutoField(primary_key=True)
    diretriz = models.CharField(max_length=200)

    def __unicode__(self):
        return '%s' % self.diretriz

    class Meta:
        verbose_name = 'Diretriz'
        verbose_name_plural = 'Diretrizes'
        ordering = ['diretriz']


class ModuloCatalog(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150, blank=False)
    digrama_modulo = models.ImageField(upload_to="fotos", blank=True)
    descricao_de_modulo = models.TextField(blank=False)

    def __unicode__(self):
        return '%s' % self.descricao_de_modulo

    class Meta:
        verbose_name = 'Modulo Catalog'
        verbose_name_plural = 'Modulos Catalog'
        ordering = ['nome']


class ApresentacaoModulo(models.Model):
    id = models.AutoField(primary_key=True)
    modulos = models.CharField(max_length=150, blank=False)
    relacionamento_dos_modulos = models.TextField(blank=False)

    def __unicode__(self):
        return '%s' % self.relacionamento_dos_modulos

    class Meta:
        verbose_name = 'Apresentacao dos modulo'
        ordering = ['relacionamento_dos_modulos']


class ModeloArquitetura(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150, blank=False)
    introducao = models.TextField(blank=False)
    referencia_escolha = models.BooleanField(choices=BOOL_CHOICES)
    drives_arquitetonicos = models.TextField(blank=False)
    visao_comportamental = models.ForeignKey(VisaoBehavioral)
    visao_de_implementacao = models.ForeignKey(VisaoImplementacao)
    visao_atual = models.ForeignKey(DescricaoVisaoAtual)
    modulo_catalog = models.ForeignKey(ModuloCatalog)
    apresentacao_modulo = models.ForeignKey(ApresentacaoModulo)
    diretriz = models.ForeignKey(Diretriz)
    cliques = models.IntegerField(editable=False, default=0)

    def pesquisaModeloArquitetura(pesquisa):
        modeloArquitetura = models.ModeloArquitetura.objects.all(headline_contains=pesquisa);
        return modeloArquitetura

    def __unicode__(self):
        return '%s' % self.nome

    class Meta:
        verbose_name = 'Modelo de Arquitetura'
        verbose_name_plural = 'Modelos de Arquitetura'
        ordering = ['nome']

class ClassificacaoMetricaAvaliacao(models.Model):
    id = models.AutoField(primary_key=True)
    metodoAvaliacao = models.CharField(max_length=300, blank=True)
    objetivo = models.TextField(blank=True)
    tiposAtributo = models.CharField(max_length=300, blank=True)
    faseAvaliacao = models.CharField(max_length=300, blank=True)
    tecnicaAvaliacao = models.TextField(blank=True)
    descricaoProcesso = models.TextField(blank=True)
    validacaoMetodo = models.TextField(blank=True)
    relacaoMetodo = models.CharField(max_length=300, blank=True)


    def __unicode__(self):
        return '%s' % self.metodoAvaliacao


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

class InformacaoArquitetural(models.Model):
    id = models.AutoField(primary_key=True)
    nomeProjeto = models.TextField(max_length=200, blank=False)
    dominioProjeto = models.TextField(max_length=200, blank=False)
    data = models.DateField(blank=True)
    objetivoNegocio = models.TextField(max_length=200, blank=False)
    stakeholders = models.ForeignKey(StakeHoldersBehavioral,blank=True,null=False)
    descricao = models.TextField(max_length=200, blank=False)
    cenario=models.ForeignKey(AtributoDiretriz,blank=True, null=False)
    taticasDesign= models.TextField(max_length=200,blank=False)
    designRacional = models.TextField(max_length=200, blank=False)

    #class Meta:
        #verbose_name = 'Informacao Arquitetural'
        #verbose_name_plural = 'Informacoes Arquiteturais'

    def __unicode__(self):
        return '%s' % self.nomeProjeto


class ModeloArquiteturaAvaliacao(models.Model):
    id = models.AutoField(primary_key=True)
    modeloArquitetura = models.ForeignKey(ModeloArquitetura, blank=True, null=False)
    nome = models.CharField(max_length=150, blank=False)
    descricao_da_qualidade = models.TextField(blank=False)
    descricao_de_nao_riscos = models.TextField(blank=False)
    descricao_de_riscos = models.TextField(blank=False)
    diagrama_de_arquitetura = models.ImageField(upload_to="fotos")
    descricao_da_arquitetura = models.TextField(blank=False)
    pricipais_abordagens_da_arquitetura = models.TextField(blank=False)
    ponto_de_sensibilidade = models.TextField(blank=False)
    restricao_de_sensibilidade = models.TextField(blank=True)
    cliques = models.IntegerField(editable=False, default=0)
    classificacao_metrica_avaliacao = models.ForeignKey(ClassificacaoMetricaAvaliacao,blank=True, null=False)
    informacao_arquitetural = models.ForeignKey(InformacaoArquitetural,blank=True, null=False)


    def pesquisaModeloArquiteturaAvaliacao(pesquisa):
        modeloArquiteturaAvaliacao = models.ModeloArquiteturaAvaliacao.objects.all(headline_contains=pesquisa);
        return modeloArquiteturaAvaliacao

    def __unicode__(self):
        return '%s' % self.nome

    class Meta:
        verbose_name = 'Avaliacao do Modelo de Arquitetura'
        verbose_name_plural = 'Avaliacoes dos Modelos de Arquitetura '
        ordering = ['modeloArquitetura']


class Tecnologias(models.Model):
    id = models.AutoField(primary_key=True)
    tecnologia = models.CharField(max_length=200)
    justificativa = models.TextField(blank=False)
    modeloArquitetura = models.ForeignKey(ModeloArquitetura, blank=True, null=False)

    def __unicode__(self):
        return '%s' % self.tecnologia



class ComponenteModulo(models.Model):
    id = models.AutoField(primary_key=True)
    diagrama_do_componente = models.ImageField(upload_to="fotos", blank=True)
    descricao_do_componente = models.TextField(blank=False)
    funcionalidades_relacionadas = models.CharField(max_length=300)
    diretriz = models.ForeignKey(Diretriz)
    moduloCatalog = models.ForeignKey(ModuloCatalog)

    def __unicode__(self):
        return '%s' % self.descricao_do_componente

    class Meta:
        verbose_name = 'Componente'
        verbose_name_plural = 'Componentes'

    ordering = ['descricao_do_componente']


class TradeOff(models.Model):
    id = models.AutoField(primary_key=True)
    pontos_de_trade_off = models.TextField(blank=False)
    modeloArquitetura = models.ForeignKey(ModeloArquiteturaAvaliacao, blank=True, null=False)
    diretriz = models.ForeignKey(Diretriz)

    def __unicode__(self):
        return '%s' % self.pontos_de_trade_off


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
    modeloArquitetura = models.ForeignKey(ModeloArquitetura, blank=True, null=False)

    def __unicode__(self):
        return '%s' % self.estilo


#codigo siliqua
class TipoPadrao (models.Model):
    nome = models.CharField(max_length=255)
    cliques = models.IntegerField(editable=False, default=0)

    class Meta:
        verbose_name = 'Tipo de Padrao'
        verbose_name_plural = 'Tipos de Padroes'

    def __unicode__(self):
        return '%s' % self.nome

    #@permalink
    #def get_absolute_url(self):
        #r1eturn ('view_tipo_padrao', None, { 'id': self.id })

#codigo siliqua
class TagPadrao(models.Model):

    class Meta:
        verbose_name = 'Tag de Padrao'
        verbose_name_plural = 'Tags de Padrao'

    nome = models.CharField(max_length=255)

    def __unicode__(self):
        return '%s' % self.nome

#codigo siliqua
class Padrao(models.Model):
    nome = models.CharField(max_length=255)
    aliase = models.TextField()
    contexto = models.TextField()
    problema = models.TextField()
    vantagens = models.TextField()
    desvantagens = models.TextField()
    aplicabilidade = models.TextField()
    referencias = models.TextField(verbose_name='referencias')
    padroesRelacionados = models.ManyToManyField("self", blank=True, related_name='padroes', verbose_name='padroes relacionados')
    tipoDePadrao = models.ForeignKey(TipoPadrao, related_name='tipoDePadrao_set', verbose_name='tipo de padrao')
    imagem = models.ImageField(upload_to="fotos", blank=True)
    cliques = models.IntegerField(editable=False, default=0)
    categorias = models.ManyToManyField("TagPadrao", blank=False, related_name='tags')

    class Meta:
        verbose_name = 'Padrao'
        verbose_name_plural = 'Padroes'

    def __unicode__(self):
        return '%s' % self.nome

        #@permalink
        #def get_absolute_url(self):
        #    return ('view_nome', None, { 'nome': self.id })

    #@permalink
    #def get_absolute_url(self):
        #return ('view_padrao', None, { 'id': self.id })
