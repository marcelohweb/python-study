"""
Documentando funções com Docstrings
"""

# Exemplos


def diz_oi():
    """Uma função simples que retorna a string 'Oi'!"""
    return 'Oi!'


print(diz_oi())
print(diz_oi.__doc__)


def exponencial(numero, potencia=2):
    """
    Retorna o exponencial de um número
    :param numero:
    :param potencia:
    :return:
    """
    return numero ** potencia


print(exponencial(2, 3))

print(exponencial.__doc__)
