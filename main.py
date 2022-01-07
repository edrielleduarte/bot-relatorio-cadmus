from logging import exception, info, INFO, basicConfig
from os import getcwd, system
from pathlib import Path
from time import sleep
from selenium.webdriver.common.by import By

from ChromeDriver.chromedrive import ChromeDriver
from Cookie.cookie import Cookies
from global_variaveis import variables, nome_vagas, localidade, descricao
import configs.config
from src.email.Email import enviar_email
from src.etapas import scroll_pag, processo_extracao_dados, criacao_planilha_xlsx
import time

basicConfig(level=INFO)
ROOT_DIR = str(Path(getcwd()))
CHROME_PORT = '9222'
url = 'https://cadmus.com.br/vagas-tecnologia/'


def create_profile():
    call_start_chrome = r'start "Chrome" chrome.exe'
    call_port = fr'--remote-debugging-port={CHROME_PORT}'
    chrome_profile = fr'{ROOT_DIR}\bin\chromeprofile'
    call_data_dir = fr'--user-data-dir="{chrome_profile}"'

    comm = fr'{call_start_chrome} {call_port} {call_data_dir}'

    system(comm)


def main():
    inicio = time.time()
    try:
        info('Iniciando')
        chrome_driver = ChromeDriver(ROOT_DIR, CHROME_PORT).driver()
        chrome_driver.get(url)
        sleep(10)

        aceite_cookie = Cookies(chrome_driver)

        sleep(2)

        scroll_pag(chrome_driver)

        sleep(10)

        tabela_linha = chrome_driver.find_element(By.XPATH, variables['table'])
        primeira_linha = tabela_linha.find_elements(By.XPATH, './div')

        # # Processo de extração do for
        processo_extracao_dados(chrome_driver, primeira_linha, nome_vagas, localidade, descricao)

        # Cria a planilha com as informações
        criacao_planilha_xlsx(nome_vagas, localidade, descricao)

        # Envio da planilha para o email
        nome_arquivo = str(Path(ROOT_DIR, 'Planilha Relatorio', 'Planilha Analitica.xlsx'))
        sleep(2)
        enviar_email(nome_arquivo)
        sleep(1)

    except Exception:
        exception('Erro no projeto')

    finally:
        chrome_driver.close()
        sleep(2)
    fim = time.time()
    print(fim - inicio)


if __name__ == '__main__':
    main()
