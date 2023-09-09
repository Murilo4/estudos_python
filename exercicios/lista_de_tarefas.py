
def listar(tarefas):
    print()
    if not tarefas:
        print('não há nenhuma tarefa')
        return
    print('tarefas:')

    for tarefa in tarefas:
        print(f'\t{tarefa}')


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('não há nenhuma tarefa para desfazer')
        return
    
    tarefa = tarefas.pop()
    tarefas_refazer.append(tarefa)

def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('não há nenhuma tarefa para desfazer')
        return
    
    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)
    
def adicionar(tarefas, comando):
    print()
    comando.split()
    if not comando:
        print('você não digitou uma tarefa')
    
    tarefas.append(comando)



tarefas = []
tarefas_refazer = []

while True:
    print('comandos: listar, refazer, desfazer')
    comando = input('digite o comando:')
    if comando == 'listar':
        listar(tarefas)
        continue
    elif comando == 'refazer':
        refazer(tarefas, tarefas_refazer)
        continue
    elif comando == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        continue
    else: 
        adicionar(tarefas, comando)
        listar(tarefas)
