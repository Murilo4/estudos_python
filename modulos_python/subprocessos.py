# usando subprocess para executar comandos externos
# subprocess é um módulo do python para executar
# processos e comandos externos no seu programa
# o método mais simples para atingir o objetivo é usando subprocess.run()
# Argumentos principais de subprocess.run()
# - stdout, stdin e stderr -> redirecionam saida, entrada e erros
# - capture_output -> captura a saida e/ou erro para uso posterior
# - text -> se True, entradas e saidas serão tratadas como texto
# e automaticamente codificadas ou decodificadas com o conjunto
# de caracteres padrão da plataforma (geralmente UTF-8).
# - shell -> se True, terá acesso ao shell do sistema. Ao usar
# shell (True), recomendo enviar o comando e os sargumentos juntos.
# - executable -> pode ser usado para especificar o caminho
# do executavel que iniciará o subprocesso.
# retorno:
# stdout, stderr, returncode e args
# importante: a codificação de caracteres do Windows pode ser 
# diferente. Tente usar cp1252, cp852, cp850 (ou outros). Linux e
# mac, use utf_8.
# comando de exemplo:
# windows: ping 127.0.0.1
# linux/mac: ping 127.0.0.1 -c 4

import subprocess
import sys

# sys.platform = linux, linux2, darwin, win32

cmd = ['ping', '127.0.0.1', '-c', '4']
encoding = 'uft_8'
system = sys.platform

if system == 'win32':
    cmd = ['ping', '127.0.0.1']
    encoding = 'cp850'

proc = subprocess.run(
    cmd, capture_output=True,
    text=True, encoding=encoding
)

print()


print(proc.stdout)

