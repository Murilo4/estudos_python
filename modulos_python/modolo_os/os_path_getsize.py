# os.path.getsize e os.stat para dados dos arquivos
import math
import os
from itertools import count

def formata_tamanho(tamanho_em_bytes: int, base: int = 1000) -> str:
    if tamanho_em_bytes <= 0:
        return "0B"
    
    abreviacao_tamanhos = "B", "KB", "MB", "GB", "TB", "PB"

    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base))

    potencia = base ** indice_abreviacao_tamanhos

    tamanho_final = round(tamanho_em_bytes / potencia, 2)
    abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamanhos]
    return f'{tamanho_final} {abreviacao_tamanho}'

print(formata_tamanho(1000))

caminho = os.path.join('/users', 'luizotavio', 'desktop', 'exemplo')
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, 'pasta atual', root)

    for dir_ in files:
        print('  ', the_counter, 'dir', dir_)

    for file_ in files:
        caminho_completo_arquivo = os.path.join(root, file_)
        stats = os.stat(caminho_completo_arquivo)
        tamanho = stats.st_size

        print('  ', the_counter, 'FILE', file_, formata_tamanho(tamanho))