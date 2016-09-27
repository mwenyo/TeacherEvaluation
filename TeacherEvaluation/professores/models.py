from django.db import models
from django.contrib.auth.models import User
from eixos.models import Eixo

# Create your models here.

class Professor(models.Model):
    qualificacao = models.CharField("qualificação", max_length=200)
    usuario = models.OneToOneField(User)
    eixo = models.ForeignKey(Eixo)

    def __str__(self):
        return self.usuario

    @property
    def full_name(self):
        return "%s %s" % (self.usuario.first_name, self.usuario.last_name)

    class Meta:
        verbose_name_plural = "professores"