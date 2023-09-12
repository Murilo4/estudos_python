# metodos em instancias de classes python
# hard coded - é algo que foi escrito diretamente no código

class Car:
    def __init__(self, nome):
        self.nome = nome
    def trottle(self):
        print(f'{self.nome} esta acelerando...')

fusca = Car('Fusca')
print(fusca.nome)
fusca.trottle()

celta = Car(nome='celta')
print(celta.nome)
celta.trottle()