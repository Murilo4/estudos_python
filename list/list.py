"""
listas em python
tipo list - mutavel
suporta varios valores de qualquer tipo
conhecimentos reutilizaveis - indices e fatiamento
metodos uteis: append, insert, pop, del, clear, extend, +
"""
string = 'ABCDE'
print(bool([])) # falsy
lista = [123, True, 'murilo', 1.2, []]
print(lista, type(lista))

lista[-3] = 'maria'
print(lista)
print(lista[2], type(lista[2]))
