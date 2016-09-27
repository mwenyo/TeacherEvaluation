from django import forms
from perguntas.models import Pergunta

class PerguntaForm(forms.ModelForm):
    class Meta:
        model = Pergunta
        fields = ('cabecalho',)
        widgets = {
            'cabecalho': forms.TextInput(attrs={'class': 'form-control'}),
        }