condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('faça algo')
else:
    print('não faça algo')

if passou_no_if is None:
    print('não passou no if')
else:
    print('passou no if')