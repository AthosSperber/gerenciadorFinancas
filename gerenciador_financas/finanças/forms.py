from django import forms
from .models import Transacao

class TransacaoForm(forms.ModelForm):
    class Meta:
        model = Transacao
        fields = ['descricao', 'valor', 'tipo', 'data']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }


class UploadReciboForm(forms.Form):
    imagem = forms.ImageField()
    descricao = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Descrição (opcional)'}))