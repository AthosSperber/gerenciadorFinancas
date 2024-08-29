import plotly.graph_objs as go
from plotly.offline import plot
from django.shortcuts import render, redirect, get_object_or_404
from .models import Transacao
from .forms import TransacaoForm

def transacoes_list(request):
    transacoes = Transacao.objects.all()
    saldo = sum([t.valor if t.tipo == 'R' else -t.valor for t in transacoes])

    receitas = sum(t.valor for t in transacoes if t.tipo == 'R')
    despesas = sum(t.valor for t in transacoes if t.tipo == 'D')

    fig = go.Figure(data=[go.Bar(x=['Receitas', 'Despesas'], y=[receitas, despesas], marker_color=['green', 'red'])])
    graphic = plot(fig, output_type='div')

    return render(request, 'finanças/transacoes_list.html', {
        'transacoes': transacoes,
        'saldo': saldo,
        'graphics': graphic,
        })

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
