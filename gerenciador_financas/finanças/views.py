from django.shortcuts import render, redirect
from .models import Transacao
from .forms import TransacaoForm

def transacoes_list(request):
    transacoes = Transacao.objects.all()
    return render(request, 'finanças/transacoes_list.html', {'transacoes': transacoes})

def transacao_create(request):
    if request.method == 'POST':
        form = TransacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transacoes_list')
    else:
        form = TransacaoForm()
    return render(request, 'finanças/transacao_form.html', {'form': form})
