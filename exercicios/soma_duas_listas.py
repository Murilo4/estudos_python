def somar(lista1, lista2):
    intervalo = min(len(l1), len(l2))
    return [
        (lista1[i] + lista2[i]) for i in range(intervalo)
    ]

l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [1, 2, 3, 4]

nova_lista = somar(l1, l2)
print(l1, l2)
print(nova_lista)

lista_soma = [x + y for x , y in zip(l1, l2)]
print(lista_soma)