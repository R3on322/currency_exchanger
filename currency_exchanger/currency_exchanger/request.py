import requests
import secrets

payload = {}
headers= {
  "apikey": secrets.API_TOKEN
}

response = requests.request("GET", secrets.BASE_CURRENCY_URL, headers=headers, data = payload)

status_code = response.status_code
result = response.text
