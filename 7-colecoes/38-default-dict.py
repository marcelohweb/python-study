"""
Módulo Collections - Default Dict

Ao criar um dicionário utilizando o default dict, nós informamos um valor default, podendo utilizar um lambda
para isso. Este valor será usado sempre que não houver um valor definido ou caso tentemos acessar uma chave
que não existe.

Obs. Lambdas sã funções sem nome, que podem ou não receber parâmetros de entrada ou retornar valores

See more: https://docs.python.org/3/library/collections.html#collections.defaultdict
"""

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

print(type(dicionario))
print(dicionario)

dicionario['nome'] = 'Marcelo'
print(dicionario)

print(dicionario['nome'])

# Prints 0
print(dicionario['outro'])



