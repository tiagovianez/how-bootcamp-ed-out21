import requests
import json
from datetime import date, datetime


def cotacao(valor):
    url = "https://economia.awesomeapi.com.br/last/USD-BRL"
    ret = requests.get(url)
    dolar = json.loads(ret.text)["USDBRL"]
    return(float(dolar['bid'])*valor)

    
moeda = cotacao(1)
print("Cotação atual: {}".format(moeda))


with open('cambio.csv', 'a') as f:
    f.write(
        "{};{}\n".format(datetime.strftime(datetime.now(), '%d/%m/%Y %H:%M'), moeda)
    )

