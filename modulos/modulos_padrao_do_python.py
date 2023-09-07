# modulos pãdrão do python (import, from, as e *)
# inteiro  - import nome_modulo
# vantagens: você tem o namespace do modulo
# desvantagens: nomes grandes
import sys

platform = 'a minha'
print(sys.platform)
print(platform)

# partes - from nome_modulo import objeto1, objeto2
# vantagens: nomes pequenos
# desvantagens: sem o namespace do modulo
from sys import exit, platform

print(platform)

# alias 1 - import nome_modulo as apelido
import sys as s

sys = 'alguma coisa'
print(s.platform)
print(sys)

# alias 2 - from nome_modulo import objeto as apelido
from sys import exit as ex
from sys import platform as pf
print(pf)

# vantagens: você pode reservar nomes para seu codigo
# desvantegens: pode ficar fora do padrão da linguagem

# má pratica - from nome_modulo import *
# vantagens: importa tudo de um modulo
# desvantagens: importa tudo de um modulo

from sys import *

print(platform)
exit()
