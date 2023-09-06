nome = input('digite o seu nome: ')
idade = input('digite a sua idade: ')

if nome and idade:
    print(f'seu nome é {nome}')
    print(f'seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print(f'seu nome tem espaços')
    else:
        print(f'seu nome não tem espaços')
    print(f'o seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
else:
    print('desculpe, você deixou campos vazios')