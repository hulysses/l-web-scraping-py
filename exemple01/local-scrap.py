from bs4 import BeautifulSoup

# Abre o arquivo index.html em modo de leitura
with open('index.html', 'r') as file:
    # Lê o conteúdo do arquivo
    conteudo = file.read()

# Cria um objeto BeautifulSoup com o conteúdo do arquivo
ex = BeautifulSoup(conteudo, 'lxml')
print(ex)

# Procura todas as tags <p> no conteúdo
print(ex.find_all('p'))

# Procura a tag com a classe 'p1' no conteúdo
print(ex.find(class_='p1'))

tags = ex.find_all('p')

# Exibe o texto de cada tag <p> encontrada
for tag in tags:
    print(tag.text)
