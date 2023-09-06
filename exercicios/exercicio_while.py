nome = 'murilo'
new_nome = ''
cont = 0
while cont < len(nome):
    letra = nome[cont]
    new_nome += '*' + letra
    cont += 1

print(new_nome + '*')