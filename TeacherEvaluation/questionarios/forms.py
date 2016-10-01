from django import forms
from questionarios.models import Questionario

class QuestionarioForm(forms.ModelForm):
    class Meta:
        model = Questionario
        fields = ('administrador', 'data', 'perguntas')
        widgets = {
            'data': forms.TextInput(attrs={'class': 'form-control'}),
        }