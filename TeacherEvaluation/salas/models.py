from django.db import models

# Create your models here.

class Sala(models.Model):
    nome = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return '/salas/%s/' % self.id