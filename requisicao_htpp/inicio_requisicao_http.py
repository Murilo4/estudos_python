# O módulo requests para requisições HTTP no Python
# HTTP (HyperText Transfer Protocol) é um protocolo usado para enviar e receber
# dados na internet. Ele funciona no modo cliente/servidor, onde o cliente
# (seu navegador, por exemplo) faz uma requisição ao servidor
# (site, por exemplo), que responde com os dados adequados.

# A mensagem de requisição do cliente deve incluir dados como:
# - O método HTTP
#       - leitura (safe) - GET, HEAD (cabeçalhos), OPTIONS (métodos seguros)
#       - escrita - POST, PUT (substitui), PATCH (atualiza), DELETE
# - O endereço do recurso a ser acessado (/users/)
# - Os cabeçalhos HTTP (Content-Type, Authorization)
# - O corpo da mensagem (caso necessário, de acordo com o método HTTP)

# A mensagem de resposta do servidor deve incluir dados como:
# - código de status HTTP (200 success, 404 Not found, 301 Moved Permanently)
# - Os cabeçalhos HTTP (Content-Type, Accept)
# O corpo da mensagem (pode estar em vazio em alguns casos)
