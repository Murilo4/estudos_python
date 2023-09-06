import statistics

quantidade_elementos_array = 0
porcentagem = 0

array = [5, 4, 8, 8, 7, 6, 6, 8, 8, 12]

try:
    media = statistics.mean(array)
    mediana = statistics.median(array)
    moda = statistics.mode(array)

    print(f'a media é de =', media)
    print(f'a mediana é de =', mediana)
    print(f'a moda é de =', moda)
except:
    print('algo de errado não certo')

for numero in array:
    quantidade_elementos_array += 1

def define_porcent(porcentagem, quantidade_elementos, valores):
    posicao_elemento_array = (quantidade_elementos * porcentagem) // 100
    valor_minimo = valores[posicao_elemento_array - 1]
    return valor_minimo


print(f'o valor minimo é de =',define_porcent(30, quantidade_elementos_array, array))
