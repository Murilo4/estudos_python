def multiplicador(*args):
    multiplicar = 1
    for numero in args:
        multiplicar *= numero
        
    return multiplicar
    
multipli = multiplicador(10, 2, 43, 5, 4)
print(multipli)


def im_par(a):
    if a % 2 == 0:
        print(f'o numero {a} é par')
    else:
        print(f'o numero {a} é impar')

valor = input('entre com um valor: ')
valor_int = int(valor)

im_par(valor_int)



