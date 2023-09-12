# escopo da classe e de metodos da classe
class Aninal:
    # nome  = 'leão'

    def __init__(self, nome):
        self.nome = nome

        variavel = 'valor'
        print(variavel)
        
    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}'
    
    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)
    

leao = Aninal(nome='leão')
print(leao.nome)
print(leao.executar('maçã'))

