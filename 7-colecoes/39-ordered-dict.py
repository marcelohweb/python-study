"""
Módulo Collections: OrderedDict

OrderedDict é um dicionário que garante a ordem de inserção dos elementos
"""

from collections import OrderedDict

# Em um dicionário, a ordem de inserção dos elementos não é garantida
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')

# Entendendo a diferença entre Dict e OrderedDict

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

# Prints true
print(dict1 == dict2)

dict1 = OrderedDict({'a': 1, 'b': 2})
dict2 = OrderedDict({'b': 2, 'a': 1})

# Prints false. OrderedDict leva em consideração a ordem dos elementos
print(dict1 == dict2)

