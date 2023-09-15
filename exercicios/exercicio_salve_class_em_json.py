# Exercicio - salve sua classe em JSON
# salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# faça em arquivos separados
import json

CAMINHO_ARQUIVO = 'exercicio_salve_class_em_json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('joão', 33)
p2 = Pessoa('helena', 21)
p3 = Pessoa('joana', 11)
bd = [vars(p1), p2.__dict__, vars(p3)]

def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        print('fazendo dump')
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    print('ELE É O __main__')
    fazer_dump()

