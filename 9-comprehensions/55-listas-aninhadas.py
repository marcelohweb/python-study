"""
Listas Aninhadas (Nested Lists)

- Em algumas linguagens temos:
    - Arrays unidimensionais (arrays/vetores)
    - Multidimensionais (matrizes/array de array)

Em Python temos as listas

numeros = [1, 2, 3, 4, 5]
"""

# Exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3 x 3

print(listas)
print(type(listas))  # Prints <class 'list'>

# Acessando os elemnetos

print(listas[0][1])  # Prints 2
print(listas[1][2])  # Prints 6
print(listas[2][0])  # Prints 7

# Iterando

for lista in listas:
    for num in lista:
        print(num)

# Como iterar com list comprehension

[[print(valor) for valor in lista] for lista in listas]

# Outros exemplos

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)
