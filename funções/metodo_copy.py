# metodos uteis dos dicionarios em python
# len - quantas chaves
# keys - iteravel com as chaves
# values - iteravel com os valores
# itens - iteravel com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma copia rasa (shallow copy)
# get - obtem uma chave
# pop - apaga um item com a chave especifica (del)
# popitem - apaga o ultimo item adicionado
# update - atualiza um dicionario com outro
import copy

d1 = {
    'c1': 1,
    'c2': 2,
}

d2 = copy.deepcopy(d1)

d2['c1'] = 1000
d2['11'][1] = 999999

print(d1)
print(d2)

