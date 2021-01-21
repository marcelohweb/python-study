"""

Unittest -> Testes Unitários

Unidades individuais podem ser: funções, métodos, classes, módulos, etc.

Para criar nossos testes, criamos classes que herdam de unittest.TestCase
e a partir de então temos acesso a todos os 'assertions' presentes no módulo

Para rodar os testes, utilizamos uniittest.main()

TestCase -> Casos de teste para a sua unidade

Conhecendo os assertions

assertEqual(a, b)
assertTrue(x)
...

See more: https://docs.python.org/3/library/unittest.html

Por convenção, todos os testes devem iniciar com test_

* Ver arquivo test_unit_test.py

"""


# Prática - Utilizando TDD
def comer(comida, is_saudavel):
    if is_saudavel:
        return f'Estou comendo {comida} porque é saudável'
    else:
        return 'Comida não saudável'


def dormir():
    return 'Estou dormindo'
