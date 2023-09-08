# reduce - faz a redução de um iteravel em um valor
from functools import reduce


produtos = [
    {'nome': 'produto 5', 'preco': 10.00},
    {'nome': 'produto 1', 'preco': 22.32},
    {'nome': 'produto 3', 'preco': 10.11},
    {'nome': 'produto 2', 'preco': 105.87},
    {'nome': 'produto 4', 'preco': 69.90},
]

def funcao_do_reduce(acumulador, produto):
    print('acumulador', acumulador)
    print('produto', produto)
    print()
    return acumulador + produto['preco']


total = reduce(
    lambda ac, p: ac + p['preco'],
    funcao_do_reduce,
    produtos,
    0
)

print('total é', total)