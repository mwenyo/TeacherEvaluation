from django.contrib import admin
from professores.models import Professor

# Register your models here.

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'qualificacao')