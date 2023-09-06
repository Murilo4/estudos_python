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

p1 = {
    'nome': 'luiz',
    'sobrenome': 'miranda',
}
print(p1['nome'])
print(p1.get('nome', 'não existe'))

nome = p1.pop('nome')
print(nome)
print(p1)
ultima_chave = p1.popitem()
print(ultima_chave)
print(p1)
p1.update({
    'nome': 'novo valor',
    'idade': 30,
})
p1.update(nome='novo valor', idade=30)
tupla = (('nome', 'novo valor'), ('idade, 30'))
p1.update(tupla)
print(p1)
