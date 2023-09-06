numero_str = input('vou dobrar o numero que voce digitar: ')

try:
    numero_float = float(numero_str)
    print('float:', numero_float)
    print(f'o dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('isso não é um numero')