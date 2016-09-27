from django.contrib import admin
from coordenadores.models import Coordenador

# Register your models here.

@admin.register(Coordenador)
class CoordenadorAdmin(admin.ModelAdmin):
    list_display = ('professor', 'modalidade')