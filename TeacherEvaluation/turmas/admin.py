from django.contrib import admin
from turmas.models import Turma

# Register your models here.

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'turno', 'ano', 'ativo', 'curso', 'periodo_letivo', 'sala')