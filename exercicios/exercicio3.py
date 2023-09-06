# """
# Faça um programa que peça ao usuário para digitar um número inteiro,
# informe se este número é par ou ímpar. Caso o usuário não digite um número
# inteiro, informe que não é um número inteiro.
# """
num = input('insira um valor inteiro: ')

if num.isdigit:
    is_impar = num % 2 == 0
    print(f'o numero {is_impar} é par')

else:
    print(f'o numero {num} é impar')
    print(f'desculpe, este valor {num} não é um valor valido')


# """
# Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
# descrito, exiba a saudação apropriada. Ex. 
# Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
# """
num = input('insira um valor inteiro: ')
try:
    num_int = int(num)
    if num_int % 2 == 0:
        print(f'o numero {num} é par')
    else:
        print(f'o numero {num} é impar')
except:
    print(f'desculpe, este valor {num} não é um valor valido')


# """
# Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
# menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
# "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
# """
nome = input('insira o seu primeiro nome: ')

if len(nome) <= 4:
    print('seu nome é curto')
elif len(nome) >= 5 and len(nome) <= 6:
    print('seu nome é normal')
elif len(nome) > 6:
    print('seu nome é grande')