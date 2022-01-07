from os import getcwd
from pathlib import Path
from time import sleep
from logging import info, INFO, basicConfig

from pandas import DataFrame
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as e_c

from global_variaveis import variaveis_dic

basicConfig(level=INFO)


def scroll_pag(chrome_driver):
    try:
        chrome_driver.execute_script('window.scrollBy(0, 900)')
    except:
        pass


def processo_extracao_dados(chrome_driver, primeira_linha, nome_vagas, localidade, descricao):
    for i, linha in enumerate(primeira_linha, start=1):
        try:
            tabela_linha = chrome_driver.find_element(By.XPATH, variaveis_dic['table'])
            primeira_linha = tabela_linha.find_element(By.XPATH, f'./div[{i}]')
            linhas_nomes_vagas = WebDriverWait(primeira_linha, 10).until(
                e_c.presence_of_element_located((By.XPATH, './div/h3'))).text
            nome_localidade = WebDriverWait(primeira_linha, 10).until(
                e_c.presence_of_element_located((By.XPATH, './div/p[1]'))).text
            nome_vagas.append(linhas_nomes_vagas)
            localidade.append(nome_localidade)
            info(f'{linhas_nomes_vagas}: {nome_localidade}')
            sleep(1)
            btn_vagas = primeira_linha.find_element(By.XPATH, './div/p[2]/a')
            chrome_driver.execute_script('arguments[0].click();', btn_vagas)
            sleep(3)
            # Try/except pra caso não exista descrição.
            try:
                descricoes = chrome_driver.find_element(By.XPATH, variaveis_dic['text_descrition']).text
                print(descricoes)
                descricao.append(descricoes)
            except:
                print('Valor do documento vazio')
                nome_vazio = 'Sem valor encontrado'
                descricao.append(nome_vazio)
                pass
            sleep(1.5)
            chrome_driver.back()
            sleep(5)

        except:
            chrome_driver.execute_script('window.scrollBy(0, 200)')
            pass

    print(len(nome_vagas), len(localidade), len(descricao))
    sleep(5)


def criacao_planilha_xlsx(nome_vagas, localidade, descricao):
    dicionario = {'Nome': nome_vagas, 'Localidade': localidade, 'Descrição da vaga': descricao}
    dataframe = DataFrame(dicionario)
    dataframe.to_excel(str(Path(getcwd(), 'Planilha Relatorio', 'Planilha Analitica.xlsx')),
                       sheet_name='Relatorio',
                       header=True, index=False)

