# funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# toda função recursiva deve ter:
# um problema que possa ser dividido em partes menores
# um caso base que para a recursão
# fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120

def recursiva(inicio=0, fim=4):
    print(inicio, fim)

    #caso base
    if inicio >= fim:
        return fim
    
    # caso recursivo
    # contar ate chegar ao final
    inicio += 1
    return recursiva(inicio, fim)

print(recursiva())