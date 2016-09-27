from django import forms
from eixos.models import Eixo

class EixoForm(forms.ModelForm):
    class Meta:
        model = Eixo
        fields = ('descricao',)
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
        }