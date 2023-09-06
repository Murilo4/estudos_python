def multiplicar(multiplo):
    def valores(num):
        return f'{num} * {multiplo} =', num * multiplo
    return valores
    

valor_dobro = multiplicar(2)
valor_triplo = multiplicar(3)
valor_quadrupo = multiplicar(4)

for num in [4, 5, 7]:
    print(valor_dobro(num))
    print(valor_triplo(num))
    print(valor_quadrupo(num))

