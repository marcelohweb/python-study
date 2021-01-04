"""
Map

Com map, fazemos mapeamento de valores para função.
"""

import math


def area(r):
    """Calcula a área de umm círculo com raio 'r"""
    return math.pi * (r ** 2)


print(area(2))
print(area(5))

# Suponha que tenamos uma lista de raios

raios = [2, 5, 8, 10]

# Map é uma função que recebe dois parâmetros. O primeiro é a função, o segundo é um iterável

areas = map(area, raios)

print(type(areas))  # Prints <class 'map'>
print(areas)  # Prints <map object at 0x7f17fd7e3940>

# Imprime o resultado da função area para cada item da lista
print(list(areas))

# Map com lambda

print(list(map(lambda r: math.pi * (r ** 2), raios)))
