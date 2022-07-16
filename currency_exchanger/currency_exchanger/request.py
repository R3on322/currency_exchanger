import requests
import secrets

def request(API_TOKEN, BASE_URL):
  payload = {}
  headers = {
    "apikey": API_TOKEN
  }
  response = requests.request("GET", BASE_URL, headers=headers, data = payload)
  return response