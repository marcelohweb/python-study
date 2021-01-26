class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def faz_som(self, som):
        print(f'{self.__nome} faz {som}')


class Gato(Animal):

    def __init__(self, nome):
        # Animal.__init__(self, nome)  # it works
        super().__init__(nome)


gato = Gato('Buza')
gato.faz_som('miau')
