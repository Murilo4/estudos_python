# sys.argv - Executando arquivos com argumentos no sistema
import sys
argumentos = sys.argv
qtd_argumentos = len(argumentos)

if qtd_argumentos <= 1:
    print('você não passou argumentos')
else:
    try:
        print(f'você passou os argumentos {argumentos[1:]}')
        print(f'você passou os argumentos {argumentos[1]}')
        print(f'você passou os argumentos {argumentos[2]}')
    except IndexError:
        print('Faltan argumentos')



