# funções decoradoras
# decorar = adicionar / remover / restringir / alterar
# funções decoradoras são funções que decoram outras funções
# usar as funções decoradoras em outras funções
# decoradores são "Syntax sugar" (açúcar sintátito)


def criar_funcao(func):
    def interna(*args, **kwargs):
        print('vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print('ok, agora você foi decorado')
        return resultado
    return interna

@criar_funcao
def inverte_string(string):
    return string[::-1]

def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')
    


invertida = inverte_string('123')
print(invertida)