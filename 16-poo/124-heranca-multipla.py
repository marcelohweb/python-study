"""
Pode ocorrer:

- Por multiderivação direta
- Por multiderivação indireta
"""

# Exemplo 1 - Multiderivação Direta


class Base1:
    pass


class Base2:
    pass


class MultiDerivada(Base1, Base2):
    pass


# Exemplo 2 - Multiderivação Indireta


class Base1:
    pass


class Base2 (Base1):
    pass


class Base3 (Base2):
    pass


class MultiDerivada(Base3):
    pass


# Obs. Não importa se a derivação é direta ou indireta. A classe que realizar a herança, herdará todos os atributos e
# métodos das superclasses.

class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'


class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} no mar!'


class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra!'


class Pinguim(Aquatico, Terrestre):

    def __init__(self, nome):
        super().__init__(nome)


baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre('Bola')
print(tatu.andar())
print(tatu.cumprimentar())

cacau = Pinguim('Cacau')
# Method Resolution Order (MRO) - Vai executar o método cumprimentar de Aquatico devido a ordem da herança
print(cacau.cumprimentar())

print(f'cacau é instância de Pinguim? {isinstance(cacau, Pinguim)}')
print(f'cacau é instância de Aquatico? {isinstance(cacau, Aquatico)}')
print(f'cacau é instância de Terrestre? {isinstance(cacau, Terrestre)}')
print(f'cacau é instância de Animal? {isinstance(cacau, Animal)}')
print(f'cacau é instância de Object? {isinstance(cacau, object)}')

# Prints the method resolution order
print(Pinguim.__mro__)

# Aqui também é exibido o method resolution order
help(Pinguim)
