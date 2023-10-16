# namedtuples - tuplas imutaveis com nome para valores
# usamos namedtuples para criar classes de objetos que são apenas um
# agrupamento de atributos, como classes normais sem métodos, ou registros de
# bases de dados, etc.
# as namedtuples são imutaveis assim como as tuplas

from typing import NamedTuple

class Carta(NamedTuple):
    valor: str = 'VALOR'
    naipe: str = 'NAIPE'

# Carta = namedtuple(
#     'Carta', ['valor', 'naipe'],
#       defaults=['VALOR, 'NAIPE'])

as_espadas = Carta('A')
# print(as_espadas)
# print(as_espadas[0])
# print(as_espadas.valor)
# print(as_espadas[1])
# print(as_espadas.naipe)

# print()

