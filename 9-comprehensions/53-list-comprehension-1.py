"""
Utilizando List Comprehension nós podemos gerar novas listas com dados processados a partir de outro iterável

# Syntax

[ dado for dado in iterável ]
"""

from datetime import datetime

# Exemplos

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)

res = [numero / 2 for numero in numeros]

print(res)


def quadrado(valor):
    return valor * valor;


res = [quadrado(numero) for numero in numeros]

print(res)

nomes = ['Marcelo', 'Joao', 'Augusto', 'Ana', 'Rafaela']

nomes_maiusculos = [nome.upper() for nome in nomes]

print(nomes_maiusculos)

# Outro exemplo

print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])
