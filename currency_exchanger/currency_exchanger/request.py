import requests
from secrets import API_TOKEN

url = "https://api.apilayer.com/exchangerates_data/latest?symbols=USD,BRL,EUR,BTC&base=USD"

payload = {}
headers= {
  "apikey": API_TOKEN
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text

print(result)