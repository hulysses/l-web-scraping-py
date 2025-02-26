import requests
import pandas as pd
from bs4 import BeautifulSoup

def scraping_uf(uf: str):
    uf_url = f'https://www.ibge.gov.br/cidades-e-estados/{uf}.html'

    # Configura a requisicao como sendo de um navegador e nao de um script
    browsers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0"}
    page = requests.get(uf_url, headers=browsers)

    if page.status_code == 200:
        soup = BeautifulSoup(page.content, 'html.parser')
        indicadores = soup.find_all('div', class_='indicador')

        # Cria um dicionario, sendo a chave o nome do indicador e o valor o valor do indicador
        uf_dict = {
            dado.select('.ind-label')[0].text: dado.select('.ind-value')[0].text
            for dado in indicadores
        }

        # Remove o texto que nao faz parte do valor do indicador e retorna o dicionario com os valores corretos
        for indicador in uf_dict:
            if ']' in uf_dict[indicador]:
                uf_dict[indicador] = uf_dict[indicador].split(']')[0][:-8]

        # Cria um DataFrame com os valores do dicionario
        df = pd.DataFrame(uf_dict.values(), index=uf_dict.keys())

        return df

print(scraping_uf('sp'))
