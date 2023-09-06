lista_a = ['luiz', 'maria', 1, True, 1.2]
lista_b = lista_a.copy() # aponta para o mesmo valor na memoria(mutavel)

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)