import copy

produtos = [
    {'nome': 'produto 5', 'preco': 10.00},
    {'nome': 'produto 1', 'preco': 22.32},
    {'nome': 'produto 3', 'preco': 10.11},
    {'nome': 'produto 2', 'preco': 105.87},
    {'nome': 'produto 4', 'preco': 69.90},
]
novos_preco = [
    {**p, 'preco': round(p['preco']* 1.1, 2)}
    for p in copy.deepcopy(produtos)
]

print(*novos_preco, sep='\n')
print()

produtos_ordenados_por_nome = sorted(produtos,
    key=lambda p: p['nome'],
    reverse=True
)
print(*produtos_ordenados_por_nome, sep='\n')
print()


produtos_ordenados_por_preco = sorted(produtos,
    key=lambda p: p['preco']
)
print(*produtos_ordenados_por_preco, sep='\n')

