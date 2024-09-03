import pytesseract
import requests
import re
from bs4 import BeautifulSoup
from PIL import Image
from datetime import datetime

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

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
    tipo = 'D'  # Definição padrão para despesa
    descricao = 'Recibo/Boleto'

    linhas = texto.split('\n')
    for linha in linhas:
        # Identificar se é um boleto ou recibo
        if any(keyword in linha.lower() for keyword in ['boleto', 'vencimento', 'cedente', 'agência']):
            descricao = 'Boleto'
            tipo = 'D'
        elif any(keyword in linha.lower() for keyword in ['recibo', 'recebido de', 'importância de']):
            descricao = 'Recibo'
            tipo = 'R'

        # Extrair valor
        if any(keyword in linha.lower() for keyword in ['valor documento', 'total', 'quantia', 'valor']):
            valor_match = re.search(r'(\d{1,3}(?:\.\d{3})*,\d{2})|(\d+,\d{2})', linha)
            if valor_match:
                valor = valor_match.group(0).replace('.', '').replace(',', '.')
                try:
                    valor = float(valor)
                except ValueError:
                    valor = 0.0

        # Extrair data
        if any(keyword in linha.lower() for keyword in ['data', 'vencimento']):
            data_match = re.search(r'(\d{2}/\d{2}/\d{4})|(\d{2}-\d{2}-\d{4})', linha)
            if data_match:
                try:
                    data = datetime.strptime(data_match.group(0), '%d/%m/%Y').date()
                except ValueError:
                    try:
                        data = datetime.strptime(data_match.group(0), '%d-%m-%Y').date()
                    except ValueError:
                        data = None

    # Caso não encontre uma data específica
    if data is None:
        data = datetime.now().date()

    # Caso não encontre um valor específico
    if valor is None:
        valor = 0.0

    return {
        'valor': valor,
        'data': data,
        'descricao': descricao,
        'tipo': tipo
    }