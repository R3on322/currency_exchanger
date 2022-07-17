import requests
import secrets



def request(API_TOKEN, BASE_URL):
  payload = {}
  headers = {
    "apikey": API_TOKEN
  }
  response_eth = requests.get(secrets.URL_FOR_ETH).json()
  response = requests.request("GET", BASE_URL, headers = headers, data = payload).json()
  response['rates']['ETH'] = float(response_eth['result']['ethusd'])
  return response




