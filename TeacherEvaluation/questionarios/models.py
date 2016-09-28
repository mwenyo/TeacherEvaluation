from django.db import models
from administradores.models import Administrador
from perguntas.models import Pergunta

# Create your models here.

class Questionario(models.Model):
	
	administrador = models.ForeignKey(Administrador)
	data = models.DateTimeField()
	pergunta = models.ManyToManyField(Pergunta)