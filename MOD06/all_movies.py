from selenium import webdriver
import time
import pandas as pd


# Acessando o navegador e fazendo a coleta da tabela
driver = webdriver.Chrome()
# driver.maximize_window()

def tem_item(xpath, driver = driver):
    try:
        driver.find_element_by_xpath(xpath)
        return True
    except:
        return False
time.sleep(5)
driver.implicitly_wait(10)
driver.get('https://pt.wikipedia.org/wiki/Nicolas_Cage')

# Botão inexistente na pagina da bibliografia do Nicolas Cage
tb_filmes = '//*[@id="dropdown-trigger--40"]'


i = 0
while not tem_item(tb_filmes):
    i+=1
    if i > 5:
        break
    pass

tabela = driver.find_element_by_xpath(
    '/html/body/div/div/div[1]/div[3]/main/div[2]/div[3]/div[1]/table[2]')


# Printando a tela
with open ('print.png', 'wb') as f:
    f.write(driver.find_element_by_xpath(
        '/html/body/div/div/div[1]/div[3]/main/div[2]/div[3]/div[1]/table[1]/tbody/tr[2]/td/div/div/div/a/img'
    ).screenshot_as_png)


# Montando o DataFrame
df = pd.read_html('<table>' + tabela.get_attribute('innerHTML') + '</table>')[0]
driver.close()


# Filtrando um DataFrame
df[df['Ano']==1984]


# Criando um CSV da Tabela coletada
df.to_csv(('movies_nicolas_cage.csv'), sep=';', index=False)

