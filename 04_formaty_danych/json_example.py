import json

text = """[{"table":"A","no":"103/A/NBP/2026","effectiveDate":"2026-05-29","rates":[{"currency":"bat (Tajlandia)","code":"THB","mid":0.1117},{"currency":"dolar amerykański","code":"USD","mid":3.6395},{"currency":"dolar australijski","code":"AUD","mid":2.6034},{"currency":"dolar Hongkongu","code":"HKD","mid":0.4645},{"currency":"dolar kanadyjski","code":"CAD","mid":2.6364},{"currency":"dolar nowozelandzki","code":"NZD","mid":2.1692},{"currency":"dolar singapurski","code":"SGD","mid":2.8473},{"currency":"euro","code":"EUR","mid":4.2322},{"currency":"forint (Węgry)","code":"HUF","mid":0.011937},{"currency":"frank szwajcarski","code":"CHF","mid":4.6401},{"currency":"funt szterling","code":"GBP","mid":4.8806},{"currency":"hrywna (Ukraina)","code":"UAH","mid":0.0822},{"currency":"jen (Japonia)","code":"JPY","mid":0.022848},{"currency":"korona czeska","code":"CZK","mid":0.1743},{"currency":"korona duńska","code":"DKK","mid":0.5663},{"currency":"korona islandzka","code":"ISK","mid":0.029554},{"currency":"korona norweska","code":"NOK","mid":0.3939},{"currency":"korona szwedzka","code":"SEK","mid":0.3928},{"currency":"lej rumuński","code":"RON","mid":0.8065},{"currency":"lira turecka","code":"TRY","mid":0.0793},{"currency":"nowy izraelski szekel","code":"ILS","mid":1.2951},{"currency":"peso chilijskie","code":"CLP","mid":0.004084},{"currency":"peso filipińskie","code":"PHP","mid":0.0591},{"currency":"peso meksykańskie","code":"MXN","mid":0.2099},{"currency":"rand (Republika Południowej Afryki)","code":"ZAR","mid":0.2239},{"currency":"real (Brazylia)","code":"BRL","mid":0.7215},{"currency":"ringgit (Malezja)","code":"MYR","mid":0.9172},{"currency":"rupia indonezyjska","code":"IDR","mid":0.00020367},{"currency":"rupia indyjska","code":"INR","mid":0.038225},{"currency":"won południowokoreański","code":"KRW","mid":0.002412},{"currency":"yuan renminbi (Chiny)","code":"CNY","mid":0.5377},{"currency":"SDR (MFW)","code":"XDR","mid":4.9790}]}]"""

print(type(text))

data = json.loads(text)

print(type(data))

json_text = json.dumps(data)

print(type(json_text))
