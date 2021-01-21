"""
Doctests

Para executar o doctest: python -m doctest -v doctests.py
"""


def soma(a, b):
    """soma os números a e b

    >>> soma(1, 2)
    3
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
