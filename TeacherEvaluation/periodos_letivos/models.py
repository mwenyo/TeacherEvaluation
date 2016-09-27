from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class PeriodoLetivo(models.Model):
    descricao = models.CharField(max_length=200, verbose_name="descrição")
    data_inicio = models.DateField("Data de Início")
    data_termino = models.DateField("Data de Término")
    status = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1)])

    class Meta:
        verbose_name = "Período Letivo"
        verbose_name_plural = "Períodos Letivos"

    def __str__(self):
        return self.descricao