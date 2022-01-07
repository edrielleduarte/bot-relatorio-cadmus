import os.path
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from json import loads


def enviar_email(path_name):
    try:
        email_pessoal = loads(os.getenv("EMAIL_PESSOAL"))[0]
        senha = loads(os.getenv("SENHA_PESSOAL"))[0]
        data_final = loads(os.getenv("DATAS_INPUT"))
        email_tipo = loads(os.getenv('TIPO_EMAIL'))[0]
        email_destinatario = loads(os.getenv('EMAIL_DESTINATARIO'))[0]
        msg = MIMEMultipart()
        porta = 587

        msg['From'] = email_pessoal
        msg['To'] = email_destinatario
        msg['Subject'] = "Relatório Analitico"

        body = "\nOlá, boa tarde! Tudo bem? \n" \
               "Segue em anexo a planilha do Relatorio Analitico com as vagas disponiveis no nosso site referente a data " \
               f"{data_final}." \
               "\nAtenciosamente,\n" \
               "Edrielle Duarte;"

        msg.attach(MIMEText(body, 'plain'))

        file_name = path_name
        attachment = open(file_name, 'rb')

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % os.path.basename(file_name))

        msg.attach(part)

        attachment.close()

        server = smtplib.SMTP(f'smtp.{email_tipo}.com', porta)
        server.starttls()
        server.login(email_pessoal, senha)
        text = msg.as_string()
        server.sendmail(email_pessoal, email_destinatario, text)
        server.quit()
        print('\nEmail enviado com sucesso!')
    except:
        print('Erro ao enviar')
