# context manager com classes
# você pode implementar seus próprios protocolos
# apenas implementando os dunder methods que o 
# python vai usar.
# isso é chamado de Duck typing. Um conceito
# relacionado com tipagem dinâmica onde o python não
# está interessado no tipo, mas se alguns métodos existem
# no seu objeto para que ele funcione de forma adequada.
# duck typing:
# quando vejo um passaro que caminha como um pato, nada como
# um pato e grasna como um pato, eu chamo aquele passaro de pato.
# para criar um context manager, os métodos __enter__ e __exit__
# devem ser implementados.
# o método __exit__ receberá a classe de exceção, a exceção e o
# trackback. Se ele retornar True, exceção no with será
# suprimidas.

class MyOpen:
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self.arquivo = None

    def __enter__(self):
        print('ABRINDO ARQUIVO')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._arquivo
    
    def __exit__(self, class_exception, exception_, trackback_):
        print('FECHANDO ARQUIVO')
        self._arquivo.close()

with MyOpen('context_manager_txt', 'w') as arquivo:
    arquivo.write('linha1\n')
    arquivo.write('linha2\n')
    arquivo.write('linha3\n')
    print('WITH', arquivo)