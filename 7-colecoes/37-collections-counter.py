"""
Módulo Collections - Counter (Contador)

Collections -> High-performance Container Datetypes

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido
com um dicionário, conendo como chave o elemento da lista passada como parâmetro e o como valor a quantidade de
ocorrências desse elemento.
"""

# Utilizando o Counter

from collections import Counter

# Exemplo 1

# Podemos utilizar qualquer iterável, aqui usamos uma lista
lista = [1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5]

res = Counter(lista)

print(type(res))
print(res)

# Exemplo 2

# Prints Counter({'a': 2, 'r': 2, 'e': 2, 'o': 2, 'M': 1, 'c': 1, 'l': 1, ' ': 1, 'S': 1, 's': 1})
# Como string é iterável, cria-se uma chave para cada letra com a quantidade de ocorrências como valor
print(Counter('Marcelo Soares'))

# Exemplo 3

texto = """
Python é uma linguagem de programação de alto nível,[5] interpretada, de script, imperativa, orientada a objetos, 
funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991.
[1] Atualmente possui um modelo de desenvolvimento comunitário, aberto e gerenciado pela organização sem 
fins lucrativos Python Software Foundation. Apesar de várias partes da linguagem possuírem padrões e 
especificações formais, a linguagem como um todo não é formalmente especificada. O padrão de facto é a 
implementação CPython.

See more: https://docs.python.org/3/library/collections.html#collections.Counter
"""

palavras = texto.split()

res = Counter(palavras)

print(res)

print(help(Counter))
