from time import sleep
from webbrowser import Chrome

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as e_c


class Cookies:
    __driver: Chrome
    __tempo_carregamento: int = 2

    def __init__(self, driver):
        self._btn_aceitar = 'aceitar'
        self.__driver = driver

        self.exec()

    def exec(self):

        print('Procurando cookies ...')

        try:
            self.fechar_cookie().click()

        except:
            print('Não foi encontrado button de cookie, o bot irá da sequencia')

        else:
            print('Cookies do Portal foram aceitos.')

    def fechar_cookie(self) -> WebElement:
        btn_aceitar_cookie = WebDriverWait(self.__driver, 2).until(
            e_c.presence_of_element_located((By.ID, self._btn_aceitar)))

        sleep(2)

        return btn_aceitar_cookie