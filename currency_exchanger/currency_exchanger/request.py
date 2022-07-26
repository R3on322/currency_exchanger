import requests
from .secrets import API_TOKEN, BASE_CURRENCY_URL, URL_FOR_ETH

def request(API_TOKEN, BASE_CURRENCY_URL):
  payload = {}
  headers = {
    "apikey": API_TOKEN
  }
  response_eth = requests.get(URL_FOR_ETH).json()
  response = requests.request("GET", BASE_CURRENCY_URL, headers = headers, data = payload).json()
  response['rates']['ETH'] = float(response_eth['ETH'])
  return response