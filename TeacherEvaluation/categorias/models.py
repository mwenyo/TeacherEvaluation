from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return '/categorias/%s/' % self.id