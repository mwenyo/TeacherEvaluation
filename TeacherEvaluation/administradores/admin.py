from django.contrib import admin
from administradores.models import Administrador

# Register your models here.

@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'cargo', 'setor')