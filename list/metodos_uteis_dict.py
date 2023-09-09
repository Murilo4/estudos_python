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

pessoa = {
    'nome': 'luiz otavio',
    'sobrenome': 'miranda',
    'idade': 900,
}

pessoa.setdefault('idade', 0)
print(pessoa['idade'])
print(len(pessoa))
print(list(pessoa.keys()))
print(list(pessoa.values()))
print(list(pessoa.items()))