import requests
from bs4 import BeautifulSoup


class Site:

    # Construtor da classe Site que recebe a url do site
    def __init__(self, site):
        self.site = site
        self.news = []

    # Metodo que faz a requisicao da pagina e retorna o conteudo da pagina
    def update_news(self):
        if self.site.lower() == 'globo':
            url = 'https://www.globo.com/'
            browsers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
            }
            page = requests.get(url, headers=browsers)
            soup = BeautifulSoup(page.content, 'html.parser')

            noticias = soup.find_all('a')
            tg_class1 = 'post__title'
            tg_class2 = 'post-multicontent__link--title__text'

            news_dict_globo = {}

            # Itera sobre as noticias e adiciona no dicionario as noticias que possuem a classe 'post__title' ou 'post-multicontent__link--title__text' no h2 da noticia
            for noticia in noticias:
                if noticia.h2 != None:
                    if tg_class1 in noticia.h2.get('class') or tg_class2 in noticia.h2.get('class'):
                        # Adiciona a noticia no dicionario com a chave sendo o titulo da noticia e o valor sendo o link da noticia
                        news_dict_globo[noticia.h2.text] = noticia.get('href')

            self.news = news_dict_globo

        if self.site.lower() == 'cnn':
            url = 'https://www.cnnbrasil.com.br/'
            browsers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
            }
            page = requests.get(url, headers=browsers)
            soup = BeautifulSoup(page.content, 'html.parser')

            noticias = soup.find_all('a')
            tg_class1 = 'block__news__title'

            news_dict_cnn = {}

            for noticia in noticias:
                if noticia.h3 != None:
                    if tg_class1 in noticia.h3.get('class'):
                        news_dict_cnn[noticia.h3.text] = noticia.get('href')

            self.news = news_dict_cnn


self = Site('cnn')
self.update_news()
print(self.news)
