class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('luiz', 'otavio')

p2 = Pessoa('maria', 'joana')

print(p1.nome)
print(p1.sobrenome)
print(p2.nome)
print(p2.sobrenome)
