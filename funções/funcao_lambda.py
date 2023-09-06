"""
    função lambda em python
    A função lambda é uma função como qualquer outra em python
    porém, são funções anônimas que contem apenas uma linha
    ou seja, tudo deve er contido dentro de uma unica expressão
"""

lista = [
    {'nome': 'luiz', 'sobrenome': 'miranda'},
    {'nome': 'maria', 'sobrenome': 'oliveira'},
    {'nome': 'daniel', 'sobrenome': 'silva'},
    {'nome': 'eduardo', 'sobrenome': 'moreira'},
    {'nome': 'aline', 'sobrenome': 'souza'},
]

def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)



def executa(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y 

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

duplica = executa(
    lambda m: lambda n: n * m,
    2
)
print(duplica(2))

print(
    executa(
        lambda x, y: x + y,
        2, 3
    )
)

print(
    executa(
        lambda *args: sum(args),
        1, 2, 3, 4, 5, 6, 7
    )
)
