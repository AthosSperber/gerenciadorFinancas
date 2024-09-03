import pytesseract
from PIL import Image
from plotly import graph_objs as go
from plotly.offline import plot
from django.shortcuts import render, redirect, get_object_or_404
from .models import Transacao, Ticker, Recibo
from .forms import TransacaoForm, ReciboForm
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

    transacoes = Transacao.objects.all()
    saldo = sum([t.valor if t.tipo == 'R' else -t.valor for t in transacoes])
    return render(request, 'finanças/cotacao.html', {
        'cotacoes': cotacoes,
        'saldo': saldo})

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


def upload_recibo(request):
    if request.method == 'POST':
        form = ReciboForm(request.POST, request.FILES)
        if form.is_valid():
            recibo = form.save()
            texto_extraido = extrair_texto_recibo(recibo.imagem.path)
            dados_transacao = parse_texto_para_transacao(texto_extraido)
            if dados_transacao:
                transacao = Transacao.objects.create(**dados_transacao)
                recibo.transacao = transacao
                recibo.save()
                return redirect('transacoes_list')
            else:
                context = {
                    'form': form,
                    'erro': 'Não foi possível extrair informações válidas do recibo.'
                }
                return render(request, 'finanças/upload_recibo.html', context)
    else:
        form = ReciboForm()
    return render(request, 'finanças/upload_recibo.html', {'form': form})

def extrair_texto_recibo(caminho_imagem):
    imagem = Image.open(caminho_imagem)
    texto = pytesseract.image_to_string(imagem, lang='por')
    return texto

def parse_texto_para_transacao(texto):
    # Implementação simples usando expressões regulares
    import re
    resultado = {}
    # Extrair valor
    valor_match = re.search(r'R\$\s?(\d+,\d{2})', texto)
    if valor_match:
        valor = valor_match.group(1).replace('.', '').replace(',', '.')
        resultado['valor'] = float(valor)
    else:
        return None
    # Extrair data
    data_match = re.search(r'Data[:\-]\s?(\d{2}/\d{2}/\d{4})', texto)
    if data_match:
        from datetime import datetime
        data_str = data_match.group(1)
        resultado['data'] = datetime.strptime(data_str, '%d/%m/%Y').date()
    else:
        return None
    # Extrair descrição
    descricao_match = re.search(r'Descrição[:\-]\s?(.*)', texto)
    if descricao_match:
        resultado['descricao'] = descricao_match.group(1).strip()
    else:
        resultado['descricao'] = 'Recibo sem descrição'
    # Definir tipo e categoria (pode ser aprimorado conforme necessidade)
    resultado['tipo'] = 'D'  # Assumindo que recibos são despesas
    resultado['categoria'] = 'Outros'
    return resultado