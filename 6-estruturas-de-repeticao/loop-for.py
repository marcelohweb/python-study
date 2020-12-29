"""
Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis
"""

nome = 'Marcelo Soares'

for letra in nome:
    print(letra)

lista = ['a', 'b', 'c']

for item in lista:
    print(item)

numeros = range(1, 10)

for numero in numeros:
    print(numero)

# Vai imprimir até o 4 porque no range o valor final não é incluso
for numero in range(1, 5):
    print(numero)

nome = 'Marcelo Soares'
for k, v in enumerate(nome):
    print(k, v)

# Decarta a chave
for _, v in enumerate(nome):
    print(v)

for v in enumerate(nome):
    print(v)

qtd = int(input("Quantas vezes o loop deve iterar?"))

for numero in range(1, qtd+1):
    print(numero)

# Concatenação
nome = 'Marcelo'
nome += ' Soares'
print(nome)

# Isso repete o nome duas vezes
nome = nome * 2
print(nome)
