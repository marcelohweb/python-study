"""
Módulo Collections - Named Tuple
"""

from collections import namedtuple

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

pituca = cachorro(idade=10, raca='Poodle', nome='Pituca')

print(pituca)

# Acessando valores
print(pituca[0])

# Or
print(pituca.idade)




