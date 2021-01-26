class Pessoa:

    def __init__(self, name, cpf, genre):
        self.__name = name
        self.__cpf = cpf
        self.__genre = genre

    def get_name(self):
        return self.__name


class Cliente(Pessoa):
    """Cliente herda de Pessoa"""

    def __init__(self, name, cpf, genre, salary):
        super().__init__(name, cpf, genre)
        self.__salary = salary

    # Overriding method
    def get_name(self):
        return 'name: ' + self._Pessoa__name

    def get_full_name(self):
        return super().get_name()


cliente = Cliente('Marcelo Soares', 1234567812, 'M', 1000)

# Para acessar o atributo privado usar o nome da classe pai
print(cliente._Pessoa__name)
print(cliente.get_full_name())
print(cliente.get_name())

print(cliente.__dict__)

