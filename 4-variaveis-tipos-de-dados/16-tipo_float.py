"""
Tipo Float

Obs. O separador de casas decimais é o ponto e não a virgula
"""

# Errado - na verdade ele cria uma tupla e não um float
valor = 1,44

print(valor)
print(type(valor)) # <class 'tuple'>

# Certo
valor = 1.44

print(valor)
print(type(valor)) # <class 'float'>

# É possível
valor1, valor2 = 1,44

print(valor1)
print(valor2)

print(type(valor1)) # <class 'int'>
print(type(valor2)) # <class 'int'>

# OBS - Ao converter float para inteiros, perdemos precisão
valor_int = int(valor)
print(valor_int)
print(type(valor_int)) # <class 'int'>

# É possível converter de inteiro para float
valor_float = float(valor_int)
print(valor_float)
print(type(valor_float)) # <class 'float'>