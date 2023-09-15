# atributos de classe
class Pessoa:
    ano_atual = 2022
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.ano_atual = 100
    
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
p1 = Pessoa('joão', 35)
p2 = Pessoa('helena', 12)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())

