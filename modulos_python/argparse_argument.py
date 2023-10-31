# argparse.ArgumentParser para argumentos mais complexos
# Tutorial oficial:
# https://docs.python.org/pt-br/3/howto/argparse.html

from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-b', '--basic',
    help='Mostra "Olá mundo" na tela',
    Type=str,
    metavar='STRING',
    default='Olá mundo',
    required=True,
    action='append', # Recebe o argumento mais de uma vez
    #nargs='+', # recebe mais de um valor
)
args = parser.parse_args()

if args.b is None:
    print('Você não passou o valor de b.')
else:
    print('O valor de b:', args.b)

