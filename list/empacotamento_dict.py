# empacotamento e desempacotamento de dicionarios
a, b = 1, 2
a, b = b, a
print(a, b)

pessoa = {
    'nome': 'aline',
    'sobrenome': 'souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoas_completa = {**pessoa, **dados_pessoa}

#args e kwargs
#args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs):
    print('não nomeados', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

mostro_argumentos_nomeados(nome='joana', qlq=123)


configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3, 
    'arg4': 4,
}