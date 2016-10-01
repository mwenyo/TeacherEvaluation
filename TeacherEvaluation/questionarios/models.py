from django.db import models
from administradores.models import Administrador
from perguntas.models import Pergunta

# Create your models here.

class Questionario(models.Model):
	
	administrador = models.ForeignKey(Administrador)
	data = models.DateTimeField()
	perguntas = models.ManyToManyField(Pergunta, through='Questionario_Pergunta')
	
class Questionario_Pergunta(models.Model):
	questionario = models.ForeignKey(Questionario, on_delete=models.CASCADE)
	pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
	data_resposta = models.DateTimeField()
	resposta = models.DecimalField(max_digits=3, decimal_places=1)