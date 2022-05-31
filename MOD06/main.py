import pandas
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys


cep = sys.argv[1]

if cep:
    # Abrindo o navegador
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://buscacepinter.correios.com.br/app/endereco/index.php?t')
    elem = driver.find_element_by_id('endereco')
    elem.clear()

    time.sleep(1)

    elem.send_keys('41630010')
    elem_cmb = driver.find_element_by_name('tipoCEP')
    elem_cmb.click()
    driver.find_element_by_xpath(
        '/html/body/main/form/div[1]/div[1]/div/div[2]/div/div[2]/select/option[6]'
    ).click()

    driver.find_element_by_xpath(
        '/html/body/main/form/div[1]/div[1]/div/div[3]/div/div/button'
    ).click()

    logradouro = driver.find_element_by_xpath(
        '/html/body/main/form/div[1]/div[2]/div/div[3]/table/tbody/tr/td[1]'
    ).text
    bairro = driver.find_element_by_xpath(
        '/html/body/main/form/div[1]/div[2]/div/div[3]/table/tbody/tr/td[2]'
    ).text
    localidade = driver.find_element_by_xpath(
        '/html/body/main/form/div[1]/div[2]/div/div[3]/table/tbody/tr/td[3]'
    ).text

    time.sleep(1)
    driver.close()

    print("""
    Para o CEP {} temos:
    
        Endereço: {}
        Bairro: {}
        Localidade: {}
    """.format(
    cep,
    logradouro, 
    bairro, 
    localidade
    ))

