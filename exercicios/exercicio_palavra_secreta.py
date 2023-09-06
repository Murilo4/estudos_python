palavra_secreta = 'perfume'
letra_acertada = ''

while letra_acertada != palavra_secreta:
    letra = input('informe uma letra:')

palavra_digitada = '******'

while palavra_digitada != palavra_secreta:
    letra = input('informe uma letra:')

    if len(letra) > 1:
        print('digite apenas uma letra! ')
        continue

    if letra in palavra_secreta:

        letra_acertada += letra
    palavra_digitada = ''
    for caracter in palavra_secreta:
        if caracter in letra_acertada:
            palavra_digitada += caracter
        else:
            palavra_digitada += '*'
    print(palavra_digitada)
    if palavra_digitada == palavra_secreta:
        print(f'meus parabens! você conseguiu, a palavra secreta é {palavra_secreta}')
        break   