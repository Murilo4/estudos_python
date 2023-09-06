"""
higher order functions
funções de primeira classe
"""

def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)

print(
    executa(saudacao, 'bom dia', 'luiz')
)
print(
    executa(saudacao, 'boa noite', 'maria')
)