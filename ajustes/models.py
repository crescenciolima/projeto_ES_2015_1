#coding:utf-8
from django.db import models

# Create your models here.
class Empresa(models.Model):

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    nome = models.CharField(max_length=255)
    cnpj = models.DecimalField(max_digits=14, decimal_places=0, help_text="Somente números")
    telefone = models.DecimalField(max_digits=10, decimal_places=0, help_text="Somente números")
    logo = models.ImageField(upload_to="fotos", blank=True)

    def __unicode__(self):
        return '%s' % self.nome
