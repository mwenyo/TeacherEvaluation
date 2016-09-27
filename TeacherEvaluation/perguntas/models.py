from django.db import models
from categorias.models import Categoria

# Create your models here.

class Pergunta(models.Model):
    cabecalho = models.CharField('Cabeçalho', max_length=200)
    categoria = models.ForeignKey(Categoria, verbose_name="Categoria")
    
    def __str__(self):
        return self.cabecalho

    def get_absolute_url(self):
        return '/perguntas/%s/' % self.id