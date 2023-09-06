"""
introdução as funções (def) em python
funções são trechos de codigo usados para
replicar determinada ação ao longo do seu codigo.
elas podem receber valores para parametros(argumentos)
e retornar um valor especifico
por padrão, funções python retornam none (nada)
"""

def imprimir(a, b, c):
    print(a, b, c)

imprimir(1, 2 , 3)
imprimir(4, 5, 6)

def saudacao(nome='sem nome'):
    print(f'olá, {nome}')

saudacao('luiz otavio')
saudacao('maria')
saudacao('helena')
saudacao()