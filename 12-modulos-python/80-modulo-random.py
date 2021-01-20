"""
Em python, módulos nada mais são do que outros arquivos python.

Módulo Random -> Possui várias funções para geração de números pseuso-aleatório.
"""

# Existem duas formas de se utilizar um módulo ou função do random

# Forma 1 - Importando todo o módulo - não recomendado. É recomendado importar apenas o que for necessario

# import random

# print(random.random())

# Obs. Ao realizar o import de todo o módulo, todas as
# funções/atributos/classes/propriedades do módulo estarão disponíveis

from random import random, uniform, choice, shuffle

# Como importei apenas a função não preciso acessar por random.random()
print(random())

# Gera um número peuso-aleratório entre dois valores
print(uniform(3, 7))

jogadas = ['pedra', 'papel', 'tesoura']

# Seleciona um valor aleatoriamente a partir de uma lista
print(choice(jogadas))

shuffle(jogadas)

print(jogadas)
