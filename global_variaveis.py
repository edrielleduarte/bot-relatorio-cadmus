import datetime as dt

variaveis_dic = {
    'table': '/html/body/section[2]/div/div[2]/div/div',
    'btn_vagas': '//*[@id="pfolio"]/div[1]/div/p[2]/a',
    'text_descrition': '/html/body/section/div/div[2]/div[1]/div[1]/p',
    'btn_return': '/html/body/div[2]/header/nav/div/div[2]/ul/li[4]/a'
}

# Aqui estão as listas nas quais são armazenado os nome das vagas, local e descrição
nome_vagas = []
localidade = []
descricao = []

# Data que o robo roda;
data_atual = dt.datetime.now()
data_formatada = data_atual.strftime('%d/%m/%Y')
