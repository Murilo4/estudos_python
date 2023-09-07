from itertools import zip_longest

l1 = ['salvador', 'ubatuba', 'belo horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
print(list(zip(l1, l2)))
print(list(zip_longest(l1, l2, fillvalue='Sem cidade')))
