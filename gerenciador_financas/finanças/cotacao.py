import requests
from bs4 import BeautifulSoup

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
