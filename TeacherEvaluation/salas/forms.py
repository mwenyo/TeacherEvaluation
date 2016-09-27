from django import forms
from salas.models import Sala

class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ('nome',)
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }