# desempacotamento em chamadas
# de metodos e funções

string = 'ABCD'
lista = ['maria', 'helena', 1,2,3, 'eduarda']
tupla = 'python', 'é', 'legal'
salas = [
    # 0           1
    ['maria', 'helena', ], # 0
    # 0           
    ['elaine', ] # 1
    # 0        1        2
    ['luiz', 'joão', 'eduarda', ], # 2
]

# p, b, *_, ap, u = lista
# print(p, u, ap)

#print('maria', 'helena', 1,2,3, 'eduarda')
#print(*lista)
#print(*string)
#print(*tupla)

print(*salas, end='\n')