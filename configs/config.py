import json
from datetime import datetime

from logging import exception
from yaml import load, FullLoader
from os import environ, getenv
from pathlib import Path

from global_variaveis import data_formatada


def config():
    """
    Script contendo as configurações inicias do projeto

    Alguns paramentros globais armazenados no arquivo yml do projeto. Para invocalos basta chamar a
    função os.getenv('param')
    """
    environ['DIRETORIO_PROJETO'] = str(Path('.').absolute())

    # Lê o arquivo yml do projeto e cria as variáveis globais do projeto.
    try:

        with open(f'{getenv("DIRETORIO_PROJETO")}/configs/.config.yml', encoding='UTF-8') as f:
            data = load(f, Loader=FullLoader)

        # Email.
        environ['EMAIL_PESSOAL'] = json.dumps(data['email_envio'])

        # Senha
        environ['SENHA_PESSOAL'] = json.dumps(data['senha'])

        # Datas.
        environ['DATAS_INPUT'] = json.dumps(data['setar_data'])

        # Tipo email: outlook, gmail.
        environ['TIPO_EMAIL'] = json.dumps(data['tipos_email'])

        # Email para destinatario
        environ['EMAIL_DESTINATARIO'] = json.dumps(data['email_destinatario'])

        if data['setar_data'] is None:
            environ['DATAS_INPUT'] = json.dumps(data_formatada)

        elif data['setar_data'] is not None:
            try:
                dates_finally = datetime.strptime(data['setar_data'], '%d/%m/%Y').date()

            except ValueError:
                raise exception('Formato fora do padrão, favor colocar o formato certo: mm/yyyy')
            environ['DATAS_INPUT'] = json.dumps(data['setar_data'])

    except Exception:
        raise exception('Não foi possível ler o arquivo .gitlab-ci.yml')


config()
