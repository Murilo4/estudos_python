class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

class Motor:
    def __init__(self, nome):
        self.motor = nome

class Fabricante:
    def __init__(self, nome):
        self.fabricante = nome



fusca = Carro('fusca')
motor1_3 = Motor('1.3')
fusca.motor = motor1_3
volkswagen = Fabricante('volkswagen')

fusca.fabricante = volkswagen

print(fusca.nome, fusca.motor.motor, fusca.fabricante.fabricante)