"""
1 - Em Python, quando uma função não contém retorno definido, o retorno é None
2 - Podemos ter diferentes returns
3 - Podemos retornar qualquer tipo de dado e até mesmo múltiplos valores* tupla
"""

from random import random


def say_hi():
    print('Hi')


ret = say_hi()

# Prints None
print(ret)


def return_hi():
    return 'Hi'


ret = return_hi()
print(ret)

# Exemplo com returns de tipos diferentes


def nova_funcao():
    variavel = True
    if variavel:
        return 1
    else:
        return False


ret = nova_funcao()

# Exemplod e retorno de múltiplos valores


def outra_funcao():
    return 2, 3, 4, 5, 'a', True


# Na verdade a função retorna uma tupla.
print(type(outra_funcao()))

# O que estamos fazendo é desempacotar uma tupla
num1, num2, num3, num4, string, boolean = outra_funcao()

print(type(num1))
print(type(string))
print(type(boolean))


def joga_moeda():
    valor = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'


print(joga_moeda())
