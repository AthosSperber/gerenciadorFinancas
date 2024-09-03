import pytesseract
import requests
from bs4 import BeautifulSoup
from PIL import Image


def get_price(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return "Erro ao acessar a página"
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    price_element = soup.find('fin-streamer', {'data-field': 'regularMarketPrice'})
    
    if price_element:
        return price_element.text
    else:
        return "Preço não encontrado"


def extrair_dados_recibo(imagem_caminho):
    imagem = Image.open(imagem_caminho)
    texto = pytesseract.image_to_string(imagem)
    
    valor = None
    data = None
    # imaginar que o texto tem as linhas 'Valor: 100,00' e 'Data: 01/09/2024'
    linhas = texto.split('\n')
    for linha in linhas:
        if 'Valor' in linha:
            valor = linha.split(':')[-1].strip()
        if 'Data' in linha:
            data = linha.split(':')[-1].strip()
    
    return {
        'valor': valor,
        'data': data,
        'descricao': 'Recibo/Boleto'
    }