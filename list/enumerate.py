"""
enumerate -  enumera iteraveis (indices)
"""
# [(0, 'maria'),(1, 'helena'),(2, 'luiz'),(3, 'joão')]
lista = ['maria', 'helena', 'luiz']
lista.append('joão')

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])

for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)

for tupla_enumerada in enumerate(lista):
    print('For da tupla: ')
    for valor in tupla_enumerada:
        print(f'\t{valor}')