"""
Stack memory            |            Haep Memory
"""


class Carro:

    def __init__(self, cor):
        self.__cor = cor


carro1 = Carro('Branco')

"""
Stack memory            |            Haep Memory
carro1                  |            Carro#xyz - 1 referência
"""

carro2 = carro1

"""
Stack memory            |            Haep Memory
carro1                  |            Carro#xyz - 2 referências
carro2                  |
"""

carro1 = None

"""
Stack memory            |            Haep Memory
carro2                  |            Carro#xyz - 1 referência
"""

carro2 = Carro('Preto')

"""
Stack memory            |            Haep Memory
                                     Carro#xyz - 0 referências - Dead Object
carro2                  |            Carro#abc - 1 referência
"""

# A partir desse momento, o Garbage Collector entra em ação com o algoritmo Reference Counting para "limpar"
# esses objetos que não possuem mais referências

# Diferentes linguagens de programação utilizam diferentes algorítmos para o garbage collector

# Obs. Python é dinamicamente tipado. Não precisamos informar o tipo no momento da criação da variável
valor = 3  # O python infere que essa variável é do tipo inteiro

# Estaticamente tipada, seria int valor = 3

# Python é fortemente tipada.
# Isso significa que o python não faz conversões (casts) automaticamente ao realizar operações.

# Ex:

idade = 28
nome = 'João'

print(nome + ' tem ' + str(idade) + ' anos')  # Necessário converter o inteiro para string

# Em linguagens fracamente tipadas, como o PHP, não seria necessário.

