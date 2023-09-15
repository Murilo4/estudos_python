# @property - um getter no modo pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um 
# atributo
# geralmente é usada nas seguintes situações
# - como getter
# - p / eviar quebrar código cliente
# - p / hibilitar setter
# - p / executar ações ao obter um atributo
# codigo cliente - é o código que usa seu código

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        print('PROPERTY')
        return self.cor_tinta
    
    @property
    def cor_tampa(self):
        return 123456
    

caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)


# class Caneta:
#     def __init__(self, cor):
#         self.cor_tinta = cor

#     def get_cor(self):
#         return self.cor_tinta     maneira não pythonica
    



