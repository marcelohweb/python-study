"""
Criando sua própria versão de loop
"""


def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


meu_for('abc')

numeros = [1, 2, 3, 4, 5]

meu_for(numeros)

