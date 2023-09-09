# controlando a quantidade de argumentos posisionais e nomeados em funções
# *args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)
# positional-only parameters (/) - tudo antes da barra deve
# ser apenas posicional
# PEP 570 - python positional-oly parameters
# keyword-only arguments (*) - * sozinho NÃO SUGA valores
# pep 3102 - keyword-only arguments

def soma(a, b, /, *, c, **kwargs):
    print(kwargs)
    print(a + b + c)

soma(1, 2, c=3, nome='teste')