# Maria pegou um emprestimo de 1.000.000
# para realizar o pagamento de 5 anos.
# A data em que ela pegou o emprestimo foi
# 20/12/2022 e o vencimento de cada parcela
# é no dia 20 de cada mês
# - Crie a data do empréstimo
# - crie a data do final do empréstimo
# - mostre todas as datas de vencimento e o valor das parcelas
from datetime import datetime
from dateutil.relativedelta import relativedelta

valor_emprestimo = 1000000
fmt = '%d/%m/%Y'
data_emprestimo = datetime.strptime('20/12/2022', fmt)
anos = relativedelta(years=5)

data_final = data_emprestimo + anos
data_parcelas = []
data_parcela = data_emprestimo


while data_parcela < data_final:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)
    

numero_parcelas = len(data_parcelas)

valor_parcela = valor_emprestimo / numero_parcelas
i = 1

for data in data_parcelas:
    print(f'{i}º parcela em :', data.strftime('%d/%m/%Y'), f'parcela de {valor_parcela:.7}')
    i += 1