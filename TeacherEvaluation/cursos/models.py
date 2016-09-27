from django.db import models
from eixos.models import Eixo
from modalidades.models import Modalidade

# Create your models here.

class Curso(models.Model):
    descricao = models.CharField("descrição", max_length=200)
    sigla = models.CharField(max_length=45)
    eixo = models.ForeignKey(Eixo, on_delete=models.CASCADE)
    modalidade = models.ForeignKey(Modalidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.sigla + ' - ' + self.descricao