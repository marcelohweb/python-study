"""
Podenos adicionar estruturas condicionais em nossas List Comprehension
"""

# Exemplos

numeros = [1, 2, 3, 4, 5]

pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

impares = [numero for numero in numeros if numero % 2 == 1]

print(impares)

# Outro exemplo

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)
