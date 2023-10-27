# Variaveis de ambiente com python
# para variaveis de ambiente
# Windows PS: $env:VARIAVEL="VALOR" | dir env:
# Linux e Mac: export NOME_VARIAVEL="VALOR" | echo $VARIAVEL
# Para obter o valor das variaveis de ambiente
# os.getenv ou os.environ['VARIAVEL']
# Para configurar variaveis de ambiente
# os.environ['VARIAVEL'] = 'valor'
# Ou usando python-dotenv e o arquivo .env
# pip install python-dotenv
# from dotenv import load_dotenv
# load_dotend()
# OBS.: sempre lembre-se de criar um .env-example
import os

# senha = os.getenv('SENHA')
# print(senha)

from dotenv import load_dotenv
load_dotenv()

# print(os.environ)
print(os.getenv('BD_PASSWORD'))
