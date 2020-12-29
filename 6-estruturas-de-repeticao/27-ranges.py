"""
Ranges são utilizados para gerar sequências numéricas, não de forma aleatória, mas sim de maneira especificada

OBS. O valor de parada não é inclusivo
"""

# Forma 1
# Quando apenas um valor é especificado, é considerado como valor de parada e o valor de início será 0
# Imprime de 0 a 10
for num in range(11):
    print(num)

# Forma 2
# Imprime de 0 a 9
for num in range(0, 10):
    print(num)

# Forma 3
# O terceiro parâmetro é o passo. Neste caso salta de 2 em 2
# Imprime 1, 3, 5, 7, 9
for num in range(1, 10, 2):
    print(num)

# Forma 4
# Ordem decrescente
for num in range(10, 0, -1):
    print(num)

lista = range(0, 10)

# prints range(0, 10)
print(lista)

lista = list(range(0, 10))

# prints [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista)
