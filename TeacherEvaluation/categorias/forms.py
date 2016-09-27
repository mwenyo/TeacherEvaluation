from django import forms
from categorias.models import Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('nome',)
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }