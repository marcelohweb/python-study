# -*- coding: utf-8 -*-
"""
[1] - Utilize Camel Case para nomes de classes
[2] - Utilize nomes em minúsculos, separados por underline para funções ou variáveis
[3] - Utilize 4 espaços para identação
[4] - Linhas em branco
    - Separar funções e definições de classes com duas linhas em branco
    - Métodos dentro de uma classe devem ser separados com uma única linha em branco
[5] - Imports
    - Devem ser sempre feitos em linhas separadas;
# Import errado
import sys
import os

Não há problema em utilizar:

from types import StringType, ListType

# Recomenda-se

from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)
# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings e
# antes de constantes ou variáveis globais

"""

'''
Comentário
'''

"""
Comentário
"""

"""
class Calculadora:
    pass

def soma():
    pass

if 'a' in 'banana':
    print('tem')

# Não faça:

funcao( algo[ 1 ], { outro: 2 } )

# Faça:

funcao(algo[1], {outro:2})

# Não faça

algo (1)

# Faça

algo(1)
"""