def soma(*args):
    total = 0
    for numero in args:
        print('Total', total, numero)
        total = total + numero
        print('Total', total)
    print(total)


#soma(1, 2, 3, 4, 5, 6)

# desempacotamento

#soma_1_2_3 = soma(1, 2, 3)

#soma_4_5_6 = soma(4, 5, 6)

numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9
outra_soma = soma(*numeros)
#print(outra_soma)

#print(sum(numeros))