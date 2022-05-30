#%%
from re import L
import requests
from bs4 import BeautifulSoup as bs
import logging
import pandas as pd
from sqlalchemy import false


#%%
url = 'https://portalcafebrasil.com.br/todos/podcasts/'


#%%
ret = requests.get(url)
ret.text


# %%
soup = bs(ret.text)
soup


# %%
# Trazendo o título e o link da página

print(soup.find('h5').text)
print(soup.find('h5').a['href'])


# %%
# Trazendo todos os títulos e links

lst_podcast = soup.find_all('h5')
for item in lst_podcast:
    print(f"EP: {item.text} \nLink: {item.a['href']}")

# %%
# Google Inspect | Parte 02

url = 'https://portalcafebrasil.com.br/todos/podcasts/page/{}/?ajax=true'
url.format(26)


# %%
# Criando uma função para coletar as informações da lista

def get_podcast(url):
    ret = requests.get(url)
    soup = bs(ret.text)
    return soup.find_all('h5')

get_podcast(url.format(26))

# %%
# Definindo uma logging de monitoramento de erros

log = logging.getLogger()
log.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
log.addHandler(ch)

# %%
# Criando um loop até conseguir coletar uma resposta

i = 1
lst_podcast = []
lst_get = get_podcast(url.format(i))
log.debug(f"Coletado {len(lst_get)} episódios do link {url.format(i)}")
while len(lst_get) > 0:
    lst_podcast = lst_podcast + lst_get
    i += 1
    lst_get = get_podcast(url.format(i))
    log.debug(f"Coletado {len(lst_get)} episódios do link {url.format(i)}")


# %%
# Quantidade de episódios encontrados
len(lst_podcast)


# %%
# Criando um DataFrame

df = pd.DataFrame(columns=['nome', 'link'])

for item in lst_podcast:
    df.loc[df.shape[0]] = [item.text, item.a['href']]


# %%
df.shape


# %%
# Exportando o DataFrame
df.to_csv('podcast_db.csv', sep=';', index=False)

