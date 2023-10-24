# os.listdir para navegar em caminhos
# /users/luizotavio/desktop/EXEMPLO
import os

caminho = os.path.join('/users', 'luizotavio', 'desktop', 'EXEMPLO')
for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)

    if not os.path.isdir(caminho_completo_pasta):
        continue

    for imagem in os.listdir(caminho_completo_pasta):
        print('  ', imagem)
        