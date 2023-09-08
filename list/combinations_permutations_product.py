# combinations, permutations e product - itertools
# combinação - ordem não importa - iteravel + tamanho do grupo
# permutação - ordem importa
# produto - ordem importa e repete valores unicos
from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

pessoas = [
    'Jõao', 'joana', 'luiz', 'leticia'
]
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
]

print_iter(combinations(pessoas, 2))
print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))

