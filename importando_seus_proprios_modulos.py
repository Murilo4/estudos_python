# entendendo os seus proprios modulos python
# o primeiro modulo executado chama-se __main__
# você pode importar outro modulo inteiro ou parte de um modulo
# o python conhece a pasta onde o __main__ está e as pastas
# abaixo dele
# ele não reconhece pastas e modulos acima do __main__ por padrão
# o python conhece todos os modulos e pacotes presentes
# nos caminhos de sys.path

import modulos_padrao_do_python

print('este modulo se chama', __name__)

from while_for.for_in_com_lists import lista


