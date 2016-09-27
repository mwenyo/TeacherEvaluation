from django.db import models

# Create your models here.

class Eixo(models.Model):
    descricao = models.CharField(max_length=200, verbose_name="descrição")

    def __str__(self):
        return self.descricao

    def get_absolute_url(self):
        return '/eixos/%s/' % self.id