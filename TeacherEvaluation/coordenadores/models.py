from django.db import models
from modalidades.models import Modalidade
from professores.models import Professor

# Create your models here.

class Coordenador(models.Model):
    professor = models.ForeignKey(Professor)
    modalidade = models.ForeignKey(Modalidade)

    def __str__(self):
        return self.professor.usuario

    class Meta:
        verbose_name_plural = "Coordenadores"