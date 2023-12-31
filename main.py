from requests import get
from bs4 import BeautifulSoup as Bs
import yaml
import re

# fazendo raspagem da página
resposta = get("https://www.w3schools.io/file/yaml-sample-example/")

# mapeando o conteúdo html
tags = Bs(resposta.text, "html.parser")

# Procurando o arquivo YAML no site
yamlExample = tags.find_all("code", attrs={"language-Yaml"})
print(f"Confirmando: \n \n {yamlExample} \n \n")

# acessando os comentários
comentarios = []
for code in yamlExample:
    comentarios.extend(re.findall(r'#\s.*', code.text))

print(f"lista com cada comentario como um elemento: \n \n {comentarios}")

dicionarioComentario = {}

for posicao, comentario in enumerate(comentarios, 1):
    dicionarioComentario[posicao] = comentario

# criando um arquivo e preenchendo seu conteúdo com o dicionário
with open('Comentarios.yaml', 'w') as file:
    yaml.dump(dicionarioComentario, file)