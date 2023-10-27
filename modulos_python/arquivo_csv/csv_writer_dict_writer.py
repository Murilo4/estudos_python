import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'csvwriter.csv'

lista_clientes = [
    {'Nome':'Luiz otavio', 'Endereço': 'Av 1, 22'},
    {'Nome':'João Silva', 'Endereço': 'R. 2, "1"'},
    {'Nome':'Maria sol', 'Endereço': 'Av B, 3A'},
]

with open(CAMINHO_CSV, 'w') as arquivo:
    nome_columas = lista_clientes[0].keys()
    escritor = csv.DictWriter(
        arquivo, 
        fieldnames=nome_columas
    )
    escritor.writeheader()

    for cliente in lista_clientes:
        print(cliente)

# with open(CAMINHO_CSV, 'w') as arquivo:
#     nome_columas = lista_clientes[0].keys()
#     nome_columas = ['Nome', 'Endereço']
#     escritor = csv.writer(arquivo)

#     escritor.writerow(nome_columas)

#     for cliente in lista_clientes:
#         escritor.writerow(cliente)