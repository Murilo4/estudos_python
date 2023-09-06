import random

cpf = '746.824.890-70'
gerar_cpf = ''
for i in range(9):
    gerar_cpf += str(random.randint(0,9))

cpf_formatado = ''
cont = 10
cpf_multiplicado = 0
    
for num in cpf:
    if num == '.':
        continue
    elif num == '-':
        break
    else:
        cpf_formatado += num 
print(gerar_cpf)

for valor_1 in gerar_cpf:
    cpf_multiplicado += int(valor_1) * cont
    cont -= 1    
    
digito_1 = (cpf_multiplicado * 10) % 11

digito_1 = digito_1 if digito_1 <= 9 else  0

cont_2 = 11
cpf_multiplicado_2 = 0
cpf_formatado_2 = ''

cpf_formatado_2 = gerar_cpf + str(digito_1)

for valor_2 in cpf_formatado_2:
    cpf_multiplicado_2 += int(valor_2) * cont_2
    cont_2 -= 1

digito_2 = (cpf_multiplicado_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_formatado_2 = cpf_formatado_2 + str(digito_2)

print(f'o cpf gerado é {cpf_formatado_2}')