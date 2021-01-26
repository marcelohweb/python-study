class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    # Por mais que seja um método, a annotation property permite que acessemos sem os (), como se fosse um atributo.
    # Ex: conta.numero
    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def limite(self):
        return self.__limite

    # Obs. limite é acessado com self.limite porque é uma property
    @property
    def valor_disponivel(self):
        return self.__saldo + self.limite

    # Getters e setters

    # Podemos setar o saldo sem os (). Ex: conta.saldo = 300
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    # Podemos obter o saldo sem os (). Ex: conta.saldo
    @saldo.getter
    def saldo(self):
        return self.__saldo

    def mostra_saldo(self):
        print(f'Saldo de {self.__saldo} do cliente {self.__titular}')


conta1 = Conta('Marcelo Soares', 100, 500)
conta2 = Conta('João da Silva', 200, 500)

conta1.mostra_saldo()

print(conta1.__dict__)
print(conta2.__dict__)

print(conta1.saldo)

conta1.saldo = 500
print(conta1.saldo)
print(conta1.valor_disponivel)