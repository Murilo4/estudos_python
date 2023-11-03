# + web scraping com python usando requests e bs4 BeautifulSoup
# - web Scraping é o ato de "raspar a web" buscando informações de forma
# automatizada, com determinada linguagem de programação, para uso posterior.
# - O módulo requests consegue carregar dados da internet para dentro do seu
# código. Já o bs4.BeautiflSoup é responsável por interpretar os dados HTML
# em formato de objetos python para facilitar a vida do desenvolvedor.
# - DOC: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/
#  + instalação
# - pip install requests types-requests bs4
import requests
from bs4 import BeautifulSoup
import re

url = 'http://127.0.0.1:3333/'
response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser')
# if parsed_html.title is not None:
#     print(parsed_html.title.text)

top_jobs_heading = parsed_html.select_one('#intro > div > div > article > h2')

if top_jobs_heading is not None:
    article = top_jobs_heading.parent

    if article is not None:
        for p in article.select('p'):
            print(re.sub(r'\s{1,}', '', p.text).strip())

    