"""
Comandos básicos do PDB

l (listar onde estamos no código)
n (próxima linha)
p (imprime variável)
c (continua a execução - finaliza o debugging)

A partir da versão 3.7, não é mais necessário importar a biblioteca pdb e então utilizar a função set_trace()
A função foi incorporada como built-in e chamada breakpoint()
"""

import pdb

name = 'oi'


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um erro: {err}'


print('hi')


print(dividir(4, 2))

pdb.set_trace()

valor1 = 10
valor2 = 5

res = valor1 + valor2
