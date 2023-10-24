# os.path trabalha com caminhos em windows, linux e mac
# os.path é um módulo  que fornece funções para trabalhar com caminhos de
# arquivos em windows, mac ou linux sem precisar se preocupar com as diferenças
# entr esses sistemas.
# exemplos de os.path:
# os.path.join: junta strings em um unico caminho, desse modo, 
# os.path.join('pasta1', 'pasta2', 'arquivo.txt') retornaria
# 'pasta1'/pasta2/arquivo.txt' no linux ou mac, e
# 'pasta1'\pasta2\arquivo.txt' no windows.
# os.path.split: divide um caminho em tupla(diretorio, arquivo).
# por exemplo, os.path.split('/home/user/arquivo.txt')
# retornaria ('/home/user', 'arquivo.txt').
# os.path.exists: verifica se um caminho especificado existe.
# os.path só trabalha com caminhs de arquivos e não faz nenhuma
# operação de entrada/saida (I/O) com arquivos em si.
import os

caminho = os.path.join('desktop', 'curso', 'arquivo.txt')
print(caminho)
diretorio, arquivo = os.path.split(caminho)
nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
print(nome_arquivo, extensao_arquivo)
print(os.path.exists('/users/luizotavio/desktop/curso-python-rep'))
print(os.path.abspath('.'))
print(os.path.basename(caminho))
print(os.path.basename(diretorio))
print(os.path.dirname(caminho))