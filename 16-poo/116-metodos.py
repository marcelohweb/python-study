"""
Há dois tipos de métodos

- Métodos de instância
- Métodos de Classe
- Métodos estáticos

Obs. Todo elemento em python que inicia e finaliza com duplo underline é chamado de dunder (Double Underline)

Obs. Os métodos dunder em Python são chamados de métodos mágicos.

Eviar criar métodos próŕios com dunder
"""


class Cliente:

    def __init__(self, cpf, name):
        self.__cpf = cpf
        self.__name = name

    # Método privado
    def __formata_nome_cliente(self):
        return self.__name.upper()

    def get_nome_cliente(self):
        return self.__formata_nome_cliente()


class ContaCorrente:

    contador = 0

    moeda = 'R$'

    def __init__(self, cliente, saldo):
        ContaCorrente.contador = ContaCorrente.contador + 1
        self.__conta = ContaCorrente.contador
        self.__saldo = saldo
        self.__cliente = cliente

    def imprime_saldo(self):
        """Imprime o saldo da conta"""
        print(f'Seu saldo é: {ContaCorrente.moeda}{self.__saldo}')

    def get_conta(self):
        return self.__conta

    # Método de classe -> estático
    # cls é uma convensão utilizada para representar a classe
    @classmethod
    def get_qtd_contas(cls):
        print(cls)  # Prints <class '__main__.ContaCorrente'>
        return cls.contador

    # Não consegue mudar o estado da classe.
    # Geralmente são métodos que fazem alguma operação apenas com os parâmetros passados
    @staticmethod
    def my_static_method():
        return 'Hi'


cliente = Cliente(12345678901, 'Marcelo Soares')
print(cliente.get_nome_cliente())
# Acessar método privado
print(cliente._Cliente__formata_nome_cliente())

conta1 = ContaCorrente(cliente, 100)
conta1.imprime_saldo()

print(conta1._ContaCorrente__cliente._Cliente__name)

print(conta1.__dict__)

# Também consigo acessar como se fosse um método estático, porém passando a instância como o self
print(ContaCorrente.imprime_saldo(conta1))

# Métodos de classe

print(f'Atualmente temos {ContaCorrente.get_qtd_contas()} conta(s) aberta(s)')
print(f'Atualmente temos {conta1.get_qtd_contas()} conta(s) aberta(s)')  # it works

nome = 'Marcelo Soares'

# Métodos estáticos
print(ContaCorrente.my_static_method())
