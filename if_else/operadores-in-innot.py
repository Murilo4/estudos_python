nome = 'murilo'
print(nome[2])
print(nome[-4])
print('ilo' in nome)
print('zero' in nome)

print('ilo' not in nome)
print('zero' not in nome)

nome2 = input('digite seu nome: ')
encontrar = input('digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:
    print(f'{encontrar} não esta em {nome}')
    