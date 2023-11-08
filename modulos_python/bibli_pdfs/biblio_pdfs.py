# PyPDF2 - Para manipular arquivos PDF
# PyPDF é um biblioteca de manipulação de arquivos PDF feita em python puro, 
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipula metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2
# link: https://pypdf2.readthedocs.io/en/3.0.0/

from pathlib import Path

from PyPDF2 import PdfReader, PdfWriter, PdfMerger

PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'

RELATORIO_BACEN = PASTA_ORIGINAIS / 'R20230210.pdf'

PASTA_NOVA.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO_BACEN)

# print(len(reader.pages))

page0 = reader.pages[0]
imagem0 = page0.images[0]

writer = PdfWriter()

with open(PASTA_NOVA / 'NOVO_PDF.pdf', 'wb') as fp:
    for page in reader.pages:
        writer.add_page(page)
    writer.write(fp)


for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    with open(PASTA_NOVA / f'page{i}.pdf', 'wb') as arquivo:
        writer.add_page(page)
        writer.write(arquivo)


files = [
    PASTA_NOVA / 'page1.pdf',
    PASTA_NOVA / 'page0.pdf',
]

merger = PdfMerger()
for file in files:
    merger.append(file)

merger.write(PASTA_NOVA / 'MERGED.pdf')
merger.close()


