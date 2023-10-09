# @property + @setter - getter e setter no modo pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# atributos que começar com um ou doi underlines
# não devem ser usados fora da classe.

class Caneta:
    def __init__(self, cor):
        self.cor = cor
        self._cor_tampa = None
    
    @property
    def cor(self):
        print('ESTOU NO GETTER')
        return self.cor
    
    @cor.setter
    def cor(self, valor):
        print('estou no setter')
        self.cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor

caneta = Caneta('azul')
caneta.cor = 'Rosa'
print(caneta.cor)


