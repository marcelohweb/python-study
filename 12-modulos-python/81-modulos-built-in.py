"""
Ver módulos built in em https://docs.python.org/3/py-modindex.html
"""

# É possível fazer o import com um alias

# import random as rdm

# print(rdm.random())

# Podemos importar todas as funções de um módulo

# from random import *

# print(random())  # Não precisa usar o nome do módulo

# Também é possível atribuir alias à função

# from random import random as rand

# print(rand())

# Para imprtar várias funções do mesmo módulo, utilizamos como uma tupla, com um por linha

from random import (
    random as rand,
    choice,
    randint
)

print(rand())
