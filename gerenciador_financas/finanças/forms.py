from django import forms
from .models import Transacao

class TransacaoForm(forms.ModelForm):
    class Meta:
        model = Transacao
        fields = ['descricao', 'valor', 'tipo', 'data']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }
