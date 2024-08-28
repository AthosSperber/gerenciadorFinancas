from django.shortcuts import render, redirect, get_object_or_404
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
    return render(request, 'finanças/transacoes_form.html', {'form': form})

def home(request):
    return render(request, 'finanças/home.html')

def transacao_delete(request, pk):
    transacao = get_object_or_404(Transacao, pk=pk)
    if request.method == 'POST':
        transacao.delete()
        return redirect('transacoes_list')
    return render(request, 'finanças/transacoes_delete.html', {'transacao': transacao})
