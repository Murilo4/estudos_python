# sets são eficientes para remover valores duplicados de iteraveis
# seus valores serão sempre unicos;
# não tem indexes;
# não garantem ordem;
# são iteraveis (for, in, not in)
# l1 = [1, 2, 3, 3, 3, 3, 1]
# s1 = set(l1)
# s1 = set(l1)
# l2 = list(s1)
s1 = {1, 2, 3}
# print(3 not in s1)
for numero in s1:
    print(numero)

#metodos uteis:
# add, update, clear, discard
s1 = set()
s1.add('luiz')
s1.add(1)
s1.update(('ola mundo',  1, 2, 3, 4))
s1.clear()
s1.discard('ola mundo')
s1.discard('luiz')
print(s1)
