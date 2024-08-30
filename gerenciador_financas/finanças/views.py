from plotly import graph_objs as go
from plotly.offline import plot
from django.shortcuts import render, redirect, get_object_or_404
from .models import Transacao, Ticker
from .forms import TransacaoForm
from .cotacao import get_price

def transacoes_list(request):
    transacoes = Transacao.objects.all()
    saldo = sum([t.valor if t.tipo == 'R' else -t.valor for t in transacoes])

    receitas = sum(t.valor for t in transacoes if t.tipo == 'R')
    despesas = sum(t.valor for t in transacoes if t.tipo == 'D')

    fig = go.Figure(data=[go.Bar(
        x=['Receitas', 'Despesas'], 
        y=[receitas, despesas], 
        marker_color=['green', 'red'], 
        width = 0.25)])
    
    fig.update_layout(
        width = 800,
        title = 'Receitas vs Despesas',
        xaxis_title= 'Categorias',
        yaxis_title = 'Valores',
        autosize = True,
    )
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


def cotacao_view(request):
    tickers = Ticker.objects.all()
    cotacoes = {ticker.nome: get_price(ticker.nome) for ticker in tickers}
    return render(request, 'finanças/cotacao.html', {'cotacoes': cotacoes})

def adicionar_ticker(request):
    if request.method == 'POST':
        ticker_nome = request.POST.get('ticker').upper()
        if ticker_nome:
            Ticker.objects.get_or_create(nome=ticker_nome)
    return redirect('cotacao')

def excluir_ticker(request, ticker_nome):
    ticker = get_object_or_404(Ticker, nome=ticker_nome)
    ticker.delete()
    return redirect('cotacao')
