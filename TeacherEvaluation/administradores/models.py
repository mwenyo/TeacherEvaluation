from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Administrador(models.Model):
    cargo = models.CharField(max_length=200, default="Pedagogo")
    setor = models.CharField(max_length=200, default="Pedagogia")
    usuario = models.OneToOneField(User)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return "%s %s" % (self.usuario.first_name, self.usuario.last_name)

    class Meta:
        verbose_name_plural = "administradores"