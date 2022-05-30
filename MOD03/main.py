#%%
from matplotlib.pyplot import text
import requests 
import json


#%%
url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'
ret = requests.get(url)

#%%
if ret:
    print(ret)
else:
    print('Fail')

# %%
dolar = json.loads(ret.text)['USDBRL']

# %%
print(f" 100 dolares hoje custam {float(dolar['bid']) * 100} reais")
# %%
# Definindo uma função
# def cotacao(valor, moeda):
#     url = f'https://economia.awesomeapi.com.br/json/last/{moeda}'
#     ret = requests.get(url)
#     dolar = json.loads(ret.text)[moeda.replace('-', '')]
#     print(f" {valor} {moeda[:3]} hoje custam {float(dolar['bid']) * valor} {moeda[-3:]}")



# %%
#     lst_money = [
#         "USD-BRL",
#         "EUR-BRL",
#         "BTC-BRL",
#         "JPY-BRL",
#         "RPL-BRL"
#     ]

# multi_moeda(20, "USD-BRL")
# %%
# Decorador

def error_check(func):
    def inner_func(*args, **kargs):
        try:
            func(*args, **kargs)
        except:
            print(f"{func.__name__} falhou")
    return inner_func


@error_check
def multi_moeda(valor, moeda):
    url = f'https://economia.awesomeapi.com.br/json/last/{moeda}'
    ret = requests.get(url)
    dolar = json.loads(ret.text)[moeda.replace('-', '')]
    print(
        f"{valor} {moeda[:3]} hoje custam {float(dolar['bid']) * valor} {moeda[-3:]} reais")


multi_moeda(20,"USD-BRL")
multi_moeda(20,"EUR-BRL")
multi_moeda(20,"BTC-BRL")
multi_moeda(20,"JPY-BRL")
multi_moeda(20,"RPL-BRL")

# %%
# Simulando um erro de conexão
import backoff
import random


@backoff.on_exception(backoff.expo, (ConnectionAbortedError, ConnectionRefusedError, TimeoutError), max_tries=10)
def test_func(*args, **kargs):
    rnd = random.random()
    print(f"""
            RND: {rnd}
            args: {args if args else 'sem args'}
            kargs: {kargs if kargs else 'sem kargs'}
    """)
    if rnd < .2:
        raise ConnectionAbortedError('Coenxão foi finalizada')
    elif rnd < .4:
        raise ConnectionRefusedError('Conexão foi recusada')
    elif rnd < .6:
        raise TimeoutError('Tempo de espera excedido')
    else:
        return "Ok!"


# %%
test_func()
# %%
test_func(42)
# %%
test_func(42, 51, nome="Vianez")
# %%
# Criando logs e formatando-o através de parâmetros
# A partir de que momento eu gostaria de receber mensagens?
import logging


log = logging.getLogger()
log.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
log.addHandler(ch)


# %%
import backoff
import random


@backoff.on_exception(backoff.expo, (ConnectionAbortedError, ConnectionRefusedError, TimeoutError), max_tries=10)
def test_func(*args, **kargs):
    rnd = random.random()
    log.debug(f"RND: {rnd}")
    log.info(f"args: {args if args else 'sem args'}")
    log.info(f"kargs: {kargs if kargs else 'sem kargs'}")
    if rnd < .2:
        log.error('Conexão foi finalizada')
        raise ConnectionAbortedError('Conexão foi finalizada')
    elif rnd < .4:
        log.error('Conexão foi recusada')
        raise ConnectionRefusedError('Conexão foi recusada')
    elif rnd < .6:
        log.error('Tempo de espera excedido')
        raise TimeoutError('Tempo de espera excedido')
    else:
        return "Ok!"

# %%
test_func()
# %%
