# with open (context manager) e metodos uteis do textiowrapper
# usamos a função open para abrir
# um arquivo em python (ele pode ou não exister)
# modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binario)
# t (modo texto), + (leitura e escrita)
# context manager - with (abre e fecha)
# metodos uteis
# write, read (escrever e ler)
# writelines (escrever varias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# vamos falar mais sobre os módulos os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# json.dump = gera um arquivo json
# json.load
import os
caminha_arquivo = 'criacao_arquivos2.txt'

with open(caminha_arquivo, 'w', encoding='utf8') as arquivo:
    arquivo.write('atenção\n')
    arquivo.write('linha 1\n')
    arquivo.write('linha 2\n')
    arquivo.writelines(
        ('linha 3\n', 'linha 4\n')
    )
# os.unlink(caminho_arquivo)
# os.remove(caminho_arquivo)
os.rename(caminha_arquivo, 'aula116-2.txt')