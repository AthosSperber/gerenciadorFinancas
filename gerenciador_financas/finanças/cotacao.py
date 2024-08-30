import requests
from bs4 import BeautifulSoup

def get_price(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    price = soup.find('fin-streamer', {'data-field': 'regularMarketPrice'}).text
    return price
