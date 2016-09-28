from django import forms
from perguntas.models import Pergunta

class PerguntaForm(forms.ModelForm):
    class Meta:
        model = Pergunta
        fields = ('cabecalho','categoria')
        widgets = {
            'cabecalho': forms.Textarea(attrs={'rows':'3'}), #'class': 'form-control'}),
        }