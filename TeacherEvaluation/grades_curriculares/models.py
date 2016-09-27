from django.db import models
from django.core.validators import MinValueValidator
from disciplinas.models import Disciplina
from professores.models import Professor
from turmas.models import Turma

# Create your models here.

class GradeCurricular(models.Model):
    carga_horaria = models.PositiveSmallIntegerField("carga horária", validators=[MinValueValidator(1)])
    obrigatorio = models.PositiveSmallIntegerField("obrigatório", default=1, validators=[MinValueValidator(1)])
    disciplina = models.ForeignKey(Disciplina, verbose_name="disciplina")
    professor = models.ForeignKey(Professor, verbose_name="professor")
    turma = models.ForeignKey(Turma, verbose_name="turma")

    class Meta:
        verbose_name_plural = "Grades Curriculares"