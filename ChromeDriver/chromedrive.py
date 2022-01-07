import profile
from json import dumps
import chromedriver_autoinstaller
from logging import info, debug
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import SessionNotCreatedException


class ChromeDriver:
    __driver: webdriver.Chrome

    def __init__(self, root_dir: str, port: str):
        self.profile = None
        self.__chrome_options = Options()
        self.__root_dir = root_dir
        self.__chrome_options.add_experimental_option('debuggerAddress', f'localhost:{port}')

        # Configuration para caminho de download de arquivo por click.
        self.__prefs = {"download": {
            "default_directory": str(Path(self.__root_dir, 'downloads-boletos')),
            "directory-upgrade": True,
            # "safebrowsing.enabled": True,
            "prompt_for_download": True,
            "extensions_to_open": ""
        }}

    def driver(self) -> webdriver.Chrome:
        try:
            chromedriver_autoinstaller.install()
            options = Options()
            options.add_argument("--start-maximized")
            options.add_experimental_option("prefs", self.__prefs)

            driver = webdriver.Chrome(options=options)


        except SessionNotCreatedException:
            raise Exception('Versão do Chrome incompatível com a do driver')

        except Exception:
            raise Exception('Não foi possível inicializar o Chrome Driver do Selenium')

        else:
            info('Sessão do Chrome iniciada com sucesso!')

            return driver
