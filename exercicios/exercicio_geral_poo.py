"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa (ABC)
    Cliente
        Clente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)"""
import abc

class Person(abc):
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Client(Person):
    def Conta(self, ):
        ...
    """
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
"""
class Account(abc):
    def __init__(self, agency, account_number, number_type_account, amount):
        self.agency = agency
        self.account_number = account_number
        self.number_type_account = number_type_account
        self.amount = amount

    def type_account(self):
        if self.number_type_account == '01':
            return checking_account(self.agency, self.account_number, self.number_type_account, self.amount)
        
        elif self.number_type_account == '013':
            return savings_account(self.agency, self.account_number, self.number_type_account, self.amount)
        
        else:
            return f'este tipo de conta não existe'
        
    
    

class savings_account(Account):

    def deposit(self):
        
        if self.amount < 0:
            print(f'você esta negativado em1 {self.amount}, com o deposito, parte deste valor irá para quitar sua divida! ')
            deposit_value = input('informe o valor desejado para depositar:')
            valor = float(deposit_value)
            self.amount += valor
            print(f'valor depositado com sucesso! {self.amount}')
            return self.amount
        
        deposit_value = input('informe o valor desejado para depositar:')
        valor = float(deposit_value)
        self.amount += valor
        print(f'valor depositado com sucesso! {self.amount}')
        return self.amount

    
    def limit(self, amount):
        if amount == 0:
            print(f'você esta com o saldo zerado')
        elif amount < 0:
            print(f'você esta negativado, você está devendo {amount}')
        else:
            print(f'seu saldo atual é de {amount}')

class checking_account(Account):
     def deposit(self):

        if self.amount < 0:
            print(f'você esta negativado em {self.amount}, com o deposito, parte deste valor irá para quitar sua divida! ')
            deposit_value = input('informe o valor desejado para depositar:')
            valor = float(deposit_value)
            self.amount += valor
            print(f'valor depositado com sucesso! {self.amount}')
            return self.amount
        
        deposit_value = input('informe o valor desejado para depositar:')
        valor = float(deposit_value)
        self.amount += valor
        print(f'valor depositado com sucesso! {self.amount}')
        return self.amount


conta1 = Account(1234, 3253523, '01', -40)
conta1 = Account.type_account()


            
    
        


"""
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""

