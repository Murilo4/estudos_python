while True:
    numero_1 = input('entre com um valor: ') # entrada de dados
    numero_2 = input('entre com outro valor: ')
    operador = input('insira o operador: +-*/: ')

    numeros_validos = None
    numero1_float = 0
    numero2_float = 0
    try:
        numero1_float = float(numero_1) # validação dos valores informados
        numero2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None # caso os valores informados não sejam validos

        if numeros_validos is None:
            print('um ou ambos os valores são invalidos')
            continue

    operadores_permitidos = '+-*/'

    if operador not in operadores_permitidos: #verificação se o operador é valido
        print('operador informado é invalido')
        continue

    if len(operador) > 1: # verificação se foi digitado apenas 1 operador
        print('digite apenas um operador')
        continue
    
    realizar = 'realizando sua operação' 
    if operador == '+': # conta de soma
        print(realizar)
        print(f'{numero1_float}+{numero2_float}=', numero1_float + numero2_float)

    elif operador == '-': # conta de subtração
        print(realizar)
        print(f'{numero1_float} - {numero2_float}=', numero1_float - numero2_float)

    elif operador == '/': # conta de divisão
        if numero2_float == 0:
            print('não é possivel fazer um divisão por zero')
        else:
            print(realizar)
            print(f'{numero1_float} / {numero2_float}=', numero1_float / numero2_float)

    elif operador == '*': # conta de multiplicação
        print(realizar)
        print(f'{numero1_float}*{numero2_float}=', numero1_float * numero2_float)

    sair = input('deseja sair? [s]im: ').lower().startswith('s') # fechar aplicação
    if sair:
        break