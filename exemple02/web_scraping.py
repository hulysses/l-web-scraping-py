import requests
from bs4 import BeautifulSoup

# Faz a requisicao HTTP para a URL informada e armazena o conteudo da pagina em uma variavel
globo_url = 'https://www.globo.com/'
page = requests.get(globo_url)

# Verifica se a requisicao foi bem sucedida
if page.status_code == 200:
    response = page.text

    # Cria um objeto BeautifulSoup com o conteudo da pagina
    soup = BeautifulSoup(response, 'html.parser')
    news_title = soup.find_all('h2', {'models': 'post__title'})

    # Exibe o titulo de cada noticia encontrada
    for title in news_title:
        print(title.text)
else:
    print('Erro ao acessar a pagina')

