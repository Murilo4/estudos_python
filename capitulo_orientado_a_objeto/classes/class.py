# class - classes são moldes para criar novos objetos
# as classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# por convenção, usamos PascalCase para nomes de 
# classes.
# string = 'luiz' #str
# print(string.upper())
# print(isinstance(string, str))
class Pessoa:
    ...

p1 = Pessoa()
p1.nome = 'luiz'
p1.sobrenome = 'otavio'
print(p1.nome)
print(p1.sobrenome)

p2 = Pessoa()
p2.nome = 'miranda'
p2.sobrenome = 'moana'
print(p2.nome)
print(p2.sobrenome)