"""
- Generators -> São iterators

Obs. O contrário não é verdadeiro. Ou seja, nem todo iterador é um generator.

Outras informações
- Generators podem ser criados com funções geradoras;
- Funções geradoras utilizam a palavra reservada yield;
- Generators podem ser criados com Expressões Geradoras.

Diferenças entre funções e generator functions (funções geradoras)
-----------------------------------------------------------------------------
| Funções                           | Generator Function                    |
-----------------------------------------------------------------------------
| utilizam return                   | utilizam yield                        |
-----------------------------------------------------------------------------
| retorna uma vez                   | podem utilizar yield múltiplas vezes  |
-----------------------------------------------------------------------------
| Funções                           | Generator Function                    |
-----------------------------------------------------------------------------
"""

# Exemplo de generator function


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador  # Retorna um generator
        contador = contador + 1


gen = conta_ate(5)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


def func_gera_lista(num):
    nums = []
    while len(nums) < num:
        nums.append(len(nums))
    return nums


# 41Mb
for i in func_gera_lista(1000000):
    print(i)


def generator_gera_lista(num):
    contador = 1
    while contador < num:
        contador
        yield contador
        contador = contador + 1


# 2,9Mb
for i in generator_gera_lista(1000000):
    print(i)
