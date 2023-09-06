# manipulando chaves e valores em dicionarios
pessoa = {}

pessoa['nome'] = 'luiz otavio'
lista = []

chave = 'nome'

pessoa[chave] = 'luiz otavio'
pessoa['sobrenome'] = 'miranda'

print(pessoa[chave])

pessoa[chave] = 'maria'

del pessoa['sobrenome']

print(pessoa)
print(pessoa['nome'])
print(pessoa.get('sobrenome', 'não existe'))


