# Criando Exceptions em Python Orientado a Objetos
# para criar uma exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de exception.
# Criando exceções (comum colocar Error ao final)
# levantando (raise) / lançando (throw) exceções
# relançando exceções
# adicionando notas em exceções (3.11.0)
class MeuError(Exception):
    ...


class OutroError(Exception):
    ...


def levantar():
    exception_ = MeuError('a', 'b', 'c')
    exception_.add_note('você errou isso')
    raise exception_


try:
    levantar()
except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = OutroError('vou lançar de novo')
    exception_.__notes__ = error.__notes__.copy()
    exception_.add_note('mais uma nota')
    raise exception_ from error