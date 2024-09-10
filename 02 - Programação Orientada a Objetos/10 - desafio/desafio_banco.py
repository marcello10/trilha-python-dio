from abc import ABC, abstractmethod
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self,valor):
        pass
    @abstractmethod
    def registrar(self,conta):
        pass
class Deposito(Transacao):
    def __init__(self, valor:float) -> None:
        self.__valor = valor
    @property
    def valor(self):
        return self.__valor
    def registrar(self, conta):
        conta.depositar(self.__valor)
class Saque(Transacao):
    def __init__(self, valor:float) -> None:
        self.__valor = valor
    def registrar(self, conta):
        conta.sacar(self.__valor)
class Historico:
    def adicionar_transacao(self,transacao: Transacao):
        pass
class Conta:
    def __init__(self, cliente,numero:int):
        self.__numero = numero
        self.__cliente:Cliente = cliente
        self.__saldo = 0.0
        self.__agencia = "0001"
        self.__historico : Historico = None
    @property
    def saldo(self):
        return self.__saldo
    @property
    def numero(self):
        return self.__numero

    @property
    def agencia(self):
        return self.__agencia
    @property
    def cliente(self):
        return self.__cliente
    @property
    def historico(self):
        return self.__historico
    def depositar(self,valor):
        if valor > 0:
            self.__saldo += valor
            return True
        else:
            print("Invalid value, must be greater than zero")
            return False
    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            return True
        else:
            print("Invalid value or insufficient funds")
            return False
    @classmethod
    def nova_conta(cls, cliente,numero):
        if isinstance(cliente,Cliente):
            return cls(cliente, numero)
class ContaCorrente(Conta):
    def __init__(self, cliente, numero: int, limite:float, limite_saques:int):
        super().__init__(cliente, numero)
        self.__limite = limite
        self.__limite_saques = limite_saques
class Cliente:
    def __init__(self, endereco, contas = []):
        self.__endereco = endereco
        self.__contas = contas
    
    @property
    def endereco(self):
        return self.__endereco
    def adcionar_conta(self,conta: Conta):
        if isinstance(conta,Conta):
            self.__contas.append(conta)
class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf,data_nascimento):
        super().__init__(endereco)
        self.cpf = cpf
        self.data_nascimento = data_nascimento