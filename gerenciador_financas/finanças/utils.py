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

    linhas = texto.split('\n')
    for linha in linhas:
        if 'Valor' in linha:
            valor = linha.split(':')[-1].strip()
            valor = re.sub(r'[^\d,.-]', '', valor).replace(',', '.')
            if valor:
                try:
                    valor = float(valor)
                except ValueError:
                    valor = None
        
        if 'Recebido' in linha or 'Crédito' in linha or 'Receita' in linha or 'Recibo' in linha:
            tipo = 'R'  # Se encontrar palavras que indicam receita
        
        if 'Data' in linha:
            data = linha.split(':')[-1].strip()
            try:
                data = datetime.strptime(data, '%d/%m/%Y').date()
            except ValueError:
                data = None

    if data is None:
        data = datetime.now().date()

    return {
        'valor': valor if valor is not None else 0.0,
        'data': data,
        'descricao': 'Recibo/Boleto',
        'tipo': tipo
    }