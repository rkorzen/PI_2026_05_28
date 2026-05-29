# pip install -r requirements.txt
# pip install requests
import requests

response = requests.get("https://api.nbp.pl/api/exchangerates/tables/A/")

print(response.status_code)
data = response.json()
rates = data[0]["rates"]

code = "USD"
value = 100 # to sa zlotowki

for rate in rates:
    if rate["code"] == code:
        print(value / rate["mid"])



