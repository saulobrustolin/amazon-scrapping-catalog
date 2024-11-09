from components.database import databaseCatalog

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from selenium.common.exceptions import NoSuchElementException

import time
import random

def acess(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(url)

    page = driver.page_source

    return catalog(page, driver)


def catalog(html, driver):

    # variável de controle do laço
    count = 2

    while True:
        while count < 19:
            try:
                # procurando cada endereço de produto
                elem = driver.find_element(By.XPATH, f'/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[{count}]/div/div/span/div/div/div/div[2]/div/div/div[1]/h2/a')

                # configurando o JSON para enviar
                data = {
                    "url": elem.get_attribute('href')
                }

                # enviando para a tabela 'catalog' do banco de dados
                databaseCatalog(data)

                count += 1
            except NoSuchElementException:
                count = 2
                break
        
        try:
            # procurar pelo elemento de 'next page'
            find = driver.find_element(By.CSS_SELECTOR, '.s-pagination-item.s-pagination-next')
            # converte o elemento de 'find' para uma str do elemento
            outer = find.get_attribute('outerHTML')

            # condicional para caso o botão de 'next page' esteja 'disabled'
            if 's-pagination-disabled' in outer or not outer:
                print('end page.')
                driver.quit()

                # retorna que foi finalizado
                return 'sucesso.'

            # faz o 'click' no ancor do elemento 'next page'
            find.click()
            time.sleep(random.randint(2, 8))
        except NoSuchElementException as e:
            print('Botão de próxima página desabilitado ou não encontrado.')
            driver.quit()

            # apresenta o erro no terminal
            raise e

            # retorna todos os produtos encontrados
            return 'sucesso.'
