from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Modalidade(models.Model):
    descricao = models.CharField(max_length=200, verbose_name="descrição")
    tempoAula = models.PositiveIntegerField("Tempo de Aula", validators=[MinValueValidator(1)])

    def __str__(self):
        return self.descricao