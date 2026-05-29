# pip install -r requirements.txt
import requests

response = requests.get("https://api.nbp.pl/api/exchangerates/tables/A/")

print(response.status_code)
print(response.json())

code = "USD"
value = 100 # to sa zlotowki

