from django.db import models
from cursos.models import Curso
from salas.models import Sala
from periodos_letivos.models import PeriodoLetivo
from django.core.validators import MinValueValidator

# Create your models here.

class Turma(models.Model):
    nome = models.CharField(max_length=200)
    ano = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1)])
    turno = models.CharField(max_length=200)
    ativo = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1)])
    curso = models.ForeignKey(Curso, verbose_name="Curso")
    periodo_letivo = models.ForeignKey(PeriodoLetivo, verbose_name="Período Letivo")
    sala = models.ForeignKey(Sala, verbose_name="Sala")

    def __str__(self):
        return '{} - {} - {}'.format(self.nome, self.ano, self.turno)

