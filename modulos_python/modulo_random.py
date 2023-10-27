# random tem geradores de números pseudoaleatórios
# obs.: números pseudoaleatórios significa que os números
# parecem ser aleatórios, mas na verdade não são. Portanto, 
# este módulo não deve ser usado para segurança ou uso criptográfico.
# O motivo disso é que quando temos uma mesma entrada e um mesmo algorítimo, 
# a saída pode ser previsível.
# doc: https://docs.python.org/pt-br/3/libraby/random.html
import random
# Funções:
# seed
#   -> Inicializa o gerador de random (por iso "números pseudoaleatórios")
# random.randrange(inicio, fim, passo)
#   -> gera um numero inteiro aleatorio dentro de um intervalo especifico
r_range = random.randrange(10, 20, 2)
print(r_range)
# random.randint(inicio, fim)
#   -> gera um numero inteiro aleatorio dentro de um intervalo "sem passo"
r_int = random.randint(10, 20)
print(r_int)
# random.uniform(inicio, fim)
#   -> gera um numero flutuante aleatorio dentro de um intervalo "sem passo"
r_uniform = random.uniform(10, 20)
print(r_uniform)
# random.shuffle(sequenciamutavel) -> embaralha a lista original
nomes = ['luiz', 'maria', 'helena', 'joana']
random.shuffle(nomes)
# print(nomes)

# random.sample(Iteravel, k=N)
#   -> Escolhe elementos do iteravel e retorna outro iteravel (não repete)
novos_nomes = random.sample(nomes, k=2)
print(nomes)
print(novos_nomes)

# random.choices(iteravel, k=N)
#   -> Escolhe elementos do iteravel e retorna outro iteravel (repete)
novos_nomes = random.choices(nomes, k=3)
# random.choice(Iteravel) -> Escolhe um elemento do iteravel
print(random.choice(nomes))