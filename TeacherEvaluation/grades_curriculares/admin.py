from django.contrib import admin
from grades_curriculares.models import GradeCurricular

# Register your models here.

@admin.register(GradeCurricular)
class GradeCurricularAdmin(admin.ModelAdmin):
    list_display = ('turma_id', 'disciplina_id', 'professor_id', 'carga_horaria', 'obrigatorio')