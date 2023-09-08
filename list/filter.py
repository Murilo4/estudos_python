# filter

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

produtos = [
    {'nome': 'produto 5', 'preco': 10.00},
    {'nome': 'produto 1', 'preco': 22.32},
    {'nome': 'produto 3', 'preco': 10.11},
    {'nome': 'produto 2', 'preco': 105.87},
    {'nome': 'produto 4', 'preco': 69.90},
]

def filtrar_preco(produto):
    return produto['preco'] >= 100,


novos_produtos = filter(
    lambda p: p['preco'] > 100,
    filtrar_preco,
    produtos
)

print_iter(produtos)
print_iter(novos_produtos)