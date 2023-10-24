# os.walk
# os.walk é uma função que permite percorrer uma estrutura de diretorios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual(root), uma lista de subdiretorios (dirs)
# e uma lista dos arquivos diretorio atual(files)
import os
from itertools import count 

caminho = os.path.join('/users', 'luizotavio', 'desktop', 'exemplo')
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, 'pasta atual', root)

    for dir_ in dirs:
        print('  ', the_counter, 'dir', dir_)

    for file_ in files:
        caminho_completo_arquivo = os.path.join(root, file_)
        print('  ', the_counter, 'file', file_)
