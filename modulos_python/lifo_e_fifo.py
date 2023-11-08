# Deque - Trabalhando com LIFO e FIFO
# deque - Double-ended queue

# Lifo e fifo
# pilha e fila

# LIFO (Last In first Out)
# Pilha(stack)
# Significa que o último item a entrar será o primeiro a sair (list)
# Artigo:
# https://www.otaviomiranda.com.br/2020/pilhas-em-python-com-listas
# Vídeo:
# https://youtu.be/svWVHEihyNI
# para tirar itens do final: o(1) tempo constante
# para tirar itens do início: o(n) tempo linear

from collections import deque

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# legal (LIFO com lista)

lista.append(10)

lista.append(11)

ultimo_removido = lista.pop()

print('Último:', ultimo_removido)
print('Lista:', lista)

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Ruim (FIFO com lista)

lista.insert(0, 10)

lista.insert(0, 11)

primeiro_removido = lista.pop(0)

print('Primeiro: ', primeiro_removido)
print('lista:', lista)

# legal (FIFO com deque)

fila_correta: deque[int] = deque()
fila_correta.append(3)
fila_correta.append(4)
fila_correta.append(5)
fila_correta.appendleft(0)
fila_correta.appendleft(1)
fila_correta.appendleft(2)
print(fila_correta)
fila_correta.pop()
fila_correta.popleft()
print(fila_correta)

