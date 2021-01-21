"""
Doctests

Para executar o doctest:

python -m doctest -v doctests.py
"""


def soma(a, b):
    """soma os números a e b

    >>> soma(1, 2)
    3

    >>> soma(4, 6)
    10
    """
    return a + b


def formata_moeda(valor):
    """
    formata valor
    :param valor:
    :return:

    >>> formata_moeda(10)
    'R$10'
    """
    return 'R$' + str(valor)


print(formata_moeda(10))


# Obs. a ... dentro do resultado significa que há um conteúdo no meio
def duplicar(valores):
    """duplica os valores em uma lista

    >>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> duplicar(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> duplicar([])
    []

    >>> duplicar([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
    """
    return [item * 2 for item in valores]


# Erro inesperado

def fala_oi():
    """fala oi

    >>> fala_oi()
    'oi'
    """

    return "oi"  # Mesmo retornando a string com aspas duplas, será exibida no console com aspas simples


def verdade():
    """retorna True

    >>> verdade()
    True
    """

    return True
