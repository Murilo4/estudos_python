lista_compras = []
import os

while True:

    cont = 0
    valor_int = 0
    opcao = input('\n o que deseja fazer? 1)adicionar itens na lista \n 2) remover itens da lista \n 3) listar valores da lista \n 4)sair \n :' )
    opcoes_permitidas = '1234'

    
    if opcao == "1":
        quantidade = input('quantos valores vão ser adicionados? ')
        try:
            valor_int = int(quantidade)
            while cont < valor_int:
                adicionar_valor = input('entre com o valor a ser adicionado: ')
                lista_compras.append(adicionar_valor)
                cont += 1

            os.system('cls')
            print(lista_compras)
            continue
        except:
            print('entre com um valor numerico!')
            continue

    elif opcao == '2':
        for indice, lista in enumerate(lista_compras):
            print(indice, lista)
        indice_valor_Deletado = input('qual o indice do valor a ser deletado?? ')

        try:
            valor_deletado_int = int(indice_valor_Deletado)

            if valor_deletado_int >= len(lista_compras):
                os.system('cls')
                print('o indice em questão não existe na lista \n')
                continue

            else:
                del lista_compras[valor_deletado_int]
                os.system('cls')
                print(f'\na lista sem o valor deletado ficou: {lista_compras} \n')
                continue

        except:
            os.system('cls')
            print('valor do indice deve ser numerico!')
        

    elif opcao == '3':
        os.system('cls')
        for indice, lista in enumerate(lista_compras):
            print(indice, lista)

    elif opcao == '4':
        os.system('cls')
        print('a lista de compras vai ser encerrada ')
        break

    else:
        print('opção não permitida')
        continue